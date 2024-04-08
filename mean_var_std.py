import numpy as np


def calculate(lista: list):

    if len(lista) != 9:
        raise ValueError("List must contain nine numbers.")
    numpy_array = np.array(lista).reshape(3, 3)
    mean = [numpy_array.mean(axis=0).tolist(), numpy_array.mean(
            axis=1).tolist(), numpy_array.mean().tolist()]
    variance = [numpy_array.var(axis=0).tolist(), numpy_array.var(
        axis=1).tolist(), numpy_array.var().tolist()]
    std = [numpy_array.std(axis=0).tolist(), numpy_array.std(
        axis=1).tolist(), numpy_array.std().tolist()]
    max = [numpy_array.max(axis=0).tolist(), numpy_array.max(
        axis=1).tolist(), numpy_array.max().tolist()]
    min = [numpy_array.min(axis=0).tolist(), numpy_array.min(
        axis=1).tolist(), numpy_array.min().tolist()]
    sum = [numpy_array.sum(axis=0).tolist(), numpy_array.sum(
        axis=1).tolist(), numpy_array.sum().tolist()]
    result = {'mean': mean, 'variance': variance,
              'standard deviation': std, 'max': max, 'min': min, 'sum': sum}
    return result
