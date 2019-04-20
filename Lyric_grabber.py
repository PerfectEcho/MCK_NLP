from bs4 import BeautifulSoup
import requests
import time

if __name__ == "__main__":
    url = "https://www.azlyrics.com/m/machinegunkelly.html"
    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')
    listAlbums = bs.find('div', attrs={"id": "listAlbum"}).find_all('a', href=True)
    with open("MGKlyrics.txt", "w")as mgkWriter:
        for song in listAlbums:
            songURL = song["href"].replace("../", "https://azlyrics.com/")
            response = requests.get(songURL)
            bs = BeautifulSoup(response.text, 'html.parser')
            songLyrics = bs.find('div', attrs={"class": "col-xs-12 col-lg-8 text-center"}).find_all('div')[6].text
            mgkWriter.write(songLyrics + "\n")
            time.sleep(.5)
