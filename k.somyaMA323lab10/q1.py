import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
import cufflinks as cf
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

for i in range(10):
    mu = 1
    n = 100
    dt = 0.01
    x0 = 1
    # np.random.seed(1)

    sigma = 0.8

    x = np.exp(
        (mu - sigma ** 2 / 2) * dt
        + sigma * np.random.normal(0, np.sqrt(dt), size=(1, n)).T
    )
    x = np.vstack([np.ones(1), x])
    x = x0 * x.cumprod(axis=0)

    # plt.figure(figsize=(20,10))
    plt.plot(x)
    # plt.legend(np.round(sigma, 2))
    # plt.xlabel("$t$")
    # plt.ylabel("$x$")
plt.title(
        "Realizations of Geometric Brownian Motion with different variances\n $\mu=1$ $\sigma=0.8$"
    )
plt.show()

for i in range(10):
    mu = -1
    n = 100
    dt = 0.01
    x0 = 1
    # np.random.seed(1)

    sigma = 0.8

    x = np.exp(
        (mu - sigma ** 2 / 2) * dt
        + sigma * np.random.normal(0, np.sqrt(dt), size=(1, n)).T
    )
    x = np.vstack([np.ones(1), x])
    x = x0 * x.cumprod(axis=0)

    # plt.figure(figsize=(20,10))
    plt.plot(x)
    # plt.legend(np.round(sigma, 2))
    # plt.xlabel("$t$")
    # plt.ylabel("$x$")
plt.title(
        "Realizations of Geometric Brownian Motion with different variances\n $\mu=-1$ $\sigma=0.8$"
    )
plt.show()

for i in range(10):
    mu = 1
    n = 100
    dt = 0.01
    x0 = 1
    # np.random.seed(1)

    sigma = 2.8

    x = np.exp(
        (mu - sigma ** 2 / 2) * dt
        + sigma * np.random.normal(0, np.sqrt(dt), size=(1, n)).T
    )
    x = np.vstack([np.ones(1), x])
    x = x0 * x.cumprod(axis=0)

    # plt.figure(figsize=(20,10))
    plt.plot(x)
    # plt.legend(np.round(sigma, 2))
    # plt.xlabel("$t$")
    # plt.ylabel("$x$")
plt.title(
        "Realizations of Geometric Brownian Motion with different variances\n $\mu=1$ $\sigma=2.8$"
    )
plt.show()

for i in range(10):
    mu = -1
    n = 100
    dt = 0.01
    x0 = 1
    # np.random.seed(1)

    sigma = 2.8

    x = np.exp(
        (mu - sigma ** 2 / 2) * dt
        + sigma * np.random.normal(0, np.sqrt(dt), size=(1, n)).T
    )
    x = np.vstack([np.ones(1), x])
    x = x0 * x.cumprod(axis=0)

    # plt.figure(figsize=(20,10))
    plt.plot(x)
    # plt.legend(np.round(sigma, 2))
    # plt.xlabel("$t$")
    # plt.ylabel("$x$")
plt.title(
        "Realizations of Geometric Brownian Motion with different variances\n $\mu=-1$ $\sigma=2.8$"
    )
plt.show()