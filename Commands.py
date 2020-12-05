from random import randint
from MoviesModel import MoviesModel
from Display import Display
import Settings

'''
COMMAND CLASS:
    Does the work of executing all the commands pulled from the command line. 
'''


class Command:
    """
    The default constructor
    Str Command: The command entered at the command line
    """
    def __init__(self, command):
        self.command = command
        self.movies = MoviesModel()
        self.__run()

    """
    Figures out what command was entered and executes that method
    """
    def __run(self):

        if self.command.action == 'pick':
            self.__pick()
        elif self.command.action == 'list':
            self.__list()
        elif self.command.action == 'watched':
            self.__watched()

    """
    The pick Command:
    Picks a random movie that is not watched and displays it
    """
    def __pick(self):
        movie_list = self.movies.get_unwatched_movies()
        pick = randint(0, len(movie_list) - 1)

        Display.display_pick(movie_list[pick])

    """
    Allows the sort method to be based on the movie title
    """
    @staticmethod
    def __takeName(movie_list):
        return movie_list[1]

    """
    Allows the sort method to be based on lowest rating
    """
    @staticmethod
    def __worst(movie_list):
        tmp = 0

        for index, section in enumerate(movie_list):
            if index >= 4:
                tmp += int(section)

        return tmp

    """
    The List Command:
    Lists movies based on what optional augment is entered
    """
    def __list(self):

        # Displays all movies, watched and unwatched in alphabetical order
        if self.command.all:
            movie_list = self.movies.get_all_movies()
            movie_list.sort(key=self.__takeName)
            Display.display_table(movie_list)

        # Displays only watched movies in alphabetical order
        elif self.command.seen:
            movie_list = self.movies.get_watched_movies()
            movie_list.sort(key=self.__takeName)
            Display.display_table(movie_list)

        # Displays watched movies in order of best to worst
        elif self.command.best:
            movie_list = self.movies.get_watched_movies()
            movie_list.sort(key=self.__worst, reverse=True)
            Display.display_table(movie_list)

        # Displays watched movies in order of worst to best
        elif self.command.worst:
            movie_list = self.movies.get_watched_movies()
            movie_list.sort(key=self.__worst)
            Display.display_table(movie_list)

        # Default behavior, displays all unwatched movies
        else:
            movie_list = self.movies.get_unwatched_movies()
            movie_list.sort(key=self.__takeName)
            Display.display_table(movie_list)

    """
    The Watched Command:
    Sets a movies status to 'watched' and updates the movies rating
    """
    def __watched(self):

        movie = " ".join(self.command.movie)
        all_parameters = self.command.__str__().split(',')
        reviewer_scores = {}
        missing_scores = []

        # goes though the list of parameters to find the review scores
        for parameter in all_parameters:
            section = parameter.split('=')[0].strip()
            for reviewer in Settings.reviewers:
                if section.lower() == reviewer.lower():
                    if (parameter.split('=')[1].strip()).isnumeric():
                        reviewer_scores[reviewer.lower()] = int(parameter.split('=')[1].strip())
                    else:
                        missing_scores.append(reviewer)

        # checks to see if all reviewer scores are accounted for
        if len(reviewer_scores) == len(Settings.reviewers):
            result = self.movies.set_watched(movie, reviewer_scores)

            if result:
                Display.display_updated_record(result)
            else:
                Display.error_missing_movie(movie)
        else:
            missing = []
            for person in missing_scores:
                missing.append(person)

            Display.error_score_missing(missing)
