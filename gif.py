import imageio
from os import listdir

def partialDataGif(delay = 0.2):
    
    pics = listdir('pics/')
    lastIndex = len(pics) - 51
    pics = pics[lastIndex:]

    with imageio.get_writer('tropics_movie_latest.gif', mode='I', duration=delay) as writer:
        for pic in pics:
            image = imageio.imread('pics/'+pic)
            writer.append_data(image)

def fullHistoricDataGif(delay = 0.2):
    pics = listdir('pics/')
    with imageio.get_writer('tropics_movie.gif', mode='I', duration=delay) as writer:
        for pic in pics:
            image = imageio.imread('pics/'+pic)
            writer.append_data(image)

partialDataGif()