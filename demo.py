from parse_doc.configuration.gcloud_syncer import GCloudSync
from parse_doc.constants import *
from parse_doc.pipeline import mkdir


mkdir(ARTIFACTS_DIR=DATA_INGESTION_ARTIFACTS_DIR)

obj = GCloudSync()
obj.sync_folder_from_gcloud(
    URL=GDRIVE_URL, 
    ZIP_FILE_PATH=ZIP_FILE_EXPORT_DIR, 
    EXTRACT_LOCATION=DATA_INGESTION_ARTIFACTS_DIR
)