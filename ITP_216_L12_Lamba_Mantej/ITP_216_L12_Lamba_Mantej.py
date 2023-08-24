import numpy as np
import matplotlib.pyplot as plt


def main():
    x = np.arange(-np.pi, np.pi, 0.1)
    y = np.sin(x)
    y2 = np.cos(x)
    y3 = np.tan(x)
    y4 = np.sinh(x)
    y5 = np.cosh(x)
    y6 = np.tanh(x)
    # 2 row, 3 columns
    fig, ax = plt.subplots(2, 3)
    ax[0, 0].plot(x, y)
    ax[0, 0].set(title='sin x', xlabel='x', ylabel='y')
    ax[0, 1].plot(x, y2)
    ax[0, 1].set(title='cos x', xlabel='x', ylabel='y')
    ax[0, 2].plot(x, y3)
    ax[0, 2].set(title='tan x', xlabel='x', ylabel='y')
    ax[1, 0].plot(x, y4)
    ax[1, 0].set(title='sinh x', xlabel='x', ylabel='y')
    ax[1, 1].plot(x, y5)
    ax[1, 1].set(title='cosh x', xlabel='x', ylabel='y')
    ax[1, 2].plot(x, y6)
    ax[1, 2].set(title='tanh x', xlabel='x', ylabel='y')
    fig.suptitle("Trig!")
    fig.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
