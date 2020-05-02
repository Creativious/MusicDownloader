import os
from os import listdir
from os.path import isfile, join
import pytube
import ffmpeg
from pytube import YouTube
import requests
from bs4 import BeautifulSoup
import time
def getMusic(url):
    starter_time = round(time.time())
    temp_path = "video_to_audio/temp"
    temp_path_videos = "video_to_audio/temp/videos"
    temp_path_audio = "video_to_audio/temp/audio"
    output_path = "video_to_audio/output"
    def playlist_or_not(url):
        check_string = "youtube.com/playlist"
        if check_string in str(url):
            return True
        else:
            return False
    def do_temp_videos_exist(path):
        if not os.path.exists(path):
            os.makedirs(path)
    def do_temp_audio_exist(path):
        if not os.path.exists(path):
            os.makedirs(path)
    def do_temp_path_exist(path):
        if not os.path.exists(path):
            os.makedirs(path)
    def do_temp_paths_exist(path1, path2, path3):
        do_temp_path_exist(path1)
        do_temp_audio_exist(path2)
        do_temp_videos_exist(path3)
    def do_output_exist(path):
        if not os.path.exists(path):
            os.makedirs(path)
    def do_folders_exist(path1, path2, path3, path4):
        do_temp_paths_exist(path1, path2, path3)
        do_output_exist(path4)
    def download_video(url, savepath):
        try:
            yt = YouTube(url)
        except:
            pass
        t = yt.streams.filter().all()
        try:
            t[0].download(savepath)
        except:
            pass
    do_folders_exist(temp_path, temp_path_audio, temp_path_videos, output_path)
    is_playlist = playlist_or_not(url)
    def get_playlist_links(url):
        sourceCode = requests.get(url).text
        soup = BeautifulSoup(sourceCode, 'html.parser')
        domain = 'https://www.youtube.com'
        blinks = []
        for link in soup.find_all("a", {"dir": "ltr"}):
            href = link.get('href')
            if href.startswith('/watch?'):
                blink = (domain + href + '\n')
                blinks.append(blink)
        return blinks
    if is_playlist:
        x = 0
        links = get_playlist_links(url)
        thecount = len(links)
        for link in links:
            x += 1
            try:
                download_video(link, temp_path_videos)
            except:
                pass
    else:
        files = []
        for f in listdir(output_path):
            string = r"" + str(f)
            files.append(string)
        try:
            yt = YouTube(url)
            title = str(yt.title)
            thingy = title.replace(r".", "")
            title = thingy
            title += ".mp3"
            thingy = title.replace(r"/", "")
            title = thingy
            thingy = title.replace(r"\"", "")
            print(title)
            print(files)
            if title in files:
                returVal = output_path + "/" + title
                return returVal
            else:
                download_video(url, temp_path_videos)
        except:
            print("FAILURE AT LINE 87")
    video_files = [f for f in listdir(temp_path_videos) if
                   isfile(join(temp_path_videos, f))]
    for video_file in video_files:
        _filename = video_file[:-3]
        video_path = temp_path_videos + "/" + _filename + "mp4"
        audio_path = output_path + "/" + _filename + "mp3"
        os.system(f'ffmpeg -i "{video_path}" "{audio_path}" -y -loglevel quiet')
    for video_file in video_files:
        _filename = video_file[:-3]
        video_path = temp_path_videos + "/" + _filename + "mp4"
        os.remove(video_path)
    video_file = video_files[0]
    _filename = video_file[:-3]
    audio_path = output_path + "/" + _filename + "mp3"
    return audio_path