from lxml import html
import requests


def kinopolis(day, cinema):
    """Takes a day and a cinema code to scrape the showings from the kinopolis site.

        day is a number of days since start of the cinema week, starting at 1 (1 -> Thursday, 2 -> Friday and so on)
        the cinema code is the same as on the website e.g. cd for citydome, rx for rex and kp for Kinopolis Darmstadt """

    page = requests.get('http://www.kinopolis.de/' + cinema + '/showtimes/week/0.php')
    tree = html.fromstring(page.text)

    results = tree.xpath('//div[@class="movieResultItem"]')

    movies = []

    for result in results:
        movie = {}

        movie['showing'] = result.xpath('ul/li/div[2]/table/tr[2]/td['+ str(day) +']//div/a/text()')
        movie['title'] = result.xpath('div[1]/h3/a/text()')
        
        if not (movie['showing'] == []):
            movies.append(movie)

    return movies
