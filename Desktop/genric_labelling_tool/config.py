import time
from oauth2client.service_account import ServiceAccountCredentials

current=int(time.time())
EXPIRATION=str(current+3600)
creds = ServiceAccountCredentials.from_json_keyfile_name('/home/sunpriya/Downloads/eduwaivecommon-01cac388cb6b.json')
client_id = creds.service_account_email
GOOGLE_ACCESS_STORAGE_ID='devsunpriya@eduwaivecommon.iam.gserviceaccount.com'
delimiter='/'
num=10