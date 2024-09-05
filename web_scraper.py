import requests
from bs4 import BeautifulSoup

URL = 'https://x.com' 

def fetch_webpage(url):
    """
    Fetch the content of a webpage.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return None

def parse_html(html):
    """
    Parse the HTML content using BeautifulSoup.
    """
    soup = BeautifulSoup(html, 'html.parser')

    # Example: Extracting all headlines (assuming <h2> tags for headlines)
    headlines = soup.find_all('h2')
    
    print("Headlines found on the page:")
    for i, headline in enumerate(headlines, 1):
        print(f"{i}. {headline.get_text(strip=True)}")

def main():
    """
    Main function to run the web scraper.
    """
    print("Fetching the webpage...")
    html_content = fetch_webpage(URL)
    
    if html_content:
        print("Parsing the webpage...")
        parse_html(html_content)
    else:
        print("Failed to retrieve the webpage content.")

if __name__ == "__main__":
    main()