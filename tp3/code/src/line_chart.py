'''
    Contains some functions related to the creation of the line chart.
'''
import plotly.express as px
import hover_template

from template import THEME


def get_empty_figure():
    '''
        Returns the figure to display when there is no data to show.

        The text to display is : 'No data to display. Select a cell
        in the heatmap for more information.

    '''

    # TODO : Construct the empty figure to display. Make sure to 
    # set dragmode=False in the layout.
    # Create a blank figure with specified layout
    fig = px.scatter()  # Use scatter as a base for an empty figure
    
    # Add informational text
    fig.add_annotation(
        x=0.5,
        y=0.5,
        text="No data to display. Select a cell in the heatmap for more information.",
        showarrow=False,
        font=dict(
                    family=THEME['font_family'],
                    size=14,
                    color=THEME['dark_color']
                )
    )
    # Hide the axes and tick labels
    fig.update_xaxes(visible=False, showticklabels=False)
    fig.update_yaxes(visible=False, showticklabels=False)

    # Set layout to disable drag mode
    fig.update_layout(
        dragmode=False,
        paper_bgcolor=THEME['background_color'],
        plot_bgcolor=THEME['background_color']
    )
    
    return fig


def add_rectangle_shape(fig):
    '''
        Adds a rectangle to the figure displayed
        behind the informational text. The color
        is the 'pale_color' in the THEME dictionary.

        The rectangle's width takes up the entire
        paper of the figure. The height goes from
        0.25% to 0.75% the height of the figure.
    '''
    # TODO : Draw the rectangle
    fig.add_shape(
        type="rect",
        x0=0, x1=1,
        y0=0.25, y1=0.75,
        xref="paper", yref="paper",
        fillcolor=THEME['pale_color'],  # Use the pale color from THEME
        opacity=0.5,
        layer="below",  # Ensure it stays behind the text
        line=dict(width=0)
    )
    
    return fig


def get_figure(line_data, arrond, year):
    '''
        Generates the line chart using the given data.

        The ticks must show the zero-padded day and
        abbreviated month. The y-axis title should be 'Trees'
        and the title should indicated the displayed
        neighborhood and year.

        In the case that there is only one data point,
        the trace should be displayed as a single
        point instead of a line.

        Args:
            line_data: The data to display in the
            line chart
            arrond: The selected neighborhood
            year: The selected year
        Returns:
            The figure to be displayed
    '''
    # TODO : Construct the required figure. Don't forget to include the hover template
    # Check if line_data is empty or has no valid data
    if line_data.empty or line_data['Counts'].sum() == 0:
        return get_empty_figure()  # Return empty figure if no data
    
    if len(line_data) == 1:
        # If only one data point, use scatter to show a single point
        fig = px.scatter(
            x=line_data.Date_Plantation,
            y=line_data.Counts,
            title=f"Trees planted in {arrond} in {year}",
            labels={'y': 'Trees'},
            color_discrete_sequence=['black']
        )
    else:
        # If multiple points, use line chart
        data = line_data.sort_values(by="Date_Plantation")
        fig = px.line(
            x=data.Date_Plantation,
            y=data.Counts,
            title=f"Trees planted in {arrond} in {year}",
            labels={'y': 'Trees'}
        )
        fig.update_traces(line_color='black')

    fig.update_layout(
        xaxis=dict(
            tickformat="%d %b",  # Format x-axis ticks to show day and abbreviated month
            title=''  # No x-axis title
        ),
        dragmode=False
    )
    
    # Apply custom hover template
    fig.update_traces(
        hovertemplate=hover_template.get_linechart_hover_template()  # Use the specified hover template
    )
    
    return fig
