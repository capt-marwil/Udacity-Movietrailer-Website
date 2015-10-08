__author__ = 'marwil'
import webbrowser



class Digital_asset(object):
    """ A general class to represent Digital assets such as Movies, TV-shows, Books, Games etc.
    """
    def __init__(self, title, synopsis, rating):
        self.title = title
        self.synopsis = synopsis
        self.rating = rating


class Movie(Digital_asset):
    """A class to store and display information on movies"""

    def __init__(self, title, synopsis, rating, movie_storyline, poster_image_url, trailer_youtube_url, director, cast):
        Digital_asset.__init__(self, title, synopsis, rating)
        self.movie_storyline = movie_storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.director = director
        self.cast = cast

    def get_title(self):
        return self.title

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def show_poster(self):
        webbrowser.open(self.poster_image)


class TvShow(Digital_asset):

    def __init__(self, title, synopsis, rating, tv_station):
        Digital_asset.__init__(title, synopsis, rating)
        self.tv_station = tv_station




class Game(Digital_asset):

    def __init__(self, title, synopsis, rating, platform):
        Digital_asset.__init__(self, title, synopsis, rating)
        self.platform = platform