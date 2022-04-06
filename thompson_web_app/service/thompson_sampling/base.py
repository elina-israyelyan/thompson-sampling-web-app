class BaseModel:
    def __init__(self):
        pass

    def predict(self, data):
        """
        Get prediction on the data.

        Parameters
        ----------
        data : optional
            Data on which prediction should be done.

        Returns
        -------
        None

        """
        pass

    def predict_proba(self, data):
        """
        Get probabilities of prediction for the data.
        Parameters
        ----------
        data : optional
            Data on which prediction should be done.
        Returns
        -------
        None
        """
        pass

    def fit(self, data):
        """
        Method to fit the data to the model.
        Parameters
        ----------
        data : optional
            Data which the model should fit to.

        Returns
        -------
        None
        """
        pass

    def save_model(self, save_path):
        """
        Method to save the model to the path provided.
        Parameters
        ----------
        save_path : str
            Path where the model should be saved

        Returns
        -------
        None
        """
        pass

    def load_model(self, load_path):
        """
        Method to load the model from the given path.
        Parameters
        ----------
        load_path : str
            Path of the model which should be loaded for the current instance.

        Returns
        -------
        None

        """
        pass
