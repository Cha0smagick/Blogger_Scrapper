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
    dates = soup.find_all(class_="datePublished")
    links = soup.find_all(class_="post-title")
elif "wordpress.com" in url:
    titles = soup.find_all(class_="entry-title")
    dates = soup.find_all("time", class_="entry-date published")
    links = soup.find_all(class_="entry-title")
else:
    print("Unsupported URL format.")
    exit()

# Extract the text, URL, and date from each entry and print them
for i in range(min(num_entries, len(titles))):
    title = titles[i]
    date = dates[i].text.strip() if dates else "Unknown Date"
    link = links[i].find('a')['href']
    print(title.text)
    print("Publication Date:", date)
    print("URL:", link)
    print()
