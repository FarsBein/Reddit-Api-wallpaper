import praw
import urllib.request
import ctypes
import os
import random


client_id = "caI0Zbw5XXBjkQ"
client_secret = "Bes-8tYR7lJwKUtVipJdOPldU7Q"
user_agent = "python_wallpaper"
username = "1st-reddit-lord"
password = "hbvvbh147"

url=''
imageName =''
filePath='C:\\Users\\User\\dev\\pythonWallpaper\\images\\'
imageDirectory=''

##########################################

def redditObj():
    reddit = praw.Reddit(client_id='caI0Zbw5XXBjkQ',
                        client_secret='Bes-8tYR7lJwKUtVipJdOPldU7Q', 
                        user_agent='python_wallpaper',
                        username='1st-reddit-lord',
                        password='hbvvbh147')
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