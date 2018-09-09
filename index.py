from lxml import html
import urllib.request
import requests
import re
import imageio
from os import listdir

#save all images
def saveAllImages():
    links = getLinkNames()
    saveImagesFromLinks(links)

#save only images not already saved
def saveLatestImages():
    links = getLinkNames()
    pics = getCurrentSavedImages()
    #get the latest saved pic name removing file extension
    lastSavedPic = (pics[len(pics)-1:])[0][:-4]
    links = links[:(links.index(lastSavedPic))]
    saveImagesFromLinks(links)

#get the list of links from NOAA   
def getLinkNames():
    page = requests.get('https://www.nhc.noaa.gov/archive/xgtwo/gtwo_archive_list.php?basin=atl')
    tree = html.fromstring(page.content)

    #go to <pre> get all children <a> get text of those tags
    links = tree.xpath('//pre/a/text()')

    #remove first link
    del links[0]
    links = removeDateTimeFormat(links)
    return links

#save the images from the provided links
def saveImagesFromLinks( links ):
    #for each link get the image
    for link in links:
        print(link)
        urllib.request.urlretrieve("https://www.nhc.noaa.gov/archive/xgtwo/atl/"+link+"/two_atl_2d0.png", "pics/"+link+".jpg")

#get the images already saved
def getCurrentSavedImages():
    pics = listdir('pics/')
    return pics

#remove the date time format: 2018-09-08 12:30 -> 201809081230
def removeDateTimeFormat(links):
    unformatedLinks = []
    for link in links:
        link = re.sub("([- :])","", link)
        unformatedLinks.append(link)
    return unformatedLinks

saveLatestImages()