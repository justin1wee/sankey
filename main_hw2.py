"""
File: main_hw2.py
Author: Andy Lin and Justin Wee
Description: A main file that runs each library to generate Sankey diagrams for the artists.json file
"""

import sankey_hw2 as sk
import convert_hw2 as cv

def main():

    # Load the cleaned artists dataframe
    df_artists = cv.convert_to_df()

    # Generate the first sankey diagram, grouping by Nationality and Decade
    grouped_df1 = cv.group_df(df_artists, ['Nationality', 'Decade'])
    sk.make_sankey(grouped_df1, ['Nationality', 'Decade'], 'artist_count')

    # Generate the second sankey diagram, grouping by Nationality and Gender
    grouped_df2 = cv.group_df(df_artists, ['Nationality', 'Gender'])
    sk.make_sankey(grouped_df2, ['Nationality', 'Gender'], 'artist_count')

    # Generate the third sankey diagram, grouping by Gender and Decade
    grouped_df3 = cv.group_df(df_artists, ['Gender', 'Decade'])
    sk.make_sankey(grouped_df3, ['Gender', 'Decade'], 'artist_count')

    # Generate the multi-layered sankey diagram, grouped by all three categories
    grouped_df4 = cv.group_df(df_artists, ['Nationality', 'Gender', 'Decade'])
    sk.make_sankey(grouped_df4, ['Gender', 'Nationality', 'Decade'], 'artist_count')

if __name__ == "__main__":
    main()
