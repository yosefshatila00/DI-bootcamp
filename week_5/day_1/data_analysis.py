import pandas as pd


data={"Name":["Alice","Bob","Charlie","David","Eva"],
      "Age":[24,30,22,35,28],
      "City":["New York","Los Angeles","Chicago","Houston","Phoenix"]}

df=pd.DataFrame(data)
df = pd.read_csv('path/to/your/csvfile.csv')
        