import praw
import urllib.request
import ctypes
import os
import random

url=''
imageName =''
filePath= os.path.abspath(os.getcwd()) + '\\images\\'
imageDirectory=''


##########################################

def redditObj():
    reddit = praw.Reddit(client_id=os.environ.get('client_id'),
                        client_secret=os.environ.get('client_secret'), 
                        user_agent=os.environ.get('user_agent'),
                        username=os.environ.get('reddit_username'),
                        password=os.environ.get('reddit_password'))
    return reddit

def downloadImage(url,filePath,fileName):
    urllib.request.urlretrieve(url,filePath+fileName)
    return filePath+fileName

def changeWallpaper(imageDirectory):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, imageDirectory , 0)
    print('Background has changed...')

def cleanFolder(directory):
    files = os.listdir(directory)
    for i in range(len(files)):
        os.remove(directory+files[i])


##########################################
subredditsList = ['wallpaper','wallpapers']
reddit =redditObj()

subreddit = reddit.subreddit(subredditsList[random.randrange(2)])

hotSubreddit = subreddit.hot(limit=1)

for i in hotSubreddit:
    if not i.is_self: #if a post has a link
        url=i.url
        imageName=str(i.author) +url[-4:]

if (imageName != url): #if not empty
    cleanFolder(filePath)
    imageDirectory = downloadImage(url,filePath,imageName)
    changeWallpaper(imageDirectory)