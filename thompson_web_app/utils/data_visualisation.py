import random

import numpy as np
import plotly.graph_objects as go
from scipy.stats import beta


def plot_dynamic_betas(a_b_lists: dict):
    """
    Dynamic plot for plotting beta distributions for a,b values given in a_b_lists.
    Parameters
    ----------
    a_b_lists : dict
        Each key is the label of one choice for which the beta distributions will be plotted.
        Each row represents a timestamp.

    Returns
    -------
    plotly.graph_objects.Figure()
        The figure that combines all the beta distributions over time, for different labels.
    """
    fig = go.Figure()
    for label_name, a_b_list in a_b_lists.items():
        hexadecimal = ["#" + ''.join([random.choice('ABCDEF0123456789') for i in range(6)])][0]
        for a, b in a_b_list:
            beta_new = beta(a, b)
            fig.add_trace(go.Scatter(visible=False,
                                     line=dict(color=hexadecimal, width=6),
                                     name=label_name,
                                     x=np.linspace(0, 1, 100),
                                     y=beta_new.pdf(np.linspace(0, 1, 100))))

    # Create and add slider
    steps = []
    for i in range(round(len(fig.data) / len(a_b_lists.keys()))):
        step = dict(
            method="update",
            args=[{"visible": [False] * len(fig.data)},
                  {"title": "Beta distribution switched to timestamp: " + str(i)}],  # layout attribute
        )
        for j in range(len(a_b_lists.keys())):  # to get the traces of the same timestamp (that's why we use i+j*len)
            step["args"][0]["visible"][
                i + j * len(list(a_b_lists.values())[0])] = True  # make the trace visible
        steps.append(step)

    sliders = [dict(
        active=0,
        currentvalue={"prefix": "Timestamp: "},
        pad={"t": 100},
        steps=steps
    )]

    fig.update_layout(
        sliders=sliders
    )

    return fig
