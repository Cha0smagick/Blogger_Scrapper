import requests
from bs4 import BeautifulSoup
import pandas as pd

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

# Create a list to store the data
data = []

# Extract and store the information from each entry
for i in range(min(num_entries, len(titles))):
    title = titles[i]
    date = dates[i].text.strip() if i < len(dates) else "Unknown Date"
    link = links[i].find('a')['href']

    entry_data = {
        'Title': title.text,
        'Publication Date': date,
        'URL': link
    }

    # Make a request to the entry URL
    entry_response = requests.get(link)
    entry_soup = BeautifulSoup(entry_response.text, "html.parser")

    # Find and store the content of the entry
    entry_content = entry_soup.find(class_="entry-content")
    if entry_content:
        entry_data['Content'] = entry_content.text.strip()

    data.append(entry_data)

    print("\nTitle:", title.text, end="")
    print("Publication Date:\n\n", date)
    print("\n\nURL:\n\n", link)
    if 'Content' in entry_data:
        print("\n\nContent:\n")
        print(entry_data['Content'])

    print("\n" + "=" * 50)

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Export the DataFrame to Excel and CSV
df.to_excel('blog_entries.xlsx', index=False)
df.to_csv('blog_entries.csv', index=False)

print("\nData exported to Excel (blog_entries.xlsx) and CSV (blog_entries.csv) files."
