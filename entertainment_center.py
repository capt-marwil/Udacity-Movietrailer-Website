import media
import fresh_tomatoes

# Create Instances of class media.Movie
wild_at_heart = media.Movie("Wild at Heart",  "An impossible Love", 1, "The story of Lula and Sailor", "img/wild_at_heart.jpg", "https://www.youtube.com/watch?v=QCQwumNQL9E", "David Lynch", "Nicolas Cage, Laura Dern")


down_by_law = media.Movie("Down by Law",  "The convicts try to escape from prison", 2, "I Scream, you scream, we all scream for icecream", "img/down_by_law.jpg", "www.youtube.com/watch?v=1H9zlFH7UhA", "Jim Jarmusch", "Roberto Benigni, John Lurie, Tom Waits")

night_on_earth = media.Movie("Night on Earth", "A collection of five stories involving cab drivers in five different cities.", 15, "Helmet,that\'s not a name", "img/night_on_earth.jpg", "https://www.youtube.com/watch?v=F1m6GlPyOSU", "Jim Jarmush", "Roberto Bengini, Armin Müller-Stahl, Joe Strummer")

# Create Instances of TV Shows (title, synopsis, rating, tv_station, poster_image_url, trailer_youtube_url, cast):

sopranos = media.TvShow("The Sopranos", "New Jersey mob boss, Tony Soprano, deals with personal and professional issues in his home and business life.", 15, "HBO", "img/sopranos.jpg","https://www.youtube.com/watch?v=wrN2k3qGbVA", "James Gandolfini, Cast Two")

thewire = media.TvShow("The Wire", "Baltimore drug scene, seen through the eyes of drug dealers and law enforcement.", 12, "HBO", "img/the_wire.jpg","https://www.youtube.com/watch?v=W3vNEd1mkaI", "Cast One, Cast Two, Cast Three")

#the_witcher = media.Game("The Witcher", "The world doesn't need a hero, it needs a professional!", 5, 'XBOX One')

#print(the_witcher.title)
#print(the_witcher.synopsis)
#print(the_witcher.rating)
#print(the_witcher.platform)

movies = []
movies.append(wild_at_heart)
movies.append(down_by_law)
movies.append(night_on_earth)

tv_shows = []
tv_shows.append(sopranos)
tv_shows.append(thewire)

# Create an new html page and open it in the systems standard browser by calling open_movies in fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies, tv_shows)