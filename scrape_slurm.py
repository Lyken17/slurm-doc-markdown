import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
import os
import re
import sys
from urllib.parse import urljoin, urlparse
from collections import deque

# Increase recursion limit to handle deep nesting in markdownify
sys.setrecursionlimit(50000)

BASE_URL = "https://slurm.schedmd.com/documentation.html"
DOMAIN = "slurm.schedmd.com"
OUTPUT_DIR = "docs"

# Set of visited URLs to avoid broken loops
visited = set()
pages_scraped = 0
MAX_PAGES = 500 # Safety limit

def fix_links(markdown_content):
    """
    Replaces .html links with .md links in markdown content.
    """
    def replacer(match):
        label = match.group(1)
        url = match.group(2)
        
        # Parse the URL to check if it's internal or external
        parsed = urlparse(url)
        
        # If it's a full URL and not our domain, leave it
        if parsed.scheme and parsed.netloc and DOMAIN not in parsed.netloc:
            return match.group(0)
            
        # If it ends with .html (ignoring query/fragment), replace with .md
        # We need to handle anchors like page.html#section
        
        if ".html" in url:
             new_url = url.replace(".html", ".md")
             return f"[{label}]({new_url})"
        
        return match.group(0)

    # Regex for markdown links: [label](url)
    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replacer, markdown_content)

def get_filename_from_url(url):
    path = urlparse(url).path
    if path.endswith('/'):
        return 'index.md'
    filename = os.path.basename(path)
    if filename.endswith('.html'):
        return filename[:-5] + '.md'
    return filename + '.md'

def process_url(url):
    """
    Scrapes a single URL and returns a list of new URLs to visit.
    """
    
    new_links = []

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract Title
    title = soup.title.string if soup.title else "Slurm Doc"
    
    # Try to find specific content to avoid navigation bars which might cause nesting issues
    content_element = soup.find('div', id='page') or soup.find('main') or soup.body
    
    if content_element:
        content_html = str(content_element)
    else:
        content_html = str(soup)

    try:
        # Convert to Markdown
        markdown = md(content_html, heading_style="ATX")
        
        # Clean up and Fix Links
        markdown = f"# {title}\n\n{markdown}"
        markdown = fix_links(markdown)
        
        # Save file
        filename = get_filename_from_url(url)
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(markdown)
    except Exception as e:
         print(f"Error converting {url}: {e}")
         return []

    # Find more links
    for a in soup.find_all('a', href=True):
        href = a['href']
        try:
            full_url = urljoin(url, href)
            parsed = urlparse(full_url)
            
            # Filter for same domain and .html extension
            if parsed.netloc == DOMAIN and parsed.path.endswith('.html'):
                new_links.append(full_url)
        except ValueError as ve:
            print(f"Skipping invalid URL from href '{href}': {ve}")
        except Exception as e:
            print(f"Error processing link '{href}': {e}")
            
    return new_links

def scrape_site():
    global pages_scraped
    to_scrape = deque([BASE_URL])
    
    while to_scrape and pages_scraped < MAX_PAGES:
        url = to_scrape.popleft()
        
        # Normalize URL by stripping fragment and query
        parsed_main = urlparse(url)
        url_no_frag = parsed_main.scheme + "://" + parsed_main.netloc + parsed_main.path
        
        if url_no_frag in visited:
            continue
            
        visited.add(url_no_frag)
        pages_scraped += 1
        
        print(f"Scraping {url_no_frag}...")
        found_links = process_url(url_no_frag)
        
        found_visited = 0
        for link in found_links:
            # Pre-check visited to avoid adding duplicates to queue
            parsed_link = urlparse(link)
            link_no_frag = parsed_link.scheme + "://" + parsed_link.netloc + parsed_link.path
            if link_no_frag in visited:
                found_visited += 1
            else:
                to_scrape.append(link)

        print(f"\t Found {len(found_links) - found_visited} (new) / {len(found_links)} (total) links")
        print(f"\t total scraped {pages_scraped}, remaining to scrape {len(to_scrape)}")

if __name__ == "__main__":
    scrape_site()
