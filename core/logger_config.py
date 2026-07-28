import os
import logging

from core.paths import LOG_DIR, LOG_PATH

os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(

    filename=LOG_PATH,

    level=logging.INFO,

    format='%(asctime)s - %(levelname)s - %(message)s'
)

Logger = logging.getLogger()