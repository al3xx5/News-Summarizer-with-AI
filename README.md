# Daily Cybersecurity News Summarizer

> An automated Python script that delivers AI-generated, humor-infused summaries of the latest cybersecurity news directly to your email.

## Overview
This project is a modular CLI application that scrapes daily articles from The Hacker News. It leverages the Gemini AI model to digest complex technical vulnerabilities and explain them using relatable analogies. The final output is formatted as a clean HTML email and sent via Gmail's SMTP server. It is designed to run completely hands-off using GitHub Actions for daily scheduling.

## Features
*   **Automated Web Scraping:** Uses BeautifulSoup to dynamically locate and extract full article text published on the current date from The Hacker News.
*   **AI Summarization:** Integrates with Google's Gemini model via the OpenAI Python SDK to generate concise, witty, and analogy-rich summaries formatted directly in HTML.
*   **Email Delivery:** Bypasses plain text limitations by structuring the AI output into a readable email, complete with source links, using Python's built-in SMTP libraries.
*   **Cloud Scheduling:** Utilizes GitHub Actions to execute the script daily on a strict cron schedule without requiring a local machine to remain powered on.

## Prerequisites
*   **Python:** The core programming language required to execute the scripts locally.
*   **Google Account:** Necessary for generating the Gmail App Password to authenticate the email delivery.
*   **Google AI Studio Account:** Required to obtain the API key to access the Gemini AI models.
*   **GitHub Account:** Used for version control and hosting the automated deployment workflow.

## Local Installation
1. Clone the repository to your local machine.
2. Create a virtual environment using the command `python -m venv venv`.
3. Activate the virtual environment.
4. Install the required dependencies using the command `pip install -r requirements.txt`.
5. Create a file named `.env` in the root directory.

## Configuration
Add the following variables to your `.env` file to configure the application securely.

*   **GEMINI_API_KEY:** Your generated API key from Google AI Studio.
*   **EMAIL_ADDRESS:** The Gmail address that will send and receive the daily summaries.
*   **EMAIL_APP_PASSWORD:** The 16-character App Password generated from your Google Account security settings.

## Usage
To run the script manually on your local machine, ensure your virtual environment is active and execute the following command in your terminal.

`python main.py`

The terminal will output the progress of the scraping and summarization process. Upon completion, check your configured email inbox for the formatted report.

## Automated Deployment
This project includes a GitHub Actions workflow located in `.github/workflows/schedule.yml`. It is configured to run automatically every day at 8:00 PM Central Time. To enable this, you must add your three environment variables into your GitHub repository's "Secrets and variables" settings. Once the secrets are saved, the cloud environment will manage the daily execution automatically.

## Author
Developed by Alex Rodriguez.
