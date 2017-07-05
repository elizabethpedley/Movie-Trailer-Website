import webbrowser


class Movie():
    ''' The class Movie() stores information about a particular movie. '''

    def __init__(self, movie_title, movie_storyline,
                 poster_image, trailer_youtube):
        ''' This contructer function take the a movies title, storyline, poster
         image, and trailer video and stores them as instance variables. '''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
