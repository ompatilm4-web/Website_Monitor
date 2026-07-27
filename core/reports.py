import os
import pandas as pd
import sqlite3 as sq

def making_report ():
    connection=sq.connect("data/websites.db")
    cursor =connection.cursor ()

    DATA=cursor.execute("SELECT * FROM WEBSITES_DATA ")
    Data=[]

    for data in DATA :
        Data.append(data)

    # Column names match what report.html expects (item.website, item.response_time, item.status)
    Data_frame=pd.DataFrame(Data,
                            columns=[
                                "website",
                                "url",
                                "response_time",
                                "status"])
    return Data_frame

def report():
    Data = making_report()

    os.makedirs("reports", exist_ok=True)
    Data.to_csv(
        "reports/uptime_report.csv",
        index=False
    )

    print("Report Generated Successfully!")

    # Return the records so the Flask route can render them in report.html
    return Data.to_dict(orient="records")