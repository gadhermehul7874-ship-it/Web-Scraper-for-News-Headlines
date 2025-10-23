News Headline Web Scraper
Overview
This Python script scrapes top news headlines from The Times of India website (https://timesofindia.indiatimes.com/) and saves them to a text file. It uses the requests library to fetch the webpage and BeautifulSoup to parse and extract headlines from HTML <h2> tags. The output is a timestamped .txt file containing numbered headlines.
Features

Fetches HTML content from a specified news website.
Extracts headlines using customizable HTML selectors.
Saves headlines to a text file with a unique timestamped filename.
Includes a User-Agent header to avoid being blocked by websites.

Prerequisites

Python 3.x: Ensure Python is installed on your system.
Required Libraries:
requests: For making HTTP requests.
beautifulsoup4: For parsing HTML content.


Install the required libraries using pip:pip install requests beautifulsoup4



Setup

Clone or download this repository to your local machine.
Ensure Python 3.x is installed. Verify by running:python --version


Install the required dependencies:pip install requests beautifulsoup4



Usage

Navigate to the project directory containing news_scraper.py.
Run the script:python news_scraper.py


The script will:
Fetch headlines from The Times of India homepage.
Save the headlines to a file named headlines_YYYYMMDD_HHMMSS.txt (e.g., headlines_20251023_110312.txt).
Print a confirmation message indicating the output file's name.



Output
The output is a text file containing numbered headlines, e.g.:
1. Headline One
2. Headline Two
3. Headline Three

Customization

Target Website: Modify the url variable in news_scraper.py to scrape a different news website.
HTML Selector: Adjust the soup.find_all("h2") line to match the website’s HTML structure. For example:
For The Times of India, headlines might use <span class="w_tle">. Update to:headlines = soup.find_all("span", class_="w_tle")


Inspect the target website’s HTML using browser developer tools (right-click → Inspect) to identify the correct tag or class.


Output Format: Modify the file-writing logic to change the format of the output file (e.g., JSON or CSV).

Notes

Website Structure: The script assumes headlines are in <h2> tags. If the target website uses different tags or classes, update the find_all selector accordingly.
Rate Limiting: Be cautious of website scraping policies. Excessive requests may lead to IP blocking. Consider adding delays (time.sleep()) for frequent scraping.
Error Handling: The script includes basic error handling for HTTP requests. Enhance it with logging or additional checks if needed.

Troubleshooting

No Headlines in Output: Check the website’s HTML structure and update the find_all selector.
HTTP Errors: Ensure the url is correct and the website is accessible. Verify the User-Agent header if blocked.
Unicode Errors: The script uses UTF-8 encoding to handle special characters. Ensure your environment supports UTF-8.

License
This project is for educational purposes and provided as-is. Respect the terms of service of the target website when scraping.
