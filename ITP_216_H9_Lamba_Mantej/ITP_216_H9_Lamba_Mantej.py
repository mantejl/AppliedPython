# Name: Mantej Lamba
# USC email: mlamba@usc.edu
# ITP 216, Fall 2022
# Section: 31883R
# Assignment 9
# Description: assignment where we work to web scrape a music website and print out the upcoming concert schedule

# proper imports
import os
from bs4 import BeautifulSoup as bs
import urllib.request
import ssl

# storing the webpage so we don't make many requests to it over and over again
# updating the part of the web request that identifies your browser, OS, and version to the web server to avoid the 403 error
def store_webpage(url, ctx, fn):
    req = urllib.request.Request(
        url,
        data=None,
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) ' 
                          'Chrome/111.0.0.0 Safari/537.36'
        }
    )
    page = urllib.request.urlopen(req, context=ctx)
    soup = bs(page.read(), 'html.parser')
    f = open(fn, 'w')
    print(soup, file=f)
    f.close()

# loading the webpage to read from
def load_webpage(url, ctx):
    page = urllib.request.urlopen(url, context=ctx)
    return bs(page.read(), 'html.parser')

def main():
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    # first website url and file name
    web_url = 'https://theoasisnightclub.com/events/'
    file_name = 'sites/theoasisnightclub.html'
    # Uncomment below line and run ONCE to save file locally
    # store_webpage(web_url, ctx, file_name)
    file_url = 'file:///' + os.path.abspath(file_name)
    soup = load_webpage(file_url, ctx)

    # finding all the names and dates in the html page
    print("Concerts coming up at The Oasis Night Club:")
    names = soup.find_all('div', class_='lead text-uppercase ls2')
    dates = soup.find_all('div', class_ = 'd-flex align-items-center text-sm-set text-extra-light-gray-color ls1')
    finalNames = []
    finalDates = []

    # adding the modified versions of the text for the names and dates to their new lists
    for name in names:
        finalNames.append(name.strong.text)
    for date in dates:
        finalDates.append(date.div.text.strip())

    # zipping the lists and iterating through it to print out the dates and names alternatively
    for date,name in zip(finalDates,finalNames):
        print("\t" + date)
        print("\t  " + name)

    # second website url and file name
    web_url2 = 'https://zydecobirmingham.com/concerts/'
    file_name2 = 'sites/zydecobirmingham.html'
    # Uncomment below line and run ONCE to save file locally
    #store_webpage(web_url2, ctx, file_name2)
    file_url2 = 'file:///' + os.path.abspath(file_name2)
    soup2 = load_webpage(file_url2, ctx)

    # finding all the names and dates in the html page
    print("Concerts coming up at Zydeco Birmingham:")
    names = soup2.find_all('div', class_='tw-name')
    dates = soup2.find_all('span', class_='tw-event-date')
    finalNames2 = []
    finalDates2 = []

    # adding the modified versions of the text for the names and dates to their new lists
    for name in names:
        finalNames2.append(name.text.strip())
    for date in dates:
        finalDates2.append(date.text.strip())

    # zipping the lists and iterating through it to print out the dates and names alternatively
    for date, name in zip(finalDates2,finalNames2):
        print("\t" + date)
        print("\t  " + name)

if __name__ == '__main__':
    main()

