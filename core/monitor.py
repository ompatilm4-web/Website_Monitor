import requests
import time
import sqlite3 as sq

from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from core import logger_config


def Fetch_data(Url):

    website_name = Url.split("//")[1]
    response_time = None
    status = "DOWN"

    try:

        # Start Timer
        start = time.time()

        # Fetch Website
        response = requests.get(Url, timeout=3)
        # Parse HTML
        Soup = BeautifulSoup(response.content, 'html.parser')
        # End Timer
        End_time = time.time()

        # Calculate Response Time
        response_time = End_time - start

        # Website Status - based on the actual HTTP response code
        status = "UP" if response.status_code == 200 else "DOWN"

        logger_config.Logger.info(f"Fetched {website_name} successfully ! Status: {status}")

        print(f"Fetched {website_name}")

    except Exception as e:

        # Site could not be reached at all - still record it as DOWN instead of dropping it
        logger_config.Logger.error(f"Failed to fetch {website_name} : {e}")
        print(f"Error : {e}")

    # Connect Database
    connection = sq.connect('data/websites.db')
    cursor = connection.cursor()
    # Insert Data (whether the check succeeded or failed)
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


def monitor():
    with ThreadPoolExecutor(max_workers=10) as TPE:
        # force the map to execute now (it's lazy otherwise) so all
        # websites are checked and stored before we read them back
        list(TPE.map(Fetch_data, Urls))

    # Read back the freshly-checked results so the /monitor page has data to show
    connection = sq.connect('data/websites.db')
    cursor = connection.cursor()
    rows = cursor.execute(
        "SELECT WEBSITE_NAME, STATUS FROM WEBSITES_DATA"
    ).fetchall()
    connection.close()

    websites = [{"name": name, "status": status} for name, status in rows]
    return websites