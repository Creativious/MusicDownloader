import os
from os import listdir
from os.path import isfile, join
import pytube
import ffmpeg
from pytube import YouTube
import requests
from pydub import AudioSegment
from time import sleep
from bs4 import BeautifulSoup
import time
import sys
URL = sys.argv[1]
def convert(aPath):
    Audio = AudioSegment.from_mp3(str(aPath))
    adjust_jump = 8
    segment_length = 200
    _8d = Audio[0]
    pan_limit = []
    limit_left = -100
    for i in range(100):
        if int(limit_left) >= 100:
            break
        pan_limit.append(limit_left)
        limit_left += adjust_jump
    pan_limit.append(100)
    for i in range(0, len(pan_limit)):
        pan_limit[i] = pan_limit[i] / 100
    print(len(pan_limit))
    print(pan_limit)
    sleep(2)
    c = 0
    flag = True
    for i in range(0, len(Audio) - segment_length, segment_length):
        peice = Audio[i:i + segment_length]
        if c == 0 and not flag:
            flag = True
            c = c + 2
        if c == len(pan_limit):
            c = c - 2
            flag = False
        if flag:
            panned = peice.pan(pan_limit[c])
            c += 1
        else:
            panned = peice.pan(pan_limit[c])
            c -= 1
        _8d = _8d + panned
        print(panned)
    print(len(_8d))
    file_name = aPath[:-3] + "_8D.mp3"
    out_f = open(file_name, 'wb')
    _8d.export(out_f, format='mp3')

def getMusic(url):
    starter_time = round(time.time())
    temp_path = "video_to_audio/temp"
    temp_path_videos = "video_to_audio/temp/videos"
    temp_path_audio = "video_to_audio/temp/audio"
    output_path = "video_to_audio/output"
    choice = input("8D-Ify your songs[Y/N] EXPERIMENTAL FEATURE")
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
        download_video(url, temp_path_videos)
    video_files = [f for f in listdir(temp_path_videos) if
                   isfile(join(temp_path_videos, f))]
    for video_file in video_files:
        _filename = video_file[:-3]
        video_path = temp_path_videos + "/" + _filename + "mp4"
        audio_path = output_path + "/" + _filename + "mp3"
        os.system(f'ffmpeg -i "{video_path}" "{audio_path}"')
        if choice.lower() == "y":
            convert(audio_path)
    for video_file in video_files:
        _filename = video_file[:-3]
        video_path = temp_path_videos + "/" + _filename + "mp4"
        os.remove(video_path)
    end_time = round(time.time())
    elapsed_time = end_time-starter_time
    return elapsed_time
output = getMusic(URL)
print(f"Program finished in {str(output)} seconds.")

