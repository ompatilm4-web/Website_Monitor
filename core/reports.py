import pandas as pd 
import sqlite3 as sq

def making_report ():
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
    return Data_frame
    
def report():
    Data = making_report()
    Data.to_csv(
        "reports/uptime_report.csv",
        index=False
    )

    print("Report Generated Successfully!")
   