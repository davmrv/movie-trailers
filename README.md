# movie-trailers
Movie trailers project for udacity nanodegree

# Usage

First, you need to declare the movies on the **index_movies.py** file using the `Movie()` class or importing the `movies` module to a file you want to use.

> Example to add a movie to the site:
>> `resident_evil_1 = movies.Movie(
    'Resident Evil',
    '''Underneath Raccoon City exists a genetic research facility called the Hive,
    owned by the Umbrella Corporation. A thief steals the genetically
    engineered T-virus and contaminates the Hive with it. In response, the
    facility\'s artificial intelligence, the Red Queen, seals the Hive and
    kills everyone inside.''',
    'http://static.tvtropes.org/pmwiki/pub/images/683290_413.jpg',
    'https://www.youtube.com/watch?v=u6uDnd_v5Bw')`
    
You can pass the **title**, **plot**. **poster url** and **youtube trailer url** to the class (`Movie(title, plot, poster_image_url, youtube_trailer_url)`)

Then, you need to add the movie to the `movies` list.

>Example:
>>`movies = [resident_evil_1, movie_2, movie_3... movie_n]`

Now, after you added a new movie or created another file using the **movies** module, you need to run the script you created or the `index_movies.py` script to create an HTML file.
