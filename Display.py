from prettytable import PrettyTable

"""
Display Class:
    Handles all output for the program
"""

class Display:

    """
    Displays a table output for whatever action is entered
    """
    def display_table(movie_list):
        t = PrettyTable()

        t.field_names = ["spot", "movie", "director", "watched", "peter", "elle"]

        for index, movie in enumerate(movie_list):
            watched = ""
            rating_peter = ""
            rating_elle = ""

            if movie[3] == "X":
                watched = "\u2705"
            else:
                watched = "\u274c"

            if movie[4] == "-":
                pass
            else:
                for index in range(0, int(movie[4])):
                    rating_peter += "* "
                for index in range(0, (5 - int(movie[4]))):
                    rating_peter += "- "

            if movie[5] == "-":
                pass
            else:
                for index in range(0, int(movie[5])):
                    rating_elle += "* "
                for index in range(0, (5 - int(movie[5]))):
                    rating_elle += "- "

            t.add_row([movie[0], movie[1], movie[2], watched, rating_peter, rating_elle])

        print(t)
