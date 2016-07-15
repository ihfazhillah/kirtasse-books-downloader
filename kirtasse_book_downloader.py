#!/usr/bin/python3
from bs4 import BeautifulSoup
import subprocess
import requests
import os

def open_bookslist(path="/home/ihfazh/.kirtasse/data/bookslist.xml"):
    with open(path, 'rb') as bookslist_file:
        return bookslist_file.read()

def get_all_links(bookslist_object):
    soup = BeautifulSoup(bookslist_object, "lxml")
    all_links = [x['id'] for x in soup.select("bk")]
    return all_links

def download_all(all_links, path_to="."):
    for index, link in enumerate(all_links):
        try:
            with open(os.path.join(path_to, "log"), "r") as f:
                links_in_log = [x.strip() for x in f.readlines()]
        except IOError:
            links_in_log = []

        if link not in links_in_log:
            print("[%s/%s] downloading %s" %(index, len(all_links), link))
            try:
                download(link, path_to=path_to)
            except requests.exceptions.ConnectionError:
                print("mencoba lagi untuk mengunduh....")
                download(link, path_to=path_to)


def download(link, path_to=".", ):
    file_name = link.split("/")[-1]
    try:
        resp = requests.get(link, stream=True, timeout=None)
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



if __name__ == '__main__':
    bookslist_object = open_bookslist()
    all_links = get_all_links(bookslist_object)
    download_all(all_links, path_to="/home/ihfazh/Public")
