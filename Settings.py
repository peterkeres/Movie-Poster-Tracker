import UserSettings

"""
Settings.py:
    This file just values that are used in other parts of the program

IF you are looking to change settings, like reviweres, Please go to the UserSettings.py file to make your changes
"""

reviewers = UserSettings.reviewers

file_path = UserSettings.file_path

column_names = ["Spot", "Movie", "Director", "Watched"]

watched_symbol = 'X'
unwatched_symbol = '-'

rating_point = UserSettings.rating_point
rating_missing = UserSettings.rating_missing

watched_emoji = UserSettings.watched_emoji
unwatched_emoji = UserSettings.unwatched_emoji

movies = [
    [1, 'The ShawShank Redemption', "Frank Darabont"],
    [2, 'The Dark Knight', 'Christopher Nolan'],
    [3, 'City of God', 'F Meirelles K Lund'],
    [4, 'Pulp Fiction', 'Quentin Tarntino'],
    [5, 'Amelie', 'Jean Pierre Jeunet'],
    [6, '12 Angery Men', 'Sidney Lumet'],
    [7, 'Blade Runnder', 'Ridley Scott'],
    [8, 'A Clockwork Orange', 'Stanley Kubrick'],
    [9, 'The Deer Hunter', 'Micheal Clmino'],
    [10, 'Casblanca', 'Micheal Curtiz'],
    [11, 'E.T.', 'Steven Spielberg'],
    [12, 'UP', 'Doctor B Peterson'],
    [13, 'The Rocky Horror Picture Show', 'Jim Sharman'],
    [14, 'The Big Lebowski', 'The Coen Brothers'],
    [15, 'Office Space', 'Mike Judge'],
    [16, 'Fight Club', 'David Fincher'],
    [17, 'Snatch', 'Guy Ritchie'],
    [18, 'Old Boy', 'Park Chan Wook'],
    [19, 'Leon: The Professional', 'Luc Besson'],
    [20, 'Scarface', 'Brian De Palma'],
    [21, 'Raiders of the Lost Ark', 'Steven Spielberg'],
    [22, 'The Lord of the Rings', 'Peter Jackson'],
    [23, 'Moonlight', 'Barry Jenkins'],
    [24, 'The Matrix', 'The Wachowskis'],
    [25, 'Apocalypse Now', 'Francis Ford Coppola'],
    [26, 'The Grand Budapest Hotel', 'Wes Anderson'],
    [27, 'Monty Python\'s Life of Brain', 'Terry Jones'],
    [28, 'In Bruges', 'Martin Mcdonach'],
    [29, '3 Idiots', 'Rajkumar Hirani'],
    [30, 'The Godfather', 'Francis Ford Coppola'],
    [31, 'The Notebook', 'Nick Cassavetes'],
    [32, 'The Lion King', 'R Allers R Minkoff'],
    [33, 'Stand By Me', 'Rob Reiner'],
    [34, 'Dirty Dancing', 'Emile Ardolino'],
    [35, 'Jurassic Park', 'Steven Spielberg'],
    [36, '2001: A Space Odyssey', 'Stanley Kubrick'],
    [37, 'The Goonies', 'Richard Donner'],
    [38, 'Wall-E', 'Andrew Stanton'],
    [39, 'Groundhog Day', 'Harold Ramis'],
    [40, 'Star Wars 4 5 6', 'George Lucas'],
    [41, 'Schindler\'s List', 'Steven Spielberg'],
    [42, 'Breakfast at Tiffany\'s', 'Blake Edwards'],
    [43, 'Shaun of the Dead', 'Edgar Wright'],
    [44, 'Back to the Future', 'Robert Zemeckis'],
    [45, 'Forrest Gump', 'Robert Zemeckis'],
    [46, 'The Silence of the Lambs', 'Jonathan Demme'],
    [47, 'The Shining', 'Stanley Kubrick'],
    [48, 'Alien', 'Ridley Scott'],
    [49, 'Memento', 'Christopher Nolan'],
    [50, 'Se7en', 'David Fincher'],
    [51, 'halloween', 'John Carpenter'],
    [52, 'Jaws', 'Steven Spielberg'],
    [53, 'The Evil Dead', 'Sam Raimi'],
    [54, 'Airplane!', 'D Zucker J Abrahams J Zucker'],
    [55, 'Mean Girls', 'Mark Waters'],
    [56, 'Lawrence of Arabia', 'David Lean'],
    [57, 'Drive', 'Nicolas Winding Refn'],
    [58, 'Casino Royale', 'Martin Campbell'],
    [59, 'Ghosterbusters', 'Ivan Reitman'],
    [60, 'Rosemary\'s Baby', 'Roman Polanski'],
    [61, 'Marry & Max', 'Adam Elliot'],
    [62, 'The Terminator', 'James Cameron'],
    [63, 'The Green Mile', 'Frank Darabont'],
    [64, 'Rocky', 'John G Acildsen'],
    [65, 'This is Spinal Tap', 'Rob Reiner'],
    [66, 'American Psycho', 'Mary Harpon'],
    [67, 'Citizen Kane', 'Orson Welles'],
    [68, 'The Intouchables', 'O Nakache E Toledano'],
    [69, 'American History X', 'Tony Kaye'],
    [70, 'Seven Samurai', 'Akira Kurosawa'],
    [71, 'Gladiator', 'Ridely Scott'],
    [72, 'The Good The Bad and The Ugly', 'Sergio Leone'],
    [73, 'Brokeback Mountian', 'Ang Lee'],
    [74, 'The Great Dictator', 'Charles Chaplin'],
    [75, 'Toy Story', 'John Lasseter'],
    [76, 'The Prestige', 'Christopher Nolan'],
    [77, 'titanic', 'James Cameron'],
    [78, 'Her', 'Spike Jonze'],
    [79, 'Boyz in the Hood', 'John Singleton'],
    [80, 'Four Weddings and a Funeral', 'Mike Newell'],
    [81, 'Little Miss Sunshine', 'J Dayton V Faris'],
    [82, 'Trainspotting', 'Danny Boyle'],
    [83, 'The Departed', 'Martin Scorsese'],
    [84, 'Saving Private Ryan', 'Steven Speliberg'],
    [85, 'No Country for Old Men', 'The Coen Brothers'],
    [86, 'The Pianist', 'Roman Polanski'],
    [87, 'Dr Strangelove', 'Stanley Kibrick'],
    [88, 'Lagaan', 'Ashutosh Dowalker'],
    [89, 'Baahubali', 'S S Rajamoil'],
    [90, 'Psycho', 'Alfred Hitchock'],
    [91, 'Vertigo', 'Alfred Hitchcock'],
    [92, 'The Truman Show', 'Peter Wejr'],
    [93, 'Reservoir Dogs', 'Quentin Tapanting'],
    [94, 'Amadeus', 'Milos Forman'],
    [95, 'Enter The Dragon', 'Robert Clouse'],
    [96, 'The Wizard of OZ', 'Velmino et al'],
    [97, 'Gangs of New York', 'Martin Scorsese'],
    [98, 'The Usual Suspects', 'Bravan Singer'],
    [99, 'Spirited Away', 'Hayao Miyazaki'],
    [100, 'Good Will Hunting', 'Gus Van Sant']
]
