import scraper
import summarizer
import mailer
from datetime import datetime

def main():
    
    # Fetch the links
    print("Fetching today's articles from The Hacker News...")
    links = scraper.get_article_links()
    
    if not links:
        print("No articles found for today. Exiting.")
        return

    today_str = datetime.now().strftime("%b %d, %Y")
    email_subject = f"Your Daily Cyber Briefing - {today_str}"
    
    # HTML structure for the email
    email_body_html = f"<h2>Cybersecurity News for {today_str}</h2><hr>"
    
    for i, link in enumerate(links, 1):
        print(f"\nProcessing article {i}/{len(links)}: {link}")
        
        # Extract the raw text
        article_text = scraper.extract_article_text(link)
        if not article_text or article_text == "No article body found":
            print("Skipping due to missing text.")
            continue
            
        print("Summarizing with Gemini...")
        summary = summarizer.summarize_article(article_text)
        
        # Append the summary to our email body
        email_body_html += f"<h3>News Item {i} (<a href='{link}'>Source</a>)</h3>"
        
        # Directly append Gemini's HTML output to the email body
        email_body_html += f"{summary}<br><hr>"
        
    print("\nAll articles processed. Sending email...")
    mailer.send_email(email_subject, email_body_html)
    print("Done! Check your inbox.")

if __name__ == "__main__":
    main()