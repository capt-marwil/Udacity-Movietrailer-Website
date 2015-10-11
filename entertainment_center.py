import media
import fresh_tomatoes

# Create Instances of class media.Movie
wild_at_heart = media.Movie("Wild at Heart",  "Young lovers Sailor and Lula run from the variety of weirdos that Lula's mom has hired to kill Sailor.", "This whole world's wild at heart and weird on top.", "img/wild_at_heart.jpg", "https://www.youtube.com/watch?v=QCQwumNQL9E", "David Lynch", "Nicolas Cage, Laura Dern, et. al.")


down_by_law = media.Movie("Down by Law",  "The story of three different men in a Louisiana prison and their eventual journey.", "I scream. You scream. We all scream. For ice cream.", "img/down_by_law.jpg", "www.youtube.com/watch?v=1H9zlFH7UhA", "Jim Jarmusch", "Roberto Benigni, John Lurie, Tom Waits, et. al.")

night_on_earth = media.Movie("Night on Earth", "An anthology of 5 different cab drivers in 5 American and European cities and their remarkable fares on the same eventful night.", "Are you sure you know where you are?", "img/night_on_earth.jpg", "https://www.youtube.com/watch?v=F1m6GlPyOSU", "Jim Jarmusch", "Winona Ryder, Roberto Bengini, Armin Müller-Stahl, et. al.")

godfather = media.Movie("The Godfather", "The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.",  "An offer you can\'t refuse.", "img/the_godfather.jpg", "https://www.youtube.com/watch?v=w0VGcWHkNeA", "Francis Ford Coppola", "Marlon Brando, Al Pacino, James Caan, et. al.")

brother = media.Movie("O Brother, Where Art Thou?", "In the deep south during the 1930s, three escaped convicts search for hidden treasure while a relentless lawman pursues them.", "Damn! We're in a tight spot!", "img/oh_brother_where_art_thou.jpg", "https://www.youtube.com/watch?v=I1C2gCXo4Gs", "Joel Coen", "George Clooney, John Turturro, Tim Blake Nelson, et. al.")

budapest = media.Movie("The Grand Budapest Hotel", "The adventures of Gustave H, a legendary concierge at a famous hotel from the fictional Republic of Zubrowka between the first and second World Wars, and Zero Moustafa, the lobby boy who becomes his most trusted friend.", "Keep your hands off my lobby boy!", "img/budapest.jpg", "https://www.youtube.com/watch?v=2bTbW70umbQ", "Wes Anderson", "Ralph Fiennes, F. Murray Abraham, Mathieu Amalric, et. al." )

# Create Instances of media.tv_shows (title, synopsis, tv_station, poster_image_url, trailer_youtube_url, cast):
sopranos = media.TvShow("The Sopranos", "New Jersey mob boss, Tony Soprano, deals with personal and professional issues in his home and business life.", "HBO", "img/sopranos.jpg","https://www.youtube.com/watch?v=wrN2k3qGbVA", "James Gandolfini, Cast Two")

thewire = media.TvShow("The Wire", "Baltimore drug scene, seen through the eyes of drug dealers and law enforcement.", "HBO", "img/the_wire.jpg","https://www.youtube.com/watch?v=W3vNEd1mkaI", "Cast One, Cast Two, Cast Three")

#the_witcher = media.Game("The Witcher", "The world doesn't need a hero, it needs a professional!", 5, 'XBOX One')

#print(the_witcher.title)
#print(the_witcher.synopsis)
#print(the_witcher.rating)
#print(the_witcher.platform)

movies = []
movies.append(wild_at_heart)
movies.append(down_by_law)
movies.append(night_on_earth)
movies.append(godfather)
movies.append(brother)
movies.append(budapest)

tv_shows = []
tv_shows.append(sopranos)
tv_shows.append(thewire)

# Create an new html page and open it in the systems standard browser by calling open_movies in fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies, tv_shows)