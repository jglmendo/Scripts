"""
-----------------------------------------------------------|
|REQUIREMENTS:                                             |
|                                                          |
|1 - Python 3x+                                            |
|2 - BeautifulSoup                                         |
|----------------------------------------------------------|
|   HOW TO USE:                                            |
|1 - IN TERMINAL:                                          |      
|2 -  python moviePicker.py                                |
|3 -  Press "y" for another movie pick, or "n" to terminate|
-----------------------------------------------------------|
"""
import random
import requests
from bs4 import BeautifulSoup

#Script searches in 250 Top movies from IMDB

URL = 'http://www.imdb.com/chart/top'

def main():
    response = requests.get(URL)
    soup = BeautifulSoup(response.text, 'html.parser')
    moviePicker = soup.select('td.titleColumn')
    inner_movietags = soup.select('td.titleColumn a')
    ratingtags = soup.select('td.posterColumn span[name=ir]')


    def get_year(movie_tag):
        moviesplit = movie_tag.text.split()
        year = moviesplit[-1]
        return year


    years = [get_year(tag) for tag in moviePicker]
    actors_list =[tag['title'] for tag in inner_movietags]
    titles = [tag.text for tag in inner_movietags]
    ratings = [float(tag['data-value']) for tag in ratingtags]
    n_movies = len(titles)


    while(True):
        idx = random.randrange(0, n_movies)
        print(f'{titles[idx]} {years[idx]}, Rating: {ratings[idx]:.1f}, Starring: {actors_list[idx]}')
        user_input = input('Do you want another movie (y/n) ')
        if user_input != 'y':
            break


if __name__ == '__main__':
    main()