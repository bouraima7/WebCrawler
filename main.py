import requests
from bs4 import BeautifulSoup

# Define the URL to scrape
url = "https://nba.com"

# Define the words to search for
words_to_search = ["Embiid", "James", "Curry"]

# Fetch the HTML content of the URL
response = requests.get(url)
html_content = response.content

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find all the text on the page
all_text = soup.get_text()

# Count the occurrences of each word
word_counts = {}
for word in words_to_search:
    count = all_text.count(word)
    word_counts[word] = count

# Print the results
for word, count in word_counts.items():
    print(f"{word}: {count} occurrences")
