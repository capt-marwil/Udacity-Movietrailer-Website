#coding=utf-8
import media
import fresh_tomatoes

# Create 6 instances of class media.Movie
wild_at_heart = media.Movie(
    "Wild at Heart",
    "Young lovers Sailor and Lula run from the variety of weirdos that Lula\'s mom has hired to kill Sailor.",
    "This whole world's wild at heart and weird on top.",
    "img/wild_at_heart.jpg",
    "https://www.youtube.com/watch?v=QCQwumNQL9E",
    "David Lynch",
    "Nicolas Cage, Laura Dern, et. al.")


down_by_law = media.Movie(
    "Down by Law",
    "The story of three different men in a Louisiana prison and their eventual journey.",
    "I scream. You scream. We all scream. For ice cream.",
    "img/down_by_law.jpg",
    "www.youtube.com/watch?v=1H9zlFH7UhA",
    "Jim Jarmusch",
    "Roberto Benigni, John Lurie, Tom Waits, et. al.")

night_on_earth = media.Movie(
    "Night on Earth",
    "An anthology of 5 different cab drivers in 5 American and European cities and their"
    " remarkable fares on the same eventful night.",
    "Are you sure you know where you are?",
    "img/night_on_earth.jpg",
    "https://www.youtube.com/watch?v=F1m6GlPyOSU",
    "Jim Jarmusch",
    "Winona Ryder, Roberto Bengini, Armin Müller-Stahl, et. al.")

godfather = media.Movie(
    "The Godfather",
    "The aging patriarch of an organized crime dynasty transfers control of"
    " his clandestine empire to his reluctant son.",
    "An offer you can\'t refuse.",
    "img/the_godfather.jpg",
    "https://www.youtube.com/watch?v=w0VGcWHkNeA",
    "Francis Ford Coppola",
    "Marlon Brando, Al Pacino, James Caan, et. al.")

brother = media.Movie(
    "O Brother, Where Art Thou?",
    "In the deep south during the 1930s, three escaped convicts search for hidden "
    "treasure while a relentless lawman pursues them.",
    "Damn! We're in a tight spot!",
    "img/oh_brother_where_art_thou.jpg",
    "https://www.youtube.com/watch?v=I1C2gCXo4Gs",
    "Joel Coen",
    "George Clooney, John Turturro, Tim Blake Nelson, et. al.")

budapest = media.Movie(
    "The Grand Budapest Hotel",
    "The adventures of Gustave H, a legendary concierge at a famous hotel from the fictional Republic of Zubrowka"
    " between the first and second World Wars, and Zero Moustafa, the lobby boy who becomes his most trusted friend.",
    "Keep your hands off my lobby boy!",
    "img/budapest.jpg",
    "https://www.youtube.com/watch?v=2bTbW70umbQ",
    "Wes Anderson",
    "Ralph Fiennes, F. Murray Abraham, Mathieu Amalric, et. al.")

# Create 6 instances of class media.tv_shows
sopranos = media.TvShow(
    "The Sopranos",
    "New Jersey mob boss, Tony Soprano, deals with personal and professional issues in his home and business life.",
    "HBO",
    "img/sopranos.jpg",
    "https://www.youtube.com/watch?v=wrN2k3qGbVA",
    "James Gandolfini, Lorraine Bracco, Edie Falco, et. al.")

thewire = media.TvShow(
    "The Wire",
    "Baltimore drug scene, seen through the eyes of drug dealers and law enforcement.",
    "HBO",
    "img/the_wire.jpg",
    "https://www.youtube.com/watch?v=W3vNEd1mkaI",
    "Dominic West, Lance Riddick, Sonja Sohn, et. al.")

captain_future = media.TvShow(
    "Captain Future",
    "This series documents the adventures of Captain Future and the crew of his ship, the Comet.",
    "NHK",
    "img/captain_future.jpg",
    "https://www.youtube.com/watch?v=FZLG0mEDPc8",
    "Anime")

life_on_mars = media.TvShow(
    "Life on Mars",
    "After being involved in a car accident in 2006, DCI Sam Tyler wakes up to find himself in 1973, the era of"
    " 'Sweeney' type policing, Mark III Cortinas, and flared trousers.",
    "BBC",
    "img/life_on_mars.jpg",
    "https://www.youtube.com/watch?v=cmmFwGgC4aU",
    "Jon Simm, Philip Glenister, Liz White, et. al.")

