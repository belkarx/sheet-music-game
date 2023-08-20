from selenium import webdriver
import urllib.parse
from bs4 import BeautifulSoup
from lxml import etree

driver = webdriver.Firefox()

names = open("names", "r").read().split("\n")

#gets sheet music links if they exist by name

with open("sheet_music_links", "w+") as f:
    for name in names:
        search_name = urllib.parse.quote(' '.join(name.split('|||')))
        #print(search_name)
        driver.get(f"https://musescore.com/sheetmusic?text={search_name}")
        soup = BeautifulSoup(driver.page_source, 'lxml')

        dom = etree.HTML(str(soup))

        try:
            heading = dom.xpath('/html/body/div[1]/div[1]/section/section/main/div[2]/section/article[1]/div[1]/div[2]/a')[0]

            link = heading.values()[1]
            h = heading[0]

            found_name = ''.join(h.itertext())
            if name.split("|||")[0].lower() in found_name.lower():
                #print(name.split("|||")[0])
                #print(name.split("|||")[1])
                #print(found_name)
                #print(link)
                #print()
                g = name.split('|||')[0] + f"|||{link}\n"
                print(g)
                print()
                f.write(g)
            else:
                print("NAME NOT FOUND")
                print(name.split("|||")[0])
                print()
        except Exception as e:
            print("ERROR | " + name.split("|||")[0])
            print()

driver.quit()
