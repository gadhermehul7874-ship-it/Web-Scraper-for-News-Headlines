import requests
from bs4 import BeautifulSoup
import datetime

# Target URL (using The Times of India as an example)
url = "https://timesofindia.indiatimes.com/"

# Set headers to mimic a browser request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

# Fetch the webpage
response = requests.get(url, headers=headers)
response.raise_for_status()  # Check for request errors

# Parse HTML with BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# Find headline elements (The Times of India uses specific classes, adjust for other sites)
headlines = soup.find_all("h2")  # Adjust selector based on website structure

# Extract and clean headline texts
headline_texts = [headline.get_text().strip() for headline in headlines if headline.get_text().strip()]

# Generate timestamp for the output file
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = f"headlines_{timestamp}.txt"

# Save headlines to a text file
with open(output_file, "w", encoding="utf-8") as file:
    for i, headline in enumerate(headline_texts, 1):
        file.write(f"{i}. {headline}\n")

print(f"Headlines saved to {output_file}")
