import os
import dropbox
from dropbox import files
from dotenv import load_dotenv

# load .env
load_dotenv()
app_key = os.environ.get("app_key")
app_secret = os.environ.get("app_secret")
oauth2_refresh_token = os.environ.get("oauth2_refresh_token")


dbx = dropbox.Dropbox(
                      app_key=app_key,
                      app_secret=app_secret,
                      oauth2_refresh_token=oauth2_refresh_token
                      )
# dbx.check_and_refresh_access_token()
path = os.getcwd()


def update_password():
    try:
        for entry in dbx.files_list_folder('/passwords').entries:
            dbx.files_download_to_file(path+"\\"+entry.name, "/passwords/"+entry.name)
            print(f"The {entry.name} has been updated")
    except Exception as e:
        print(e)
        print("Updating process goes wrong")


def upload_password():
    print("Sending data to the cloud")
    try:
        binary_file = open("password.json", mode="rb")
        dbx.files_upload(binary_file.read(), "/passwords/password.json", mode=files.WriteMode.overwrite)
        print("Sending is successful")
    except Exception as e:
        print("Sending process goes wrong")
        print(e)

