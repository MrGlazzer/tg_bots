import os
import logging


if not os.path.isdir("logs"):
    os.mkdir("logs")

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='logs/sample.log',
    level=logging.INFO
)
