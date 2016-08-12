"""Info for trailers site."""


import movies
import site_compile

# Create "Movie" instance for Resident Evil Movie
resident_evil_1 = movies.Movie(
    'Resident Evil',
    '''Underneath Raccoon City exists a genetic research facility called the Hive,
    owned by the Umbrella Corporation. A thief steals the genetically
    engineered T-virus and contaminates the Hive with it. In response, the
    facility\'s artificial intelligence, the Red Queen, seals the Hive and
    kills everyone inside.''',
    'http://static.tvtropes.org/pmwiki/pub/images/683290_413.jpg',
    'https://www.youtube.com/watch?v=u6uDnd_v5Bw')

# Create "Movie" instance for Silent Hill Movie
silent_hill_1 = movies.Movie(
    'Silent Hill',
    '''Rose and her husband, Christopher Da Silva, are concerned about their
    adopted daughter, 9-year old Sharon, who has been sleepwalking while
    calling the name of a town, "Silent Hill". Desperate for answers, Rose
    takes Sharon to Silent Hill. As they approach the town, she is pursued by
    police officer Cybil Bennett, who has become suspicious of Rose\'s motives
    after witnessing Sharon panic at a gas station when her drawings are
    mysteriously vandalized. A mysterious child appears in the road, causing
    Rose to swerve and crash the car, knocking herself unconscious. When she
    awakens, Sharon is missing, while fog and falling ash blanket the town.''',
    'http://www.impawards.com/2006/posters/silent_hill_xlg.jpg',
    'https://www.youtube.com/watch?v=WWMGZe6iucw')

# Create "Movie" instance for Sweeney Todd
sweeney_todd = movies.Movie(
    'Sweeney Todd',
    '''In 1846, Benjamin Barker, a barber, arrives in London, accompanied by
    sailor Anthony Hope. Fifteen years earlier, he was falsely convicted and
    sentenced to penal transportation by the corrupt Judge Turpin, who lusted
    after Barker\'s wife Lucy. Barker adopts the alias "Sweeney Todd" and
    returns to his old Fleet Street shop, situated above Mrs. Nellie Lovett\'s
    meat pie shop. He learns that Turpin raped Lucy, who then poisoned herself
    with arsenic. The couple\'s daughter, Johanna, is now Turpin\'s ward, and
    is the object of Turpin\'s lust. Todd vows revenge, and re-opens his barber
    shop after Mrs. Lovett returns his straight razors to him. Anthony becomes
    enamored with Johanna, but is caught by Turpin and driven away by his
    corrupt associate, Beadle Bamford.''',
    'https://hannahb93.files.wordpress.com/2010/07/sweeney-todd-poster.jpg',
    'https://www.youtube.com/watch?v=_4R72KROZ20')

# Create "Movie" instance for Interstellar
interstellar = movies.Movie(
    'Interstellar',
    '''In a futuristic 21st-century era, crop blight on Earth has made farming
    increasingly difficult and threatens humanity\'s survival. Joseph Cooper
    (McConaughey), a widowed former NASA pilot, runs a farm with his
    father-in-law, son, and daughter Murphy, who believes her bedroom is
    haunted by a poltergeist. When a pattern is created out of dust on the
    floor, Cooper realizes that gravity is behind its formation, not a "ghost".
    He interprets the pattern as a set of geographic coordinates formed into
    binary code. Cooper and Murphy follow them to a secret NASA facility, where
    they are met by Cooper\'s former professor Dr. Brand (Caine).''',
    'http://i.imgur.com/oLlnH5S.jpg',
    'https://www.youtube.com/watch?v=zSWdZVtXT7E')

# Create "Movie" instance for Transcendence
transcendence = movies.Movie(
    'Transcendence',
    '''Dr. Will Caster (Johnny Depp) is a scientist who researches the nature
    of sentience, including artificial intelligence. He and his team work to
    create a sentient computer; he predicts that such a computer will create a
    technological singularity, or in his words "Transcendence". His wife,
    Evelyn (Rebecca Hall), is also a scientist and helps him with his work.''',
    'http://www.impawards.com/2014/posters/transcendence.jpg',
    'https://www.youtube.com/watch?v=VCTen3-B8GU')

# Create "Movie" instance for The Giver
the_giver = movies.Movie(
    'The Giver',
    '''Following a calamity referred to as The Ruin, society is reorganized
    into a series of communities, and all memories of the past are held by one
    person, the Receiver of Memory. Since the Receiver of Memory is the only
    individual in the community who has the memories from before, he must
    advise the Chief Elder, and the other Elders, on the decisions for the
    community.''',
    'http://www.impawards.com/2014/posters/giver_ver13.jpg',
    'https://www.youtube.com/watch?v=iJNNugNe0Wo')

# Create "Movie" instance for The Martian
the_martian = movies.Movie(
    'The Martian',
    '''In 2035, the crew of the Ares III manned mission to Mars is exploring
    the Acidalia Planitia on Martian solar day (sol) 18 of their 31-sol
    expedition. An unexpectedly strong dust storm threatens to topple their
    Mars Ascent Vehicle (MAV), forcing them to hastily leave the planet. During
    the evacuation, astronaut Mark Watney is struck by debris and lost in the
    storm; the last telemetry from his suit indicates no signs of life. With
    Watney believed dead, mission commander Melissa Lewis orders the remaining
    crew to return to their orbiting vessel Hermes without him.''',
    'http://cdn.traileraddict.com/content/20th-century-fox/martian2015-5.jpg',
    'https://www.youtube.com/watch?v=ej3ioOneTy8')

# Create "Movie" instance for Star Wars: The Force Awakens
the_force_awakens = movies.Movie(
    'Star Wars: The Force Awakens',
    '''Approximately 30 years after the destruction of the second Death
    Star, the last remaining Jedi, Luke Skywalker, has disappeared. The First
    Order has risen from the fallen Galactic Empire and seeks to eliminate the
    New Republic. The Resistance, backed by the Republic and led by Luke\'s
    twin sister, General Leia Organa, opposes them while searching for Luke to
    enlist his aid.''',
    'http://goo.gl/P9wQwp',
    'https://www.youtube.com/watch?v=sGbxmsDFVnE')

"""Create list of movies to use in the open_movies_page function from the
"fresh_tomatoes.py" module (changed to "site_compile.py")
"""

movies = [
        resident_evil_1,
        silent_hill_1,
        sweeney_todd,
        interstellar,
        transcendence,
        the_giver,
        the_martian,
        the_force_awakens
    ]

# "Compile" site into HTML
site_compile.open_movies_page(movies)
