"""
File: sankey_hw2.py
Description: Provide a wrapper that maps a dataframe to a sankey diagram
"""
import plotly.graph_objects as go


def _code_mapping(df, columns):
    """
    Map labels in dataframe columns to integers that can be used in the make_sankey function

    :param df: pandas dataframe where data comes from
    :param columns: list of columns to be mapped
    :return df: dataframe with values mapped to integers
    :return labels: labels of each node of the sankey diagram
    """
    labels = []

    # get distinct labels
    for col in columns:
        labels.extend(list(df[col]))

    labels = sorted(set(labels), key=str)

    # get integer codes
    codes = list(range(len(labels)))

    # create label to code mapping
    lc_map = dict(zip(labels, codes))

    # substitute names for codes in the dataframe
    for col in columns:
        df = df.replace({col: lc_map})

    return df, labels


def make_sankey(df, columns, vals):
    """
    Map a dataframe to a sankey diagram
    :param df: Input dataframe
    :param columns: List of columns from dataframe
    :param vals: Thickness of the link for each row
    :return:
    """

    # Provides default values if vals is not given
    if vals:
        values = df[vals]
    else:
        values = [1] * len(df) # all 1's

    # Uses helper function to map code to dataframe
    df, labels = _code_mapping(df, columns)

    # Initialize source, target, and value lists for links
    sources, targets, values = [], [], []

    # Process each pair of adjacent columns as source and target
    for i in range(len(columns) - 1):
        sources.extend(df[columns[i]])
        targets.extend(df[columns[i + 1]])
        values.extend(df[vals])

    # Define the link and node for the Sankey diagram
    link = {'source': sources, 'target': targets, 'value': values,
            'line': {'color': 'black', 'width': 0.2}}
    node = {'label': labels}

    # Produce sankey diagram
    sk = go.Sankey(link=link, node=node)
    fig = go.Figure(sk)
    fig.show()
