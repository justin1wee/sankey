"""
File: convert_hw2.py
Authors: Andy Lin, Justin Wee
Description: Converts the artists.json file into a dataframe and groups categories accordingly
"""

import pandas as pd

def convert_to_df(filename='artists.json'):
    """
    Converts the artists json file to a pandas dataframe and cleans dataframe to
    include only relevant information

    :param FILENAME: name of the file to convert (i.e. artists.json)
    :return df_artists: a pandas dataframe of artists and relevant information
    """

    # Import file
    artists = pd.read_json(filename)
    df_artists = artists.loc[:,['Nationality', 'Gender', 'BeginDate']]

    # Calculate and store Decade column as an integer, and removes BeginDate column
    df_artists['Decade'] = (df_artists['BeginDate'] // 10) * 10
    df_artists.drop('BeginDate', axis=1, inplace=True)

    # Filter rows out which have 0 as decade and/or missing data
    df_artists = df_artists[(df_artists['Decade'] != 0) & (df_artists['Nationality'].notnull() &
                                                           (df_artists['Nationality'] != 'Nationality unknown'))]

    return df_artists

def group_df(df, cats):
    """
    Groups the dataframe by two categories and creates an artist count column

    :param df: the dataframe to be modified
    :param cats: list of categories for dataframe to be grouped by
    :return grouped_artists: a pandas dataframe grouped by two categories and a count column
    """

    # Group artists by Category 1 and Category 2
    grouped_artists = df.groupby(cats).size().reset_index(name='artist_count')

    # Filter out all counts that are less than 20
    grouped_artists = grouped_artists[(grouped_artists['artist_count'] >= 20)]

    return grouped_artists




