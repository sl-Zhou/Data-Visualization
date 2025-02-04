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

    mode = mode.lower()
    
    if mode not in MODES:
        raise ValueError(f"Invalid mode: {mode}. Mode must be one of {MODES}.")

    if mode == 'count':
        hover_template = f"""
        <span style="font-family: 'Verdana'; font-size: 24px; color: black;">
            {name}
        </span><br>
        <span style="font-size: 16px; color: #555555;">
            %{{y}} lines
        </span>
        """
    elif mode == 'percent':
        hover_template = f"""
        <span style="font-family: 'Grenze Gotish'; font-size: 24px; color: black;">
            {name}
        </span><br>
        <span style="font-size: 16px; color: #555555;">
            %{{y:.2f}}% of lines
        </span>
        """
    else:
        # This should never happen
        raise ValueError(f"Unhandled mode: {mode}")

    return hover_template
