from __future__ import unicode_literals
import youtube_dl

def getInfo(link):
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s.%(ext)s','quiet':True})

    with ydl:
        result = ydl.extract_info(
            link,
            download=False         
        )
     
        return result

def getAudioLink(info):
    for tmp in info["formats"]:
        if "audio only" in tmp["format"]:
            return tmp["url"]

def getM4aLink(info):
    for tmp in info["formats"]:
        if "audio only" in tmp["format"]:
            if("m4a" in tmp["ext"]):
                return tmp["url"]

    return ""


def getExtension(info,url):
    for tmp in info["formats"]:
        if url in tmp["url"]:
            return tmp["ext"]


def getTitle(info):
    return info["title"]

def outputTitles(info):
    for entry in info["entries"]:
        print(entry["title"])

def getLinks(info):
    tmp = []
    for entry in info["entries"]:
        tmp.append(entry["webpage_url"])
    
    return tmp

def downloadMp3(link):
    op = {
        'format':'bestaudio/best',
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        }],        
        'quiet':True
    }
    with youtube_dl.YoutubeDL(op) as ydl:
        ydl.download([link])

def downloadMp4(link):
    op = {
        'postprocessors': [{
        'key': 'FFmpegVideoConvertor',
        'preferedformat': 'mp4',
        }],        
        'quiet':True
    }

    with youtube_dl.YoutubeDL(op) as ydl:
        ydl.download([link])

