import requests
import time
import sqlite3 as sq

from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from core import logger_config


def Fetch_data(Url):

    try:

        # Start Timer
        start = time.time()
        
        # Fetch Website
        response = requests.get(Url)
        # Parse HTML
        Soup = BeautifulSoup(response.content, 'html.parser')
        # End Timer
        End_time = time.time()
        
        # Calculate Response Time
        response_time = End_time - start

        # Website Status
        status = "UP"
        # Website Name
        website_name = Url.split("//")[1]
        
        logger_config.Logger.info("Websites are Fetched Successfully !")
        
        print(f"Fetched {website_name}")
        
        # Connect Database
        connection = sq.connect('data/websites.db')
        cursor = connection.cursor()
        # Insert Data
        cursor.execute('''

        INSERT OR REPLACE INTO WEBSITES_DATA
        (WEBSITE_NAME, WEBSITE_URL, RESPONSE_TIME, STATUS)

        VALUES (?, ?, ?, ?)

        ''', (

            website_name,
            Url,
            response_time,
            status

        ))

        # Save Changes
        connection.commit()
        logger_config.Logger.info("Fetched Websites are stored in the Db file  Successfully !")

        # Close Database
        connection.close()

    except Exception as e:

        print(f"Error : {e}")
    
Urls=[
    "https://www.google.com",
    "https://www.youtube.com",
    "https://www.github.com",
    "https://www.openai.com",
    "https://www.wikipedia.org",

    "https://www.amazon.in",
    "https://www.flipkart.com",
    "https://www.microsoft.com",
    "https://www.apple.com",
    "https://www.netflix.com",

    "https://www.reddit.com",
    "https://www.linkedin.com",
    "https://www.instagram.com",
    "https://www.facebook.com",
    "https://www.twitter.com",

    "https://www.stackoverflow.com",
    "https://www.python.org",
    "https://www.djangoproject.com",
    "https://pandas.pydata.org",
    "https://numpy.org",

    "https://www.ibm.com",
    "https://www.oracle.com",
    "https://www.adobe.com",
    "https://www.spotify.com",
    "https://www.tesla.com"
]
    
    
    
    
def monitor () :
    with ThreadPoolExecutor(max_workers=10) as TPE :
        results= TPE.map(Fetch_data,Urls)
    
    

    

    