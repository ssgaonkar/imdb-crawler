import urllib
from bs4 import BeautifulSoup as bs
import webbrowser
import movie_mania

class Movie():
    """Class for movie"""

    def __init__(self,movie_title,movie_storyline,poster_img,trailer_url):
        self.title=movie_title
        self.storyline=movie_storyline
        self.poster_img_url=poster_img
        self.trailer_yt_url=trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer_yt_url)


soup = bs(urllib.urlopen('http://www.imdb.com/movies-coming-soon/?ref_=inth_cs').read(), "html.parser")

tables = soup.find_all('table')[:6]
movies= []
for table in tables:
    img= table.find('img')
    img_src = img.get('src')
    title = img.get('title')
    trailer = table.find_all("a",{ "class" : "title-trailer" })[0]
    trailer_url = trailer.get('data-video')
    storyline = table.find_all("div",{ "class" : "outline" })[0]
    storyline_desc = storyline.get_text()
    movie = Movie(title,storyline_desc,img_src,trailer_url)
    movies.append(movie)

movie_mania.open_movies_page(movies)

