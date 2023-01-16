import requests
from bs4 import BeautifulSoup

# Ask for the URL of the Blogger blog
url = input("Please enter the URL of the Blogger blog: ")

# Ask for the number of entries to review
num_entries = int(input("Please enter the number of entries to review: "))

# Print the URL of the blog
print("The URL of the blog is: ", url)

# Make a request to the website
response = requests.get(url)

# Parse the HTML or XML of the website
soup = BeautifulSoup(response.text, "html.parser")

# Find all the elements with the class "post-title"
titles = soup.find_all(class_="post-title")

# Extract the text from each element and print it
for title in titles[:num_entries]:
    print(title.text)
    print("URL: ", title.find('a')['href'])