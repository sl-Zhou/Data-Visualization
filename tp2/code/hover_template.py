'''
    Provides the template for the hover tooltips.
'''
from modes import MODES


def get_hover_template(name, mode):
    '''
        Sets the template for the hover tooltips.

        The template contains:
            * A title stating player name with:
                - Font family: Grenze Gotish
                - Font size: 24px
                - Font color: Black
            * The number of lines spoken by the player, formatted as:
                - The number of lines if the mode is 'Count ("X lines").
                - The percent of lines fomatted with two
                    decimal points followed by a '%' symbol
                    if the mode is 'Percent' ("Y% of lines").

        Args:
            name: The hovered element's player's name
            mode: The current display mode
        Returns:
            The hover template with the elements descibed above
    '''
    # TODO: Generate and return the over template

    # Lowercase the mode for consistency
    mode = mode.lower()

    # Base template for player name
    template = '<span style="font-family: Grenze Gotisch; font-size: 24px; color: black;">{}</span><br>'.format(name)

    # Add the lines information based on mode
    if mode == 'count':
        # Use %{y} for y-axis values
        template += '%{y} lines<extra></extra>'
    elif mode == 'percent':
        # Format percentage with two decimal points
        template += '%{y:.2f}% of lines<extra></extra>'
    else:
        raise ValueError(f"Invalid mode '{mode}'. Mode should be 'count' or 'percent'.")

    return template
