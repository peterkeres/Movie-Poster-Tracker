import csv
import Settings

"""
Movies Model Class:
    interacts with the 'database' to pull in data to pass to the commands.py class
"""


class MoviesModel:
    """
    The default constructor
    """

    def __init__(self):
        self.file_path = Settings.file_path

    """
    Grabs all the movie records from the database text file
    Return: List[]
    """

    def get_all_movies(self):
        with open(self.file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            movie_list = []
            line_count = 0

            for row in csv_reader:
                if line_count == 0:
                    pass
                else:
                    movie_list.append(row)

                line_count += 1

        return movie_list

    """
    Gabs all unwatched movie records from the database text file
    Return: List[]
    """

    def get_unwatched_movies(self):

        all_movies = self.get_all_movies()
        unwatched_movies = []

        for movie in all_movies:

            if movie[3] == "-":
                unwatched_movies.append(movie)

        return unwatched_movies

    """
    Grabs all watched movie records from the database text file
    Return: List[]
    """

    def get_watched_movies(self):

        all_movies = self.get_all_movies()
        watched_movies = []

        for movie in all_movies:

            if movie[3] == 'X':
                watched_movies.append(movie)

        return watched_movies

    """
    Sets a movie record to a 'watched' status
    Also sets the rating on the movie
    
    Str Movie: the movie you want to set watched status on
    Dictionary Ratings: a dictionary of each rating scores with the key being the reviewer's name and value being score
    
    Return: Bool If the watched status was set on the movie record
    """

    def set_watched(self, movie, ratings):

        all_movies = self.get_all_movies()
        all_movies.insert(0, Settings.column_names + Settings.reviewers)
        found = False

        search = movie.lower()

        for index, movie in enumerate(all_movies):

            cur_movie = movie[1].lower()

            if cur_movie == search:
                all_movies[index][3] = Settings.watched_symbol

                for slot, reviewer in enumerate(Settings.reviewers):
                    all_movies[index][slot + 4] = ratings[reviewer.lower()]
                found = all_movies[index]
        if found:
            with open(self.file_path, mode='w') as csv_file:
                movie_writer = csv.writer(csv_file)

                movie_writer.writerows(all_movies)

        return found

    def find_movie(self, movie):
        all_movies = self.get_all_movies()

        found = False

        for curMovie in all_movies:

            if curMovie[1] == movie:
                found = curMovie

        return found
