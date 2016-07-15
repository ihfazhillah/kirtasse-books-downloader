## Kirtasse (ALL) Books Downloader

Mengunduh semua buku (kutub) untuk aplikasi [elkirtasse](http://elkirtasse.sourceforge.com) menjadi mudah.

### Installasi
Tidak butuh installasi, tinggal jalankan file dengan beberapa perubahan

di paling bawah:
```python3
  bookslist_object = open_bookslist("/home/ihfazh/.kirtasse/data")
  all_links = get_all_links(bookslist_object)
  download_all(all_links, path_to="/home/ihfazh/Public")
```

ubah parameter dari fungsi `open_bookslist` dengan path dimana bookslist.xml berada. Secara default, dia beralamat di `~/.kirtasse/data/bookslist.xml`

juga ubah parameter dari fungsi `download_all` untuk `path_to` dengan folder kamu ingin simpan.

### Requirements
*  `bs4`
* `requests`
