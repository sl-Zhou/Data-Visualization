'''
    Provides the template for the tooltips.
'''


def get_bubble_hover_template():
    '''
        Sets the template for the hover tooltips.
        
        Contains four labels, followed by their corresponding
        value and units where appropriate, separated by a
        colon : country, population, GDP and CO2 emissions.

        The labels' font is bold and the values are normal weight

        returns:
            The content of the tooltip
    '''
    # TODO : Generate tooltip

    hover_template = (
        "<b>Country:</b> %{hovertext}<br>"
        "<b>Population:</b> %{marker.size:,}M<br>"
        "<b>GDP:</b> %{x:,.0f} USD<br>"
        "<b>CO₂ Emissions:</b> %{y:.2f} metric tonnes<br>"
        "Year: %{animation_frame}<extra></extra>"
    )

    return hover_template
