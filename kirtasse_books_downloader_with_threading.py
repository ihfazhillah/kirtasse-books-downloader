#!/usr/bin/python2
from bs4 import BeautifulSoup
import subprocess
import requests
import os
import threading
import random


def open_bookslist(path="/home/ihfazh/.kirtasse/data/bookslist.xml"):
    with open(path, 'rb') as bookslist_file:
        return bookslist_file.read()

def get_all_links(bookslist_object):
    soup = BeautifulSoup(bookslist_object, "lxml")
    all_links = [x['id'] for x in soup.select("bk")]
    return all_links

def download_all(all_links, path_to="."):
    # for index, link in enumerate(all_links):
    #     try:
    #         with open(os.path.join(path_to, "log"), "r") as f:
    #             links_in_log = [x.strip() for x in f.readlines()]
    #     except IOError:
    #         links_in_log = []

        # if link not in links_in_log:
        #     print("[%s/%s] downloading %s" %(index, len(all_links), link))
        #     try:
        #         download(link, path_to=path_to)
        #     except requests.exceptions.ConnectionError:
        #         print("mencoba lagi untuk mengunduh....")
        #         download(link, path_to=path_to)
    links_in_log = []
    while len(links_in_log) < len(all_links):
        try:
            with open(os.path.join(path_to, "log"), "r") as f:
                links_in_log = [x.strip() for x in f.readlines()]
        except IOError:
            links_in_log = []

        link_to_dl = random.choice(all_links)
        if link_to_dl not in links_in_log:
            print("[%s/%s] downloading %s" %(len(links_in_log), len(all_links),
            link_to_dl))
            download(link_to_dl, path_to=path_to)





def download(link, path_to=".", ):
    file_name = link.split("/")[-1]
    try:
        resp = requests.get(link, stream=True)
        total_length = resp.headers.get('content-length')
        dl = 0
        with open(os.path.join(path_to, file_name), "wb") as f:
            for chunk in resp.iter_content(chunk_size=1024):
                if chunk:
                    dl += len(chunk)
                    f.write(chunk)
                    print("downloading %s [%s/%s]" %(
                                            resp.url, dl, total_length))
        # logging
        with open(os.path.join(path_to, "log"), "a") as f:
            f.write("%s\n" %link)
    except requests.exceptions.ConnectionError:
        download(link, path_to)
    except requests.exceptions.TimeOut:
        download(link, path_to)

def main():
    bookslist_object = open_bookslist()
    all_links = get_all_links(bookslist_object)
    download_all(all_links, path_to="/home/ihfazh/Public")



if __name__ == '__main__':
    threads = []
    for x in range(30):
        t = threading.Thread(target=main)
        threads.append(t)
        t.start()
