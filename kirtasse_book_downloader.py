#!/usr/bin/python3
from bs4 import BeautifulSoup
import subprocess


def open_bookslist(path="/home/ihfazh/.kirtasse/data/bookslist.xml"):
    with open(path, 'rb') as bookslist_file:
        return bookslist_file.read()

def get_all_links(bookslist_object):
    soup = BeautifulSoup(bookslist_object)
    all_links = [x['id'] for x in soup.select("bk")]
    return all_links

def download(all_links, path_to="."):
    for link in all_links:
        print("downloading %s" %link)
        subprocess.Popen(['wget', '-c', '-P', path_to, link])


if __name__ == '__main__':
    bookslist_object = open_bookslist()
    all_links = get_all_links(bookslist_object)
    download(all_links, path_to="/home/ihfazh/Public")
