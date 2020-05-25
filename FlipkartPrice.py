import bs4, requests

def getFlipkartPrice(productUrl):
    res = requests.get(productUrl)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('#container > div > div.t-0M7P._3GgMx1._2doH3V > div._3e7xtJ > div._1HmYoV.hCUpcT > div._1HmYoV._35HD7C.col-8-12 > div:nth-child(2) > div > div._3iZgFn > div._2i1QSc > div > div._1vC4OE._3qQ9m1')
    return elems[0].text.strip()

price = getFlipkartPrice('https://www.flipkart.com/automate-boring-stuff-python/p/itmfc37mzsbxfnzh')
print('The price is ' + price)