tatortreiniger = media.TvShow(
    "Der Tatortreiniger",
    "The bizarre everyday adventures of Heiko \"Schotty\" Schotte, whose profession is to clean up crime scenes.",
    "NDR",
    "img/tatortreiniger.jpg",
    "https://www.youtube.com/watch?v=aRAQDNnmGRU",
    "Bjarne Mädel, Katharina M. Schubert, et. al.")

firefly = media.TvShow(
    "Firefly",
    "Five hundred years in the future, a renegade crew aboard a small spacecraft tries to survive as they travel"
    " the unknown parts of the galaxy and evade warring factions as well as authority agents out to get them.",
    "FOX",
    "img/firefly.jpg",
    "https://www.youtube.com/watch?v=mG9bSBGLtMc",
    "Nathan Fillion, Gina Torres, Alan Tudyk et. al.")


# create 6 instances of game objects of class media.Game
the_witcher = media.Game(
    "The Witcher",
    "The Witcher 3: Wild Hunt concludes the story of the witcher Geralt of Rivia,"
    " the serie's protagonist, whose story to date has been covered in the previous versions",
    "img/witcher3.jpeg",
    "https://www.youtube.com/watch?v=tDfa1Qp2SwA",
    "XBOX One, PS4, Microsoft Windows")

tentacle = media.Game(
    "Day of the tentacle",
    "Five years after the events of Maniac Mansion, Purple Tentacle—a mutant"
    " monster and lab assistant created by mad scientist Dr. Fred Edison—drinks"
    " toxic sludge from a river behind Dr. Fred's laboratory. The sludge causes"
    " him to grow a pair of flipper-like arms, develop vastly increased "
    "intelligence and a thirst for global domination.",
    "img/day_of_the_tentacle.jpeg",
    "https://www.youtube.com/watch?v=dZ7uWVp75tI",
    "DOS, Mac OS")

lego_star_wars = media.Game(
    "Lego Starwars",
    "The game comically retells the trilogy's events using cut scenes without dialogue."
    " The player assumes the roles of the films' characters, each of which possess specific weapons and abilities.",
    "img/lego_starwars.jpeg",
    "https://www.youtube.com/watch?v=XRZTJ35w9Sw",
    "Microsoft Windows, OS X, Xbox, GameCube, PlayStation 2, "
    "Game Boy Advance, Nintendo DS, PlayStation Portable, Xbox 360, Mobile phone")

indiana_jones = media.Game(
    "Indiana Jones and the fate of Atlantis",
    "The plot is set in the fictional Indiana Jones universe and revolves"
    " around the eponymous protagonist's global search for the legendary sunken city of Atlantis.",
    "img/indy_atlantis.jpeg",
    "https://www.youtube.com/watch?v=lncARrPO8Qo",
    "DOS, Mac OS, Amiga, FM Towns, Microsoft Windows, Wii")

masseffect = media.Game(
    "Mass Effect",
    "The game focuses on the protagonist, Commander Shepard, and his or her quest"
    " to stop the rogue Spectre Saren Arterius from leading an army of sentient machines,"
    " called the Geth, to conquer the galaxy.",
    "img/masseffect.jpeg",
    "https://www.youtube.com/watch?v=-_6ZMr2bMco",
    "XBOX 360, PS3, Microsoft Windows")

dragon_age_inquistiton = media.Game(
    "Dragon Age: Inquisition",
    "The story of Dragon Age: Inquisition follows a player character known as"
    " the Inquisitor on a journey to settle the civil unrest in the continent of"
    " Thedas and close a mysterious tear in the sky called the 'Breach',"
    " which is unleashing dangerous demons upon the world.",
    "img/inquisition.jpeg",
    "https://www.youtube.com/watch?v=jJqxfkgSUog",
    "XBOX 330, XBOX One, PS3, PS4, Microsoft Windows")

movies = []
movies.append(wild_at_heart)
movies.append(down_by_law)
movies.append(night_on_earth)
movies.append(godfather)
movies.append(brother)
movies.append(budapest)

tv_shows = []
tv_shows.append(life_on_mars)
tv_shows.append(tatortreiniger)
tv_shows.append(firefly)
tv_shows.append(sopranos)
tv_shows.append(thewire)
tv_shows.append(captain_future)

games = []
games.append(tentacle)
games.append(indiana_jones)
games.append(lego_star_wars)
games.append(dragon_age_inquistiton)
games.append(masseffect)
games.append(the_witcher)


# Create an new html page and open it in the systems standard browser by calling open_movies in fresh_tomatoes.py
fresh_tomatoes.open_movies_page(movies, tv_shows, games)