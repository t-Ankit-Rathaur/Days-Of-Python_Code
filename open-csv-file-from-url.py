# import pandas
import pandas as pd
# request module
import requests
# from IO import StringIO(class)
from io import StringIO
# URL(Uniform Resource locator)
url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0"}
req = requests.get(url, headers=headers)
data = StringIO(req.text)
# read_CSV
pd.read_csv(data)