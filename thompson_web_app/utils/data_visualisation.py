import random

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from scipy.stats import beta


def get_dist_params(model=None, data: pd.DataFrame = None, exploration_time: int = 10):
    """
    Dynamic plot for plotting beta distributions for a,b values given in a_b_lists.
    Parameters
    ----------
    model: ThompsonSampling
        The model of the distribution.
    data : dict
        Each column is the label of one choice for which the distributions will be calculated over time.
        Each row represents a single timestamp.
    exploration_time: int
        The exploration time used for fitting the model.
    Returns
    -------
    dict
        Each key represents the label name and the values are arrays, each index having
        the distribution parameters of one timestamp.
    """
    dist_params = {k: [] for k in data.columns}
    exploration_time = exploration_time
    for i in range(len(data)):  # fitting data by each timestamp one by one
        if i == 0:
            model.fit(data.iloc[[i]], prefit=False,
                      exploration_time=exploration_time)  # if first time make sure its not prefit
        else:
            model.fit(data.iloc[[i]], prefit=True, exploration_time=exploration_time)
        if i % exploration_time == 0:
            for j in range(len(list(data.columns))):
                dist_params[model.arm_labels[j]].append(model.arm_reward_probas[j])  # getting distribution parameters
    return dist_params


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
        hexadecimal = ["#" + ''.join([random.choice('ABCDEF0123456789') for i in range(6)])][0]  # apply random color
        for a, b in a_b_list:
            beta_new = beta(a, b)  # getting the distribution with current a,b parameters for beta distribution
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
    )]  # make the slider

    fig.update_layout(
        sliders=sliders
    )

    return fig
