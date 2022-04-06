import random

import pandas as pd
import plotly.graph_objects as go

from service.thompson_sampling.model import ThompsonSampling
from utils.data_visualisation import plot_dynamic_betas


def model_beta_visualisation():
    data = {}
    data['B1'] = [random.randint(0, 1) for x in range(50)] + [1] * 50 +[0]*50
    data['B2'] = [random.randint(0, 1) for x in range(50)] + [0] * 100
    data['B3'] = [random.randint(0, 1) for x in range(150)]
    model = ThompsonSampling()
    data = pd.DataFrame(data)
    a_b_lists = {k: [] for k in data.keys()}
    for i in range(len(data)):
        model.fit(data.iloc[[i]])
        for j in range(len(list(data.columns))):
            a_b_lists[model.arm_labels[j]].append(model.arm_reward_probas[j])
    fig_1 = go.FigureWidget(plot_dynamic_betas(a_b_lists))
    predicts_best = []
    for i in range(100):
        predicts_best.append(model.predict())
    fig_2 = go.Figure(data=[go.Histogram(x=predicts_best)])
    fig_2.show()
    fig_1.show()
