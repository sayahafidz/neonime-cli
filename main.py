from bs4 import BeautifulSoup
import requests
import subprocess
from zippyshare_downloader import extract_info, extract_info_coro, download

import os

anime_link_list = []
# folder = 'D:\\Downloads\\Video\\'
folder = 'Anime\\'


def show_animes():
    html_text = requests.get('https://neonime.co/').text
    soup = BeautifulSoup(html_text, 'lxml')
    animes = soup.find('div', class_='item_1 items')
    for index, anime in enumerate(animes):
        try:
            anime_link = anime.find('a')
            anime_title = anime.find('span').text
            anime_title_episode = anime.find(
                "h2", {"class": "text-center"}).text
            print(
                f'{index}. {anime_title}{anime_title_episode}')
            anime_link_list.append(anime_link["href"])
        except:
            break


def anime_page(pilihan):
    halaman_anime = requests.get(anime_link_list[pilihan]).text
    sup = BeautifulSoup(halaman_anime, 'lxml')
    cari_download = sup.find('a', string=' Zippyshare')
    file = extract_info(cari_download['href'],
                        download=True, unzip=False, folder=folder)
    print(file)
    # subprocess.run(
    #     f'zippyshare-dl {cari_download["href"]} --folder {folder} ')


def choose_anime():
    print('')
    user_input = input('Masukkan pilihan anda: ')
    if user_input.isdigit() and int(user_input) < len(anime_link_list):
        anime_page(int(user_input))
    else:
        choose_anime()


if __name__ == "__main__":
    show_animes()
    choose_anime()
    print("file ada di " + os.getcwd() + "\\" + folder)
