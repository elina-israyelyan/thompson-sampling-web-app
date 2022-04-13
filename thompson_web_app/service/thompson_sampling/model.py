import pickle

import numpy as np
import pandas as pd

from service.thompson_sampling.base import BaseModel


class ThompsonSampling(BaseModel):
    def __init__(self):
        self.arm_reward_probas = None
        self.penalties = []
        self.arm_labels = []

    @property
    def arm_labels(self):
        return self._arm_labels

    @arm_labels.setter
    def arm_labels(self, arm_labels):
        self.arm_reward_probas = [(1, 1)] * len(arm_labels)
        self.penalties = [0] * len(arm_labels)
        self._arm_labels = arm_labels

    def fit(self, data: pd.DataFrame, prefit: bool = True):
        """
        Method to fit the data to the Binomial Thompson Sampling model
        Parameters
        ----------
        data : pandas.DataFrame
            Data to fit the model.
        prefit : bool
            If True use the previous, trained  parameters of beta distribution for each arm.
        Returns
        -------
        None
        """
        if not self.arm_labels or not prefit:
            self.arm_labels = data.columns.tolist()
        for i in range(len(data)):
            best_arm_label = self.predict()
            best_arm = self.arm_labels.index(best_arm_label)
            try:
                is_reward = data[best_arm_label].tolist()[i]
            except KeyError:
                print("best arm selected was not in the new data, "
                      "so we dont know if there is a reward or not")
                continue
            if is_reward == 1 or is_reward == 0:
                self.penalties[best_arm] += 1 - is_reward
                a, b = self.arm_reward_probas[best_arm]
                self.arm_reward_probas[best_arm] = (a + is_reward, b + 1 - is_reward)

    def predict(self):
        """
        Predict which arm is the most reward bringing at current time.
        Returns
        -------
        str
            The name of the arm which gave the most probability to have a reward.
        """
        max_proba = -1
        best_arm = -1
        for arm in range(len(self.arm_labels)):
            a, b = self.arm_reward_probas[arm]
            arm_reward_proba = np.random.beta(a, b)
            if arm_reward_proba > max_proba:
                max_proba = arm_reward_proba
                best_arm = arm
        return self.arm_labels[best_arm]

    def predict_proba(self):
        """
        Predict which arm is the most reward bringing at current time.
        Returns
        -------
        str
           The name of the arm which gave the most probability to have a reward.
        """
        max_proba = -1
        best_arm = -1
        for arm in range(len(self.arm_labels)):
            a, b = self.arm_reward_probas[arm]
            arm_reward_proba = np.random.beta(a, b)
            if arm_reward_proba > max_proba:
                max_proba = arm_reward_proba
                best_arm = arm
        return self.arm_labels[best_arm], max_proba

    def save_model(self, save_path: str = "./", version: str = "latest"):
        """
        Save the model parameters in the mentioned path.
        Parameters
        ----------
        save_path : str
            Path where the model needs to be saved.
        version : str
            The version suffix which will be added to the model path.

        Returns
        -------
        None
            Saves the model in the save_path.

        """
        with open(save_path + "model_" + version, 'wb') as f:
            pickle.dump({
                "arm_reward_probas": self.arm_reward_probas,
                "arm_labels": self.arm_labels,
                "penalties": self.penalties}, f, protocol=pickle.HIGHEST_PROTOCOL)

    def load_model(self, load_path: str = "./", version: str = "latest"):
        """
        Load model from the mentioned path.
        Parameters
        ----------
        load_path : str
            Path from which the model should be loaded.
        version : str
            The version of the model which should be loaded.

        Returns
        -------
        None
            Loads the parameters of the model from the path.
        """
        with open(load_path + "model_" + version, 'rb') as f:
            model = pickle.load(f)
        self.arm_reward_probas, self.arm_labels, self.penalties = (model["arm_reward_probas"],
                                                                   model["arm_labels"],
                                                                   model["penalties"])