# MusicDownloader
Downloads videos from youtube converts them and then saves them after deleting the videos. The only needed use of WiFi is to communicate to YouTube.

This program was created by Creativious as a small little project to test out.

A quick explanation of how this program works.

1. Download the video to the video_to_audio/temp/videos path
2. Convert that video to audio with FFMPEG
3. Output it to video_to_audio/output

Ways I found how to convert .mp4(Downloading from YouTube gives .mp4) to .mp3(compatible with most devices)

Using a module called moviepy, which converted this test video(https://www.youtube.com/watch?v=H_Q6KwWOCvE) to audio in 11 seconds(The time includes the download time)
But when your downloading a playlist of lets say 100 songs(Which is the limit for the playlist thing) it stacks up fast, which would be 1100 seconds or a bit over 18 minutes.

So the other way was to use FFMPEG which converted it in 5 seconds(The time includes the download time)
With 100 songs it can take 500 seconds or a bit over 8 minutes, though I haven't tested it with 100 songs these are just estimates

Mesage me at Creativious#0874 on discord to ask questions if you feel like it.

Default output path is the video_to_audio/output

Bugs:
When moving files to a new destination it sometimes will name it "Youtube.mp3" I haven't found a fix for it, but it doesn't seem to affect it, if you need a correct name, just don't use the move function.

