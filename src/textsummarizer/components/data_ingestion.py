import os 
import urllib.request as request
import zipfile

from textsummarizer.logging import logger
from textsummarizer.utils.common import get_size

from textsummarizer.entity import DataIngestionConfig
from pathlib import Path


class DataIngestion:
    def __init__(self,config:DataIngestionConfig) -> None:
        self.config = config

    

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename , headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} downloaded! with the following info : \n{headers}")
        
        else:
            logger.info(f"File already exists of size :{get_size(Path(self.config.local_data_file))}")
    

    def extract_zip_file(self):

        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok= True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
              
        
