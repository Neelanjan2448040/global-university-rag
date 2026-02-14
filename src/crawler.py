import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from datetime import datetime
import time


def get_domain(url):
    """Extract domain from URL"""
    return urlparse(url).netloc


def is_relevant_page(url):
    """Check if URL is relevant for university information"""
    relevant_keywords = [
        'admission', 'admissions', 'apply', 'application',
        'program', 'programmes', 'courses', 'curriculum',
        'scholarship', 'financial-aid', 'funding', 'fees', 'tuition',
        'research', 'faculty', 'department',
        'computer-science', 'cs', 'engineering', 'computing',
        'about', 'overview', 'undergraduate', 'graduate',
        'requirements', 'eligibility', 'cost'
    ]
    url_lower = url.lower()
    return any(keyword in url_lower for keyword in relevant_keywords)


def crawl_website(base_url, max_pages=10):
    """
    Enhanced crawler that targets relevant university pages
    """
    visited = set()
    to_visit = [base_url]
    domain = get_domain(base_url)
    scraped_data = []
    
    # Add specific paths to prioritize
    priority_paths = [
        '/admissions', '/admission', '/apply',
        '/programs', '/academics', '/courses',
        '/scholarships', '/financial-aid', '/fees', '/tuition',
        '/research', '/faculty',
        '/computer-science', '/cs', '/engineering'
    ]
    
    # Add priority URLs
    for path in priority_paths:
        priority_url = urljoin(base_url, path)
        if priority_url not in to_visit:
            to_visit.insert(0, priority_url)

    while to_visit and len(visited) < max_pages:
        current_url = to_visit.pop(0)

        if current_url in visited:
            continue

        try:
            print(f"Crawling: {current_url}")
            response = requests.get(current_url, timeout=10, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            })
            response.raise_for_status()
            soup = BeautifulSoup(response.text, "html.parser")
            
            # Remove script and style elements
            for script in soup(["script", "style", "nav", "footer"]):
                script.decompose()
                
        except Exception as e:
            print(f"Error crawling {current_url}: {e}")
            continue

        visited.add(current_url)

        title = soup.title.string if soup.title else "No Title"
        university_name = domain

        # Extract main content more intelligently
        main_content = soup.find('main') or soup.find('article') or soup.find('div', class_='content') or soup.body
        
        if main_content:
            # Extract headings and their content
            headings = main_content.find_all(["h1", "h2", "h3"])
            
            for heading in headings:
                content = []
                
                # Get all text between this heading and the next
                for sibling in heading.find_next_siblings():
                    if sibling.name in ["h1", "h2", "h3"]:
                        break
                    if sibling.name in ["p", "ul", "ol", "div"]:
                        text = sibling.get_text(strip=True)
                        if text and len(text) > 20:  # Only meaningful content
                            content.append(text)

                if content:
                    scraped_data.append({
                        "url": current_url,
                        "university": university_name,
                        "title": title,
                        "section": heading.get_text(strip=True),
                        "content": " ".join(content),
                        "metadata": {
                            "scraped_at": str(datetime.now()),
                            "page_type": "admissions" if "admission" in current_url.lower() else
                                        "programs" if "program" in current_url.lower() else
                                        "financial" if any(x in current_url.lower() for x in ["fee", "tuition", "scholarship"]) else
                                        "research" if "research" in current_url.lower() else
                                        "general"
                        }
                    })

        # Add relevant internal links
        for link in soup.find_all("a", href=True):
            absolute_link = urljoin(current_url, link["href"])
            if get_domain(absolute_link) == domain and absolute_link not in visited:
                # Prioritize relevant pages
                if is_relevant_page(absolute_link):
                    to_visit.insert(0, absolute_link)  # Add to front
                elif len(to_visit) < max_pages * 2:
                    to_visit.append(absolute_link)  # Add to back
        
        time.sleep(0.5)  # Be respectful to servers

    print(f"Crawled {len(visited)} pages, extracted {len(scraped_data)} sections")
    return scraped_data