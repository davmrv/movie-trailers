"""Movies module."""


class Movie():
    """Base class to instantiate movies objects to create the movie trailers site.

    arguments (title, plot, poster_image_url, trailer_youtube_url).

    """

    def __init__(self, title, plot, poster_image_url, trailer_youtube_url):
        """Movie __init__."""
        self.title = title
        self.plot = plot
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
