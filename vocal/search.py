import urllib.request
import urllib.parse
import re


def TestThing(anInput):
    query_string = urllib.parse.urlencode({"search_query" : anInput})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    VideoList = []
    for search_result in search_results:
        finalParse = "http://www.youtube.com/watch?v=" + search_result
        VideoList.append(finalParse)
    return VideoList