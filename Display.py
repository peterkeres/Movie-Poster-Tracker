from prettytable import PrettyTable
from progress.spinner import PixelSpinner
import time
import Settings

"""
Display Class:
    Handles all output for the program
"""


class Display:
    """
    Displays the output of a movie pick
    list[] pick: the movie record of the movie that has been picked to watch
    """
    @staticmethod
    def display_pick(pick):
        # Note: this does noting really, commit out if you dont want wait for the loading bar
        spinner = PixelSpinner('Finding a movie! ')
        for i in range(10):
            time.sleep(.3)
            spinner.next()

        print(f'\nGet ready to watch! {pick[1]}')

    """
    Displays the output for when a movie is set to watched
    list[] record: the movie record of the movie that has been set to watched status
    """
    @staticmethod
    def display_updated_record(record):
        print(f"\"{record[1]}\" has been updated!!!")

    """
    Displays a table output for whatever action is entered
    list[] movie_list: lists of movie records to be displayed
    """
    @staticmethod
    def display_table(movie_list):
        table = PrettyTable()
        table.field_names = Settings.column_names + Settings.reviewers

        for movie in movie_list:
            watched = ""
            rating = ""
            row = [movie[0], movie[1], movie[2]]

            # fills the watched column
            if movie[3] == Settings.watched_symbol:
                watched = Settings.watched_emoji
            else:
                watched = Settings.unwatched_emoji

            row.append(watched)

            # fills out each reviewer's column
            for reviewer in range(4, len(movie)):
                if movie[reviewer] == Settings.unwatched_symbol:
                    pass
                else:
                    for index in range(0, int(movie[reviewer])):
                        rating += Settings.rating_point + " "
                    for index in range(0, (5 - int(movie[reviewer]))):
                        rating += Settings.rating_missing + " "

                row.append(rating)
                rating = ""

            table.add_row(row)

        print(table)

    """
    Displays an error message for when scores are missing during the watched command
    list[] missing_scores: a list of who's scores are missing
    """
    @staticmethod
    def error_score_missing(missing_scores):
        print('ERROR!!!! Missing review scores for the following:')
        for missing in missing_scores: print(missing)

    """
    Displays an error message when a movie could not be found
    Str movie: the string of the movie that the USER entered
    """
    @staticmethod
    def error_missing_movie(moive):
        print(f'ERROR!!!! Could not find movie \"{moive}\", Check spelling')