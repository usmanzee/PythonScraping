import requests
import csv
import json
from bs4 import BeautifulSoup

f = csv.writer(open('movies.csv', 'w', encoding="utf-8"))
f.writerow(['Movie Name', 'Total Number of Ratings', 'Rating Score', 'Genre', 'Budget', 'Gross USA'])
data = []

root_url = 'https://www.imdb.com/chart/top?ref_=nv_mv_250'
page = requests.get(root_url)
soup = BeautifulSoup(page.text, 'html.parser')

movieTrs = soup.find_all(class_="titleColumn")
for movieTr in movieTrs:
    movieTags = movieTr.find_all("a")

    for movieTag in movieTags:
        movieLink = "https://www.imdb.com/" + movieTag['href']
        movieHtml = requests.get(movieLink)

        movieSoup = BeautifulSoup(movieHtml.text, 'html.parser')

        movieTitleWrapper = movieSoup.find(class_='title_bar_wrapper')
        movieRatingsWrapper = movieSoup.find(class_='ratings_wrapper')

        movieName = movieTitleWrapper.find('h1').text

        ratingScore = movieSoup.find(class_='ratingValue').find('span').text

        totalNumberOfRatings = movieSoup.find(class_='imdbRating').find('a').find('span').text

        genre = movieSoup.find(class_='subtext').find('a').text

        movieDetails = movieSoup.find(id='titleDetails')

        budgetText = movieDetails.find('h4', text='Budget:')

        if budgetText != None:
            budget = budgetText.next_sibling.string
        else:
            budget = 'None'

        grossUSAText = movieDetails.find('h4', text='Gross USA:')

        if grossUSAText != None:
            grossUSA = grossUSAText.next_sibling.string
        else:
            grossUSA = 'None'

        budget = budget.strip()
        grossUSA = grossUSA.strip()

        item = {}
        item['Movie Name'] = movieName
        item['Total Number of Ratings'] = totalNumberOfRatings
        item['Rating Score'] = ratingScore
        item['Genre'] = genre
        item['Budget'] = budget
        item['Gross USA'] = grossUSA

        print(item)
        data.append(item)

        f.writerow([movieName, totalNumberOfRatings, ratingScore, genre, budget, grossUSA])
        with open("Movies.json", "w", encoding="utf-8") as writeJSON:
            json.dump(data, writeJSON, ensure_ascii=False)
