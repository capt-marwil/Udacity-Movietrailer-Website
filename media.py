class Digital_asset(object):
    """ A general class to represent digital assets such as Movies, TV-shows, Games etc."""

    def __init__(self, title, synopsis, poster_image_url, trailer_youtube_url):
        self.title = title
        self.synopsis = synopsis
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url


class Movie(Digital_asset):
    """A class to store and display information on movies inherits from Digital_asset"""

    def __init__(self, title, synopsis, movie_storyline, poster_image_url, trailer_youtube_url, director, cast):
        Digital_asset.__init__(self, title, synopsis, poster_image_url, trailer_youtube_url)
        self.movie_storyline = movie_storyline
        self.director = director
        self.cast = cast.split(',')

    def get_cast(self):
        cast = ""
        for i in self.cast:
            cast = cast + i + "<br>"
        return cast


class TvShow(Digital_asset):
    """A class to store and display information on tv shows inherits from Digital_asset"""

    def __init__(self, title, synopsis, tv_station, poster_image_url, trailer_youtube_url, cast):
        Digital_asset.__init__(self, title, synopsis, poster_image_url, trailer_youtube_url)
        self.tv_station = tv_station
        self.cast = cast.split(',')

    def get_cast(self):
        cast = ""
        for i in self.cast:
            cast = cast + i + "<br>"
        return cast


class Game(Digital_asset):
    """A class to store and display information on tv shows inherits from Digital_asset"""
    def __init__(self, title, synopsis, poster_image_url, trailer_youtube_url, platform):
        Digital_asset.__init__(self, title, synopsis, poster_image_url, trailer_youtube_url)
        self.platform = platform.split(',')

    def get_platform(self):
        platform = ""
        for i in self.platform:
            platform = platform + i + "<br>"
        return platform
