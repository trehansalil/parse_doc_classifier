import os
import zipfile
import gdown
from parse_doc.constants import *

class GCloudSync:

    def unzip_to_location(self, zip_file_path, extract_location):
        """Unzips a zip file to the specified location.

        Args:
            zip_file_path: The path to the zip file.
            extract_location: The directory where the contents should be extracted.
        """

        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extract_location)    
        
    def sync_folder_to_gcloud(self, URL, ZIP_FILE_PATH, EXTRACT_LOCATION):
        
        gdown.download(URL, ZIP_FILE_PATH)

        self.unzip_to_location(zip_file_path=ZIP_FILE_PATH, extract_location=EXTRACT_LOCATION)

        
    def sync_folder_from_gcloud(self, URL, ZIP_FILE_PATH, EXTRACT_LOCATION):
        
        gdown.download(URL, ZIP_FILE_PATH)

        self.unzip_to_location(zip_file_path=ZIP_FILE_PATH, extract_location=EXTRACT_LOCATION)

        os.system(f'rm -r {ZIP_FILE_PATH}')
