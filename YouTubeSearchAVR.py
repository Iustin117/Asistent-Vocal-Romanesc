import urllib.request
import webbrowser

def youtube_play(titlu):
    link = "https://www.youtube.com/results?search_query=" + titlu
    html = urllib.request.urlopen(link)
    b = str(html.read().decode())
    startinglink = b.find("/watch?v=")
    fc = startinglink + 9
    lc = fc + 11
    videoid = str(b)[fc:lc]
    webbrowser.open("https://www.youtube.com/watch?v=" + videoid)
