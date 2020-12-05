import requests
from bs4 import BeautifulSoup
import re

LYRIC_WEBSITE = "https://www.lyricsmania.com"
LYRIC_WEBSITE_SEARCH = "https://www.lyricsmania.com/search.php?"


def search_songs(song_name):
    params = {"k": song_name, "x": "0", "y": "0"}

    # Gets the list of songs from the lyric website
    res = requests.get(LYRIC_WEBSITE_SEARCH, params=params)
    soup = BeautifulSoup(res.text, "html.parser")

    # Find the links of the songs
    ul = soup.find("ul", attrs={"class": "search"})
    lis = ul.find_all("li")
    as_ = [li.find("a") for li in lis]


    # # Goes to the actual song
    selected_song = as_[0].attrs["href"]
    song_url = LYRIC_WEBSITE + selected_song
    res_song = requests.get(song_url)

    soup_song = BeautifulSoup(res_song.text, "html.parser")
    song_body = soup_song.find("div", attrs={"class": "lyrics-body"})

    # Gets the content
    content = song_body.text

    print(content)



search_songs(input("song: "))
