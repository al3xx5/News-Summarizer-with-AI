from openai import OpenAI
import config

client = OpenAI(
    api_key=config.GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

def summarize_article(article_text):

    # Safety check in case the scraper failed to find text
    if not article_text or article_text == "No article body found":
        return "Error: No valid text provided to summarize."

    system_prompt = (
        "You are a highly intelligent, witty, and humorous AI cybersecurity news anchor. "
        "Your job is to read the provided tech/security news article and give a summary. "
        "You must strictly follow these rules:\n"
        "1. Provide Context: Briefly explain the underlying concepts, background, or 'why this matters' before diving into the news.\n"
        "2. Summarize: Give a clear, concise summary of the actual event or breach.\n"
        "3. Be Humorous: Inject lighthearted humor, wit, and a bit of sass into your delivery.\n"
        "4. Use Analogies: Explain the complex technical vulnerabilities using funny, relatable everyday analogies (e.g., comparing a firewall bypass to a bouncer at a club).\n"
        "5. Formatting: Output your response STRICTLY in raw HTML format. Use standard tags like <p>, <b>, <i>, <ul>, and <li> for formatting. DO NOT use any Markdown symbols (like ** or #)."
    )

    try:
        response = client.chat.completions.create(
            model="gemini-3-flash-preview",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": f"Here is the article text to summarize:\n\n{article_text}"}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred during summarization: {e}"

# Testing block to ensure summarizer is working
if __name__ == "__main__":
    # A dummy cybersecurity article for testing
    sample_text = (
        "Cybersecurity researchers have discovered a new vulnerability in the widely used "
        "FluxCapacitor open-source library. The flaw, tracked as CVE-2026-9999, allows remote "
        "attackers to bypass authentication mechanisms by sending a specially crafted sequence of "
        "null bytes in the login header. This results in a buffer overflow, granting the attacker "
        "full administrative privileges. The maintainers have released an emergency patch in version 4.2.1."
    )
    
    print("Sending test text to Gemini...\n")
    summary = summarize_article(sample_text)
    print("--- AI Summary ---\n")
    print(summary)