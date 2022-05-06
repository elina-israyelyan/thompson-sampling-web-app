import pandas as pd


class DataPreProcessing:
    def __init__(self, processing_steps: list = None, make_binary_kwargs: dict = None):
        self.processing_steps = processing_steps
        self.make_binary_kwargs = make_binary_kwargs

    def preprocess(self, data):
        """
        Preprocess data with the steps given in model instantiation.
        Parameters
        ----------
        data : pandas.DataFrame
           Data to preprocess.
        Returns
        -------
        pandas.DataFrame
           Preprocessed dataframe.
        """
        for method_name in self.processing_steps:
            method = getattr(self, method_name)
            data = method(data)
        return data

    def make_binary(self, data: pd.DataFrame):
        """
        Make data binary based on threshold given in model instantiation
        Parameters
        ----------
        data : pandas.DataFrame
            Data to transform
        Returns
        -------
        pandas.DataFrame
            Transformed dataframe.
        """
        data = data.transform(lambda x: x > self.make_binary_kwargs["threshold"])
        data.replace({False: 0, True: 1}, inplace=True)
        return data

