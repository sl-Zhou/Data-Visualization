'''
    This file contains the functions to call when
    a click is detected on the map, depending on the context
'''
import dash_html_components as html


def no_clicks(style):
    '''
        Deals with the case where the map was not clicked

        Args:
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    # TODO : Handle no clicks on the map
    # Check if the panel is already hidden
    if style and style.get('visibility') == 'hidden':
        # If already hidden, maintain current state
        return None, None, None, style
    
    return None, None, None, None


def map_base_clicked(title, mode, theme, style):
    '''
        Deals with the case where the map base is
        clicked (but not a marker)

        Args:
            title: The current display title
            mode: The current display title
            theme: The current display theme
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    # TODO : Handle clicks on the map base
    # Check current panel state
    if style and style.get('visibility') == 'hidden':
        # If panel is hidden, keep it hidden
        return None, None, None, style
    
    return title, mode, theme, style


def map_marker_clicked(figure, curve, point, title, mode, theme, style): # noqa : E501 pylint: disable=unused-argument too-many-arguments line-too-long
    '''
        Deals with the case where a marker is clicked

        Args:
            figure: The current figure
            curve: The index of the curve containing the clicked marker
            point: The index of the clicked marker
            title: The current display title
            mode: The current display title
            theme: The current display theme
            style: The current display style for the panel
        Returns:
            title: The updated display title
            mode: The updated display title
            theme: The updated display theme
            style: The updated display style for the panel
    '''
    # TODO : Handle clicks on the markers
    # Set panel style to visible with border and padding
    panel_style = {'visibility': 'visible', 'border': '1px solid black', 'padding': '10px'}

    # Extract data from the clicked marker
    marker_data = figure['data'][curve]['customdata'][point]
    marker_color = figure['data'][curve]['marker']['color']
    
    # Set title - project name with marker color
    project_name = marker_data[0]
    title_element = [html.Span(project_name, style={'color': marker_color})]
    
    # Set mode - implementation method
    implementation_mode = marker_data[2]
    mode_element = [html.Span(implementation_mode), html.Span("\n")]
    
    # Set theme - displayed as a list if available
    thematic_objective = marker_data[1]
    if thematic_objective:
        theme_items = thematic_objective.split('\n')
        theme_element = [
            html.Span("Thématique:"),
            html.Ul(children=[html.Li(item) for item in theme_items if item.strip()])
        ]
    else:
        theme_element = None

    return title_element, mode_element, theme_element, panel_style
