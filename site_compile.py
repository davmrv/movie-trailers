"""Script to transform the movies info into HTML."""

import webbrowser
import os
import re

# Customized module of the fresh_tomatoes module

# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Movie Trailers!</title>
    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <!-- added masonry plugin -->
    <script src="https://unpkg.com/masonry-layout@4.1/dist/masonry.pkgd.min.js"></script>
    <!-- added custom css -->
    <link href="css/main.css" rel="stylesheet">
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        <!-- changed "ready" to "on load" -->
        $(window).on('load', function () {
            <!-- init masonry plugin -->
            $('.main-container').masonry({
                itemSelector: '.movie-tile-container',
                percentPosition: true,
                originLeft: true
            });

            $('.movie-tile-container').hide().first().show("fast", function showNext() {

            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
        <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
        </a>
            <div class="scale-media" id="trailer-video-container">
            </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="main-container container">
      {movie_tiles}
    </div>
    <footer>
        <div class="container">
            Movies trailers &copy;
        </div>
    </footer>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-4 col-lg-4 col-xs-12 movie-tile-container text-center" >
    <div class="movie-tile col-xs-10"
    data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal"
    data-target="#trailer">
        <div class="poster-container">
            <img src="{poster_image_url}">
        </div>
        <div class="movie-title">
            <h2>{movie_title}</h2>
        </div>
        <!-- added plot text -->
        <div class="movie-plot">
            <p>{movie_plot}</p>
        </div>
        <button class="btn btn-primary">Watch Trailer</button>
    </div>
</div>
'''


def create_movie_tiles_content(movies):
    """Create content for movies tiles."""
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (
            youtube_id_match.group(0) if youtube_id_match else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
            movie_plot=movie.plot
        )
    return content


def open_movies_page(movies):
    """Create HTML and open the file on the browser."""
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
