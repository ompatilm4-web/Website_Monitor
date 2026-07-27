import os
import logging

os.makedirs('logs', exist_ok=True)

logging.basicConfig(

    filename='logs/monitor.log',

    level=logging.INFO,

    format='%(asctime)s - %(levelname)s - %(message)s'
)

Logger = logging.getLogger()