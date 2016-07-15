#!/usr/bin/python3
from bs4 import BeautifulSoup
import subprocess
import requests
import os

def open_bookslist(path="/home/ihfazh/.kirtasse/data/bookslist.xml"):
    with open(path, 'rb') as bookslist_file:
        return bookslist_file.read()

def get_all_links(bookslist_object):
    soup = BeautifulSoup(bookslist_object)
    all_links = [x['id'] for x in soup.select("bk")]
    return all_links

def download(all_links, path_to="."):
    for link in all_links:
        with open(os.path.join(path_to, "log"), "r") as f:
            links_in_log = f.readlines()

        if link not in links_in_log:
            print("downloading %s" %link)
            file_name = link.split("/")[-1]
            resp = requests.get(link, stream=True)
            with open(os.path.join(path_to, file_name), "wb") as f:
                for chunk in resp.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
        # logging
        with open(os.path.join(path_to, "log"), "a") as f:
            f.write(link)



if __name__ == '__main__':
    bookslist_object = open_bookslist()
    all_links = get_all_links(bookslist_object)
    download(all_links, path_to="/home/ihfazh/Public")
