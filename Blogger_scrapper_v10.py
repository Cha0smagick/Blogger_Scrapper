import requests
from bs4 import BeautifulSoup

# Ask for the URL of the blog
url = input("Please enter the URL of the blog: ")

# Ask for the number of entries to review
num_entries = int(input("Please enter the number of entries to review: "))

# Print the URL of the blog
print("The URL of the blog is:", url)

# Make a request to the website
response = requests.get(url)

# Parse the HTML of the website
soup = BeautifulSoup(response.text, "html.parser")

# Find all the elements with the appropriate class or tag for both platforms
if "blogspot.com" in url:
    titles = soup.find_all(class_="post-title")
    dates = soup.find_all(class_="date-header")
    links = soup.find_all(class_="post-title")
elif "wordpress.com" in url:
    titles = soup.find_all(class_="entry-title")
    dates = soup.find_all("time", class_="entry-date published")
    links = soup.find_all(class_="entry-title")
else:
    print("Unsupported URL format.")
    exit()

# Extract and print the information from each entry
for i in range(min(num_entries, len(titles))):
    title = titles[i]
    date = dates[i].text.strip() if i < len(dates) else "Unknown Date"
    link = links[i].find('a')['href']

    print("Title:", title.text)
    print("Publication Date:", date)
    print("URL:", link)
    print()

    # Make a request to the entry URL
    entry_response = requests.get(link)
    entry_soup = BeautifulSoup(entry_response.text, "html.parser")

    # Find and print the content of the entry
    entry_content = entry_soup.find(class_="entry-content")
    if entry_content:
        print("Content:")
        print(entry_content.text.strip())
        print()
    else:
        print("No content found for this entry.")
        print()
