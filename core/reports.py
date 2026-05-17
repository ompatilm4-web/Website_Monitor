import pandas as pd 
import sqlite3 as sq

connection=sq.connect("data/websites.db")
cursor =connection.cursor ()

DATA=cursor.execute("SELECT * FROM WEBSITES_DATA ")
Data=[]

for data in DATA :
    Data.append(data)
    
Data_frame=pd.DataFrame(Data,
                        columns=[
                            "Website_name",
                            "URLs",
                            "Response Time",
                            'Status'])

Data_frame.to_csv(
    "reports/uptime_report.csv",
    index=False
)