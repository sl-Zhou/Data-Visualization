'''
    Contains the functions to set up the map visualization.

'''

import plotly.graph_objects as go
import plotly.express as px

import hover_template as hover


def add_choro_trace(fig, montreal_data, locations, z_vals, colorscale):
    '''
        Adds the choropleth trace, representing Montreal's neighborhoods.

        Note: The z values and colorscale provided ensure every neighborhood
        will be grey in color. Although the trace is defined using Plotly's
        choropleth features, we are simply defining our base map.

        The opacity of the map background color should be 0.2.

        Args:
            fig: The figure to add the choropleth trace to
            montreal_data: The data used for the trace
            locations: The locations (neighborhoods) to show on the trace
            z_vals: The table to use for the choropleth's z values
            colorscale: The table to use for the choropleth's color scale
        Returns:
            fig: The updated figure with the choropleth trace

    '''
    # TODO : Draw the map base
    choropleth_trace = go.Choroplethmapbox(
        geojson=montreal_data,
        locations=locations,
        customdata=locations,
        z=z_vals,
        marker=dict(opacity=0.4, line=dict(width=0.9)),  # set the opacity of the map background color
        colorscale=colorscale,  # set the color of the map
        featureidkey="properties.NOM",
        name=montreal_data.get('name', ''),
        below="",
        showscale=False,  # remove scale bar
        hovertemplate=hover.map_base_hover_template(),  # apply hover template for the base map
        )
    
    fig.add_trace(choropleth_trace)

    return fig


def add_scatter_traces(fig, street_df):
    '''
        Adds the scatter trace, representing Montreal's pedestrian paths.

        The marker size should be 20.

        Args:
            fig: The figure to add the scatter trace to
            street_df: The dataframe containing the information on the
                pedestrian paths to display
        Returns:
            The figure now containing the scatter trace

    '''
    # TODO : Add the scatter markers to the map base

    temp_fig = px.scatter_mapbox(
        street_df,
        lat="properties.LATITUDE",
        lon="properties.LONGITUDE",
        color="properties.TYPE_SITE_INTERVENTION",
        opacity=1,
        zoom=11,
        # defining custom data for hover template and for the panel information
        custom_data=[
            "properties.NOM_PROJET", 
            "properties.OBJECTIF_THEMATIQUE",
            "properties.MODE_IMPLANTATION", 
            "properties.TYPE_SITE_INTERVENTION"
        ]
    )
    temp_fig.update_traces(
        marker=dict(size=20),
        hovertemplate=hover.map_marker_hover_template('%{customdata[3]}') # set hover template of the markers
    )

    for trace in temp_fig.data:
        fig.add_trace(trace)

    return fig
