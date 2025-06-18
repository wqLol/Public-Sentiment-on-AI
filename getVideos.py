# REFERENCE - GOOGLE API DOCS
import os
import googleapiclient.discovery
from apikey import key

scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"



def getVideo(query):
    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=key)

    request = youtube.search().list(
        part="snippet",
        maxResults=25,
        q="surfing"
    )
    response = request.execute()

    print(response)
