import requests
import pandas as pd
import os
from bs4 import BeautifulSoup

#Change year
url = "https://www.iplt20.com/auction/2024"

r = requests.get(url)

soup = BeautifulSoup(r.text, "lxml")

tables = soup.find_all("table", id="t1")
i=0

for table in tables:
 
    if table:
        
        headers = [th.get_text(strip=True) for th in table.find_all("th")]
        
        
        rows = []
        for tr in table.find_all("tr")[1:]:  
            cells = [td.get_text(strip=True) for td in tr.find_all("td")]
            rows.append(cells)
        df = pd.DataFrame(rows, columns=headers)
        df['Team'] = i
        filename = f'2024_ipl_auction_table_{i + 1}.csv' # Change year
        
        folder_path = r'C:\Users\prabh\OneDrive\Desktop\IPL_Auction\All_Teams_Yearly_Data\2024_teams_data'  #Change year


        file_path = os.path.join(folder_path, filename)
        
        df.to_csv(file_path, index=False)
        
        
    else:
        print("Table not found.")
        
    i=i+1

