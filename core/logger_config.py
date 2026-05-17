import logging

logging.basicConfig(

    filename='../logs/monitor.log',

    level=logging.INFO,

    format='%(asctime)s - %(levelname)s - %(message)s'
)

Logger = logging.getLogger()