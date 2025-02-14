'''
    Contains some functions related to the creation of the bar chart.
    The bar chart displays the data either as counts or as percentages.
'''

import plotly.graph_objects as go
import plotly.io as pio

from hover_template import get_hover_template
from modes import MODES, MODE_TO_COLUMN
from template import THEME, create_template

def init_figure():
    '''
        Initializes the Graph Object figure used to display the bar chart.
        Sets the template to be used to "simple_white" as a base with
        our custom template on top. Sets the title to 'Lines per act'

        Returns:
            fig: The figure which will display the bar chart
    '''
    fig = go.Figure()

    # TODO : Update the template to include the new theme and set the title
    create_template()
    fig.update_layout(
        template="simple_white+custom_theme",
        dragmode=False,
        barmode='relative',
        title=dict(
            text='Lines per Act',
            x=0,
            xanchor='left'
        )
    )

    return fig


def draw(fig, data, mode):
    '''
        Draws the bar chart.

        Arg:
            fig: The figure comprising the bar chart
            data: The data to be displayed
            mode: Whether to display the count or percent data.
        Returns:
            fig: The figure comprising the drawn bar chart
    '''
    fig = go.Figure(fig)  # conversion back to Graph Object
    # TODO : Update the figure's data according to the selected mode

    fig.data = []

    # Validate the mode
    if mode not in MODES:
        raise ValueError(f"Invalid mode. Choose '{MODES['count']}' or '{MODES['percent']}'.")

    # Use MODE_TO_COLUMN to get the correct column name
    value_column = MODE_TO_COLUMN[MODES[mode]]
    yaxis_title = 'Line Count' if mode == 'count' else 'Line Percentage (%)'

    # Get the sorted list of players
    sorted_players = sorted(data['Player'].unique())

    # Add a bar trace for each player
    for player in sorted_players:
        player_data = data[data['Player'] == player]
        fig.add_trace(
            go.Bar(
                x=player_data['Act'],
                y=player_data[value_column],
                name=player,
                hovertemplate=get_hover_template(player, mode)
        )
    )

    # Update layout
    fig.update_layout(
        title=dict(
            text='Lines per Act',
            x=0,
            xanchor='left'
        ),
        xaxis=dict(
            tickvals=[1, 2, 3, 4, 5],
            ticktext=['Act 1', 'Act 2', 'Act 3', 'Act 4', 'Act 5']
        ),
        yaxis_title=yaxis_title,
        barmode='stack',
        legend = dict(traceorder='normal')
    )

    return fig

def update_y_axis(fig, mode):
    '''
        Updates the y axis to say 'Lines (%)' or 'Lines (Count) depending on
        the current display.

        Args:
            mode: Current display mode
        Returns: 
            The updated figure
    '''
    # TODO : Update the y axis title according to the current mode
    if mode == 'count':
        yaxis_title = 'Lines (Count)'
    elif mode == 'percent':
        yaxis_title = 'Lines (%)'
    else:
        raise ValueError(f"Invalid")

    fig.update_layout(yaxis_title=yaxis_title)
    return fig