from service.thompson_sampling import BaseModel


def get_best_reward(model: BaseModel, n: int = 100):
    """
    Get best rewards for n predictions.
    Parameters
    ----------
    model : BaseModel
        The fitted model to do predictions with.
    n : int
        The number of iterations for prediction.

    Returns
    -------
    list
        The list of best rewards for each iteration

    """
    return [model.predict() for _ in range(n)]
