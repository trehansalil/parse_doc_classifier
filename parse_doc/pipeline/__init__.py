import os


def mkdir(ARTIFACTS_DIR):
    '''Check if the directory exists'''
    if not os.path.exists(ARTIFACTS_DIR):
        # If it doesn't exist, create it
        os.makedirs(ARTIFACTS_DIR)
    else:
        # If it exists, you can print a message or perform other actions
        print('The folder already exists.')