import os
import pandas as pd
import sqlite3 as sq

from core.paths import DB_PATH, REPORTS_DIR, REPORT_CSV_PATH

def making_report ():
    connection=sq.connect(DB_PATH)
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

    os.makedirs(REPORTS_DIR, exist_ok=True)
    Data.to_csv(
        REPORT_CSV_PATH,
        index=False
    )

    print("Report Generated Successfully!")

    # Return the records so the Flask route can render them in report.html
    return Data.to_dict(orient="records")