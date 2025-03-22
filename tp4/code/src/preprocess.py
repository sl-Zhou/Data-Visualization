'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd

def round_decimals(my_df):
    '''
        Rounds all the numbers in the dataframe to two decimal points

        args:
            my_df: The dataframe to preprocess
        returns:
            The dataframe with rounded numbers
    '''
    # TODO : Round the dataframe
    # Create a copy of the dataframe
    df_rounded = my_df.copy()
    
    # Round the GDP column to 2 decimal places
    if 'GDP' in df_rounded.columns:
        df_rounded['GDP'] = df_rounded['GDP'].round(2)
    
    # Round the CO2 column to 2 decimal places
    if 'CO2' in df_rounded.columns:
        df_rounded['CO2'] = df_rounded['CO2'].round(2)
    
    return df_rounded


def get_range(col, df1, df2):
    '''
        An array containing the minimum and maximum values for the given
        column in the two dataframes.

        args:
            col: The name of the column for which we want the range
            df1: The first dataframe containing a column with the given name
            df2: The first dataframe containing a column with the given name
        returns:
            The minimum and maximum values across the two dataframes
    '''
    # TODO : Get the range from the dataframes
    min_value = min(df1[col].min(), df2[col].min())
    max_value = max(df1[col].max(), df2[col].max())
    # Return as an array [min, max]
    return [min_value, max_value]


def combine_dfs(df1, df2):
    '''
        Combines the two dataframes, adding a column 'Year' with the
        value 2000 for the rows from the first dataframe and the value
        2015 for the rows from the second dataframe

        args:
            df1: The first dataframe to combine
            df2: The second dataframe, to be appended to the first
        returns:
            The dataframe containing both dataframes provided as arg.
            Each row of the resulting dataframe has a column 'Year'
            containing the value 2000 or 2015, depending on its
            original dataframe.
    '''
    # TODO : Combine the two dataframes
    # Create copies of the dataframes
    df1_copy = df1.copy()
    df2_copy = df2.copy()
    
    # Add 'Year' column to each dataframe
    df1_copy['Year'] = 2000
    df2_copy['Year'] = 2015
    
    # Combine the two dataframes
    combined_df = pd.concat([df1_copy, df2_copy], ignore_index=True)
    
    return combined_df


def sort_dy_by_yr_continent(my_df):
    '''
        Sorts the dataframe by year and then by continent.

        args:
            my_df: The dataframe to sort
        returns:
            The sorted dataframe.
    '''
    # TODO : Sort the dataframe
    # Sort the dataframe by 'Year' and then by 'Continent'
    sorted_df = my_df.sort_values(by=['Year', 'Continent'])
    sorted_df = sorted_df.reset_index(drop=True)

    return sorted_df
