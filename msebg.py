#!/usr/bin/env python 
#
# Python script for Eric Ligman's Amazin Free Microsoft eBook Giveaway
# https://blogs.msdn.microsoft.com/mssmallbiz/2017/07/11/largest-free-microsoft-ebook-giveaway-im-giving-away-millions-of-free-microsoft-ebooks-again-including-windows-10-office-365-office-2016-power-bi-azure-windows-8-1-office-2013-sharepo/
#
# original link to download list of eBooks
# http://ligman.me/2sZVmcG
#
# link to powershell download script

import requests
import urllib

def download(book):
    text = requests.get(book)

    # get real dowwnload name for file
    filename = text.url

    # take last part of name / 
    filename = filename.rsplit('/',1)[1]

    # convert %20 to spaces and other URL values
    filename = urllib.unquote(filename)

    print('Saving: ' + filename)

    # write file out in chunks to system
    bookfile = open(filename, 'wb')
    for chunk in text.iter_content(100000):
         bookfile.write(chunk)
    bookfile.close()

def main():
    download_list = 'http://ligman.me/2sZVmcG'
    res = requests.get(download_list)
    # convert list to array
    books =  (res.text.splitlines())
    # remove header from array
    books.remove('MSFT eBooks')
    numBooks = len(books)
    print("About to download %d books files!" % (numBooks))
    bookNum = 1
    exceptionNum = 0
    # download books
    for book in books:
        try:
           print("Downloading book %d of %d" % (bookNum, numBooks))
           print("%d exceptions so far." % (exceptionNum))
           bookNum = bookNum + 1
           download(book)
        except TypeError:
           exceptionNum = exceptionNum + 1
           print("Skipping book because TypeError")
        except:
           exceptionNum = exceptionNum + 1
           print("Skipping book because exception")


if  __name__ =='__main__':
    main()


