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
    the default constructor
    Str Command: The command entered at the command line
    """

    def __init__(self, command):
        self.command = command
        self.movies = MoviesModel()
        self.__run()

    """
    Figures out what command was entered and executes that method
    """

    # todo check is enter command upper case breakes this
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

    # todo push out to the display file
    def __pick(self):
        movie_list = self.movies.get_unwatched_movies()
        pick = randint(0, len(movie_list) - 1)

        # print(movie_list[pick])
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

    # todo test this!
    @staticmethod
    def __worst(movie_list):
        tmp = 0

        for index, section in enumerate(movie_list):
            if index >= 4:
                tmp += int(section)
        # return int(movie_list[5]) + int(movie_list[4])
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

    # todo double check all works, seems too. then send over to the datbase file
    def __watched(self):

        movie = " ".join(self.command.movie)
        all_parameters = self.command.__str__().split(',')
        reviewer_scores = {}
        missing_scores = []

        for parameter in all_parameters:
            section = parameter.split('=')[0].strip()
            for reviewer in Settings.reviewers:
                if section.lower() == reviewer.lower():
                    if (parameter.split('=')[1].strip()).isnumeric():
                        print(section)
                        reviewer_scores[reviewer.lower()] = int(parameter.split('=')[1].strip())
                    else:
                        missing_scores.append(reviewer)
                        print("ERROR!!!")

        if len(reviewer_scores) == len(Settings.reviewers):
            print('all good,move on')
            print(reviewer_scores)
        else:
            print("missing the scores of", end=" ")
            for person in missing_scores:
                print(person.capitalize(), end=", "),

        # for section in Settings.reviewers:
        #     print(self.command.__str__())
        #
        # if self.movies.set_watched(movie, self.command.peter, self.command.elle):
        #     print(f"{movie} updated!")
        # else:
        #     print(f"Movie: \"{movie}\" Could not be found ;(")
