'''
    Contains some functions to preprocess the data used in the visualisation.
'''
import pandas as pd
# import json

TITLES = {
    # pylint: disable=line-too-long
    '1. Noyau villageois': 'Noyau villageois',
    '2. Rue commerciale de quartier, d’ambiance ou de destination': 'Rue commerciale de quartier, d’ambiance ou de destination', # noqa : E501
    '3. Rue transversale à une rue commerciale': 'Rue transversale à une rue commerciale', # noqa : E501
    '4. Rue bordant un bâtiment public ou institutionnel  (tels qu’une école primaire ou secondaire, un cégep ou une université, une station de métro, un musée, théâtre, marché public, une église, etc.)': 'Rue bordant un bâtiment public ou institutionnel', # noqa : E501
    '5. Rue en bordure ou entre deux parcs ou place publique': 'Rue en bordure ou entre deux parcs ou place publique', # noqa : E501
    '6. Rue entre un parc et un bâtiment public ou institutionnel': 'Rue entre un parc et un bâtiment public ou institutionnel', # noqa : E501
    '7. Passage entre rues résidentielles': 'Passage entre rues résidentielles'
}


def to_df(data):
    '''
        Converts the data to a pandas dataframe.

        Args:
            data: The data to convert
        Returns:
            my_df: The corresponding dataframe
    '''
    # TODO : Convert JSON formatted data to dataframe
    if isinstance(data, dict):
        if "features" in data:
            # Handling GeoJSON-like structure
            features = data["features"]
            if not features:
                raise ValueError("No features found in GeoJSON data")

            # Extract properties and geometry
            type = [feature["type"] for feature in features]
            properties = [feature["properties"] for feature in features]
            geometries = [feature["geometry"] for feature in features]

            # Convert to DataFrames with prefixed column names
            type_df = pd.DataFrame(type, columns=["type"])
            properties_df = pd.DataFrame(properties).add_prefix("properties.")
            geometries_df = pd.json_normalize(geometries)
            geometries_df.columns = [f"geometry.{col}" for col in geometries_df.columns]

            # Combine into a single DataFrame
            my_df = pd.concat([type_df, properties_df, geometries_df], axis=1)
        else:
            # Handling regular JSON dictionary
            my_df = pd.json_normalize(data)
    elif isinstance(data, list):
        # Handling list of dictionaries
        if not data:
            raise ValueError("Empty list provided")
        my_df = pd.DataFrame(data)
    else:
        raise ValueError("Unsupported data format: must be dict or list")

    return my_df


def update_titles(my_df):
    '''
        Updates the column "TYPE_SITE_INTERVENTION" with corresponding
        values from the 'TITLES' dictionary (above).

        Args:
            my_df: The dataframe to update
        Returns:
            my_df: The dataframe with the appropriate replacements
                made according to the 'TITLES' dictionary
    '''
    # TODO : Update the titles
    my_df["properties.TYPE_SITE_INTERVENTION"] = my_df["properties.TYPE_SITE_INTERVENTION"].replace(TITLES)
    return my_df


def sort_df(my_df):
    '''
        Sorts the dataframe by the column "TYPE_SITE_INTERVENTION" in
        alphabetical order.

        Args:
            my_df: The dataframe to sort
        Returns:
            my_df: The sorted dataframe
    '''
    # TODO : Sort the df
    my_df = my_df.sort_values(by="properties.TYPE_SITE_INTERVENTION", ascending=True)
    return my_df


def get_neighborhoods(montreal_data):
    '''
        Gets the name of the neighborhoods in the dataset

        Args:
            montreal_data: The data to parse
        Returns:
            locations: An array containing the names of the
                neighborhoods in the data set
    '''
    # TODO : Return the array of neighborhoods
    locations = [feature["properties"]["NOM"] for feature in montreal_data["features"]]
    return locations

# with open('./assets/data/montreal.json', encoding='utf-8') as data_file:
#     montreal_data = json.load(data_file)

# with open('./assets/data/projetpietonnisation2017.geojson',
#           encoding='utf-8') as data_file:
#     street_data = json.load(data_file)

# street_df = to_df(street_data)
# street_df = update_titles(street_df)
# street_df = sort_df(street_df)
# print(street_df.head())
# locations = get_neighborhoods(montreal_data)
# print(locations)