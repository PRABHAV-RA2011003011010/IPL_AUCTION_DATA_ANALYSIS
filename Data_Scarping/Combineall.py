import requests
import pandas as pd
from bs4 import BeautifulSoup

# Define the URL of the page to scrape
url = "https://www.iplt20.com/auction/2014"

# Send an HTTP GET request to the URL
r = requests.get(url)

# Parse the HTML content using BeautifulSoup with 'lxml' parser
soup = BeautifulSoup(r.text, "lxml")

# Find the table using its id attribute
tables = soup.find_all("table", id="t1")
all_rows = []

for table in tables:
 
    if table:
        # Extract the headers from the table
        headers = [th.get_text(strip=True) for th in table.find_all("th")]
        
        # Extract the rows from the table
        rows = []
        for tr in table.find_all("tr")[1:]:  # Skip the header row
            cells = [td.get_text(strip=True) for td in tr.find_all("td")]
            rows.append(cells)
        all_rows.extend(rows)
        
        
    else:
        print("Table not found.")
        
df = pd.DataFrame(all_rows, columns=headers)
df.to_csv('ipl_auction_2014.csv', index=False)
