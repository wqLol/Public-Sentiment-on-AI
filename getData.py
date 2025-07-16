# REFERENCE - GOOGLE API DOCS
import googleapiclient.discovery


def getVideo(youtube, query, startDate, endDate):

    request = youtube.search().list(
        part="snippet",
        maxResults=25,
        type="video",
        order="viewCount",
        videoDuration="medium",
        relevanceLanguage="en",
        publishedAfter=startDate,
        publishedBefore=endDate,
        q=query
    )
    response = request.execute()

    return response



def getComments(youtube, videoId):

    request = youtube.commentThreads().list(
        part="snippet",
        maxResults=100,
        videoId = videoId
    )
    
    response = request.execute()

    return response


