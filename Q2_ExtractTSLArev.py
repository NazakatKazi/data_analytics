!pip install pandas
!pip install requests
!mamba install bs4
!mamba install html5lib
!pip install lxml
!pip install plotly

import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
data  = requests.get(url).text
print(data)

soup = BeautifulSoup(data, 'html5lib')
tesla_data = pd.DataFrame(columns=["Year", "Revenue"])

for row in soup.find("tbody").find_all('tr'):
    col = row.find_all("td")
    year = col[0].text
    revenue = col[1].text
    
for row in soup.find("tbody").find_all('tr'):
    cols = row.find_all("td")
    for col in cols:
        print(col.text, end=' ')
    print()
