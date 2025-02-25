'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd

def convert_dates(dataframe):
    '''
        Converts the dates in the dataframe to datetime objects.

        Args:
            dataframe: The dataframe to process
        Returns:
            The processed dataframe with datetime-formatted dates.
    '''
    # TODO : Convert dates
    dataframe['Date_Plantation'] = pd.to_datetime(dataframe['Date_Plantation'])
    return dataframe


def filter_years(dataframe, start, end):
    '''
        Filters the elements of the dataframe by date, making sure
        they fall in the desired range.

        Args:
            dataframe: The dataframe to process
            start: The starting year (inclusive)
            end: The ending year (inclusive)
        Returns:
            The dataframe filtered by date.
    '''
    # TODO : Filter by dates
    dataframe = dataframe[(dataframe['Date_Plantation'].dt.year >= start) & (dataframe['Date_Plantation'].dt.year <= end)]
    return dataframe


def summarize_yearly_counts(dataframe):
    '''
        Groups the data by neighborhood and year,
        summing the number of trees planted in each neighborhood
        each year.

        Args:
            dataframe: The dataframe to process
        Returns:
            The processed dataframe with column 'Counts'
            containing the counts of planted
            trees for each neighborhood each year.
    '''
    # TODO : Summarize df
    df = dataframe.copy()
    # Extract year from Date_Plantation as an integer
    df['Year'] = df['Date_Plantation'].dt.year
    # Group by neighborhood and year, count rows
    yearly_counts = df.groupby(['Arrond_Nom', 'Year']).size().reset_index(name='Counts')
    # Rename 'Year' to 'Date_Plantation'
    yearly_counts.rename(columns={'Year': 'Date_Plantation'}, inplace=True)
    return yearly_counts



def restructure_df(yearly_df):
    '''
        Restructures the dataframe into a format easier
        to be displayed as a heatmap.

        The resulting dataframe should have as index
        the names of the neighborhoods, while the columns
        should be each considered year. The values
        in each cell represent the number of trees
        planted by the given neighborhood the given year.

        Any empty cells are filled with zeros.

        Args:
            yearly_df: The dataframe to process
        Returns:
            The restructured dataframe
    '''
    # TODO : Restructure df and fill empty cells with 0
    # pivot the dataframe and fill empty cells with 0
    heatmap_df = yearly_df.pivot(
        index='Arrond_Nom',
        columns='Date_Plantation',
        values='Counts'
    ).fillna(0)
     
    return heatmap_df


def get_daily_info(dataframe, arrond, year):
    '''
        From the given dataframe, gets
        the daily amount of planted trees
        in the given neighborhood and year.

        Args:
            dataframe: The dataframe to process
            arrond: The desired neighborhood
            year: The desired year
        Returns:
            The daily tree count data for that
            neighborhood and year.
    '''
    # TODO : Get daily tree count data and return
        # Filter the dataframe for the given year and neighborhood
    # Filter the dataframe for the given year and neighborhood
    df_filtered = dataframe[
        (dataframe['Arrond_Nom'] == arrond) & 
        (dataframe['Date_Plantation'].dt.year == int(year))
    ]
    
    # Group by day and count the number of trees planted each day
    daily_counts = df_filtered.groupby('Date_Plantation').size()
    
    # Create a date range from the min to max planting date
    date_range = pd.date_range(
        start=daily_counts.index.min(),
        end=daily_counts.index.max(),
        freq="D"
    )
    
    # Reindex to include all dates in the range, filling missing with 0
    daily_counts = daily_counts.reindex(date_range, fill_value=0).reset_index()
    
    # Rename columns to match the first function
    daily_counts.columns = ['Date_Plantation', 'Counts']
    
    return daily_counts

# data = pd.read_csv('src/assets/data/arbres.csv')
# data = convert_dates(data)
# data = filter_years(data, 2010, 2020)
# data = summarize_yearly_counts(data)
# data = restructure_df(data)
# print(data)
# data = get_daily_info(data, 'Le Sud-Ouest', '2017')
# print(data.to_string(index=False))