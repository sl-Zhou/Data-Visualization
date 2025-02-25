'''
    Contains some functions related to the creation of the heatmap.
'''
import plotly.express as px
import hover_template

def get_figure(data):
    '''
        Generates the heatmap from the given dataset.

        Make sure to set the title of the color bar to 'Trees'
        and to display each year as an x-tick. The x and y axes should
        be titled "Year" and "Neighborhood". 

        Args:
            data: The data to display
        Returns:
            The figure to be displayed.
    '''
    # Define axis labels and color bar title
    axis_labels = {'x': 'Year', 'y': 'Neighborhood', 'color': 'Trees'}
    
    # Initialize the heatmap with specified settings
    heatmap_fig = px.imshow(
        data,
        color_continuous_scale='Bluyl',
        labels=axis_labels
    )
    
    # Configure layout to disable dragging and set x-axis ticks
    heatmap_fig.update_layout(
        dragmode=False,
        xaxis={'tickmode': 'linear'}
    )
    
    # Apply custom hover template
    heatmap_fig.update_traces(
        hovertemplate=hover_template.get_heatmap_hover_template()
    )
    
    return heatmap_fig