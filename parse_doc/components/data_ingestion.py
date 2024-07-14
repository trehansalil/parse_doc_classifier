import os
import sys
import inspect
from zipfile import ZipFile
from parse_doc.logger import logging
from parse_doc.exception import CustomException
from parse_doc.configuration.gcloud_syncer import GCloudSync
from parse_doc.entity.config_entity import DataIngestionConfig
from parse_doc.entity.artifact_entity import DataIngestionArtifact
from parse_doc.pipeline import mkdir


class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        self.data_ingestion_config = data_ingestion_config
        self.gcloud = GCloudSync()
        mkdir(ARTIFACTS_DIR=self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR)
        
    def get_data_from_gdrive(self) -> None:
        current_function_name = inspect.stack()[0][3]
        logging.info(f"Entered the {current_function_name} method of {self.__class__.__name__} class")        
        try:
            self.gcloud.sync_folder_from_gcloud(
                URL=self.data_ingestion_config.GDRIVE_URL,
                ZIP_FILE_PATH=self.data_ingestion_config.ZIP_FILE_EXPORT_DIR,
                EXTRACT_LOCATION=self.data_ingestion_config.DATA_INGESTION_ARTIFACTS_DIR,
            )

            logging.info(f"Exited the {current_function_name} method of {self.__class__.__name__} class")

        except Exception as e:
            raise CustomException(e, sys) from e

    def initiate_data_ingestion(self) -> DataIngestionArtifact:
        current_function_name = inspect.stack()[0][3]
        logging.info(f"Entered the {current_function_name} method of {self.__class__.__name__} class")

        try:
            self.get_data_from_gdrive()

            data_ingestion_artifact: DataIngestionArtifact = DataIngestionArtifact(
                train_file_path=self.data_ingestion_config.TRAIN_DATA_ARTIFACTS_DIR,
                test_file_path=self.data_ingestion_config.TEST_DATA_ARTIFACTS_DIR,
            )

            logging.info(f"Exited the {current_function_name} method of {self.__class__.__name__} class")

            return data_ingestion_artifact

        except Exception as e:
            raise CustomException(e, sys) from e