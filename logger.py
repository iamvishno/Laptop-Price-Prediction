import logging
import os



from datetime import datetime

current_date = f"{datetime.now().date()}"

log_files = os.path.join(os.getcwd(),'Logs',current_date)
os.makedirs(log_files,exist_ok=True)
log_file_path = os.path.join(log_files,'log')
logging.basicConfig(
    filename=log_file_path,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logging.info('Hello This is First Logging')
logging.info('2nd logging')