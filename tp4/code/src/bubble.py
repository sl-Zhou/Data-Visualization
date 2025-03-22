'''
    This file contains the code for the bubble plot.
'''

import plotly.express as px


def get_plot(my_df, gdp_range, co2_range):
    '''
        Generates the bubble plot.

        The x and y axes are log scaled, and there is
        an animation between the data for years 2000 and 2015.

        The discrete color scale (sequence) to use is Set1 (see : https://plotly.com/python/discrete-color/)

        The markers' maximum size is 30 and their minimum
        size is 6.

        Args:
            my_df: The dataframe to display
            gdp_range: The range for the x axis
            co2_range: The range for the y axis
        Returns:
            The generated figure
    '''
    # TODO : Define figure with animation
    # ✅ Création de la figure avec animation
    fig = px.scatter(my_df, x='GDP', y='CO2', animation_frame= 'Year', animation_group='Country Name',
                     size= 'Population', color='Continent', hover_name='Country Name', log_x= True, log_y= True,
                     range_x= gdp_range, range_y= co2_range, color_discrete_sequence= px.colors.qualitative.Set1,
                     size_max= 30)
    
    # ✅ Appliquer `sizemin` via `update_traces()`
    fig.update_traces(marker=dict(sizemin=6))

    # ✅ Effacer le menu d'animation par défaut
    if hasattr(fig.layout, 'updatemenus'):
        fig.layout.updatemenus = None
    
    return fig


def update_animation_hover_template(fig):
    '''
        Sets the hover template of the figure,
        as well as the hover template of each
        trace of each animation frame of the figure

        Args:
            fig: The figure to update
        Returns:
            The updated figure
    '''

    # TODO : Set the hover template
     # ✅ Définition du hover template personnalisé
    hover_template = (
        "<b>Country:</b> %{hovertext}<br>"
        "<b>Population:</b> %{marker.size}<br>"
        "<b>GDP:</b> %{x:,.2f} $ (USD)<br>"
        "<b>CO₂ emissions:</b> %{y:.1f} metric tonnes<br>"
    )

    # ✅ Appliquer le hover template à toutes les traces principales
    for trace in fig.data:
        trace.hovertemplate = hover_template

    # ✅ Appliquer le hover template aux frames de l'animation
    for frame in fig.frames:
        for trace in frame.data:
            trace.hovertemplate = hover_template

    return fig  # Retourne la figure mise à jour


def update_animation_menu(fig):
    '''
        Updates the animation menu to show the current year 
        and removes the unnecessary 'Stop' button.

        Args:
            fig: The figure containing the menu to update
        Returns:
            The updated figure
    '''
    # Clear existing updatemenus to avoid duplicates
    if hasattr(fig.layout, 'updatemenus'):
        fig.layout.updatemenus = None

    # ✅ Définition du menu d'animation avec UN SEUL bouton "Animate"
    updatemenus = [{
        "buttons": [
            {
                "args": [None, {"frame": {"duration": 1000, "redraw": True},
                                "fromcurrent": True, "transition": {"duration": 300, "easing": "cubic-in-out"}}],
                "label": "Animate",
                "method": "animate"
            }
        ],
        "direction": "left",
        "pad": {"r": 10, "t": 50},
        "showactive": False,
        "type": "buttons",
        "x": 0.1,
        "xanchor": "right",
        "y": -0.235,
        "yanchor": "top",
        "bgcolor": "white",
        "bordercolor": "lightgray",
        "borderwidth": 1
    }]

    # ✅ Définition du slider (inclus dans le même update_layout)
    sliders = [{
        "active": 0,
        "yanchor": "top",
        "xanchor": "left",
        "currentvalue": {
            "font": {"size": 14},
            "prefix": "Data for year: ",  # ✅ Affichage de l'année sélectionnée
            "visible": True,
            "xanchor": "left"
        },
        "transition": {"duration": 300},
        "pad": {"b": 10, "t": 50},
        "len": 0.9,
        "x": 0.1,
        "y": -0.2,  # ✅ Ajustement pour aligner correctement le slider
        "steps": [
            {
                "args": [[frame.name], 
                         {"frame": {"duration": 500, "redraw": True},
                          "mode": "immediate"}],
                "label": frame.name,  # ✅ Chaque step correspond à une année
                "method": "animate"
            }
            for frame in fig.frames  # ✅ Récupération des frames pour le slider
        ]
    }]

    # ✅ Un SEUL `update_layout()` qui met à jour les boutons ET le slider
    fig.update_layout(updatemenus=updatemenus, sliders=sliders)

    return fig  # Retourne la figure mise à jour



def update_axes_labels(fig):
    '''
        Updates the axes labels with their corresponding titles.

        Args:
            fig: The figure to be updated
        Returns:
            The updated figure
    '''
    # TODO : Update labels
    # ✅ Mise à jour des titres des axes
    fig.update_layout(xaxis_title='GDP per capita ($USD)',
                      yaxis_title='CO2 emissions (metric tonnes)')
    
    return fig  # Retourne la figure mise à jour


def update_template(fig):
    '''
        Updates the layout of the figure, setting
        its template to 'simple_white'

        Args:
            fig: The figure to update
        Returns
            The updated figure
    '''
    # TODO : Update template
    fig.update_layout(template='simple_white',
                      plot_bgcolor= "white") # Mise à jour du template
    
    return fig  # Retourne la figure mise à jour


def update_legend(fig):
    '''
        Updated the legend title

        Args:
            fig: The figure to be updated
        Returns:
            The updated figure
    '''
    # TODO : Update legend
    fig.update_layout(
        legend_title_text="Legend",  # ✅ Ajoute un titre clair
        legend=dict(
            orientation="v",  # ✅ Mode VERTICAL (au lieu de "h" pour horizontal)
            x=1.02,  # ✅ Positionne à droite du graphique
            y=1,  # ✅ Aligné en haut
            xanchor="left",  # ✅ S'ancre à gauche de la légende
            yanchor="top",  # ✅ S'ancre en haut
            bgcolor="rgba(255, 255, 255, 0.5)",  # ✅ Fond semi-transparent pour lisibilité
            bordercolor="gray",  # ✅ Bordure grise discrète
            borderwidth=1  # ✅ Bordure fine
        )
    )
    return fig  # Retourne la figure mise à jour