import Settings
import csv

"""
FileMaker.py:
    only thing this file does is create the start database file based on the settings in Settings.py
"""

'''
Creates the database file
'''
def create_database():

    columns = Settings.column_names
    for reviewer in Settings.reviewers:
        columns.append(reviewer)

    records = Settings.movies

    for index, record in enumerate(records):
        records[index].append(Settings.unwatched_symbol)

        for reviewer in enumerate(Settings.reviewers):
            records[index].append(Settings.unwatched_symbol)

    with open(Settings.file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(columns)
        writer.writerows(records)
