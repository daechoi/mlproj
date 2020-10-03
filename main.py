import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2, 10)

fig, ax = plt.subplots()
# ax.plot(x, x, label='linear')
# ax.plot(x, x ** 2, label='quadratic')
# ax.plot(x, x ** 3, label='cubic')

ax.set_xlabel('x label')
ax.set_ylabel('y label')

ax.set_title('Simple Plot')
ax.legend()


def my_plotter(ax, data1, data2, param_dict):
    """
    A helper function to make a graph

    :param ax: Axes
        Axes to draw to
    :param data1: array
        The x data
    :param data2: array
        The y data

    :param param_dict:  dict
        Dictionary of kwargs to pass to ax.plot

    :return:
        out: list
            list of artists added
    """
    out = ax.plot(data1, data2, **param_dict)
    return out


data2 = np.random.rand(10, 1)

my_plotter(ax, x, data2, {'marker': 'x'})

plt.show()
