# REFERENCE - GOOGLE API DOCS
import googleapiclient.discovery


def getVideo(youtube, query, startDate, endDate):

    request = youtube.search().list(
        part="snippet",
        maxResults=25,
        type="video",
        publishedAfter=startDate,
        publishedBefore=endDate,
        q=query
    )
    response = request.execute()

    return response



def getComments(youtube, videoId):

    request = youtube.comments().list(
        part="snippet",
        maxResults=10,
        parentId = videoId
    )
    
    response = request.execute()

    return response


