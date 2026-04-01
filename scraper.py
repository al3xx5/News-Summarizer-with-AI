import requests
from bs4 import BeautifulSoup
from datetime import datetime

from urllib3 import response

def get_article_links():

    url = "https://thehackernews.com/"

    # headers to prevent request being blocked as a bot
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Failed to load homepage. Status code {response.status_code}")
        return []

    soup = BeautifulSoup(response.content, "html.parser")

    # Getting the article cards
    article_elements = soup.find_all("a", class_= "story-link")

    today_str = datetime.now().strftime("%b %d, %Y")

    todays_links = []

    for article in article_elements:
        link = article.get("href")

        # Date text is found next to calendar icon
        date_element = article.find("i", class_="icon-calendar")

        if date_element and date_element.parent:
            # Articles date
            date_text = date_element.parent.get_text(strip=True)


            # If today's date is on the articles date, save link
            if today_str in date_text:
                if link not in todays_links:
                    todays_links.append(link)


    # Fallback if couldn't find articles
    if not todays_links and article_elements:
        print(f"No articles matched today's date ({today_str}). Fetching the 3 latest articles instead.")
        return [a.get("href") for a in article_elements[:3]]

    return todays_links

def extract_article_text(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.content, "html.parser")

    article_body = soup.find("div", class_="articlebody")

    if not article_body:
        return "No article body found"

    paragraphs = article_body.find_all("p")
    text = "\n".join([p.get_text(strip=True) for p in paragraphs])

    return text


# TESTING BLOCK TO ENSURE SCRAPER IS WORKING
if __name__ == "__main__":
    print("Finding today's articles...")
    links = get_article_links()
    
    print(f"Found {len(links)} articles. Extracting content...\n")
    for link in links:
        print(f"Extracting from: {link}")
        content = extract_article_text(link)
        # Short preview of the text to confirm it works
        print(f"Preview: {content[:150]}...\n")
        print("-" * 50)