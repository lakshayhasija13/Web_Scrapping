import requests
from lxml import html

def simple_web_scraper_alternate(url):
    # Send an HTTP request to the specified URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using lxml
        tree = html.fromstring(response.content)
        
        # Extract information based on the HTML structure of the website
        article_titles = tree.xpath('//h2[@class="article-title"]/text()')
        
        # Print the extracted information
        for title in article_titles:
            print(title.strip())
    else:
        print(f"Failed to retrieve content. Status code: {response.status_code}")

# Example usage
url_to_scrape = 'https://exampleblog.com'
simple_web_scraper_alternate(url_to_scrape)
