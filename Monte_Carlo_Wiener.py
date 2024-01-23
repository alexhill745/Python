import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    S_0 = 100
    S = S_0
    delta_S = 0
    sigma = 0.1 # 30% Volatility
    delta_T = 7 / 365 # 1 Week timeline
    mu = 0.05   # 15% Expected return
    a = mu * delta_T
    b = sigma * (delta_T**0.5)
    prices = []
    for i in range(1000):
        epsilon = np.random.normal(0, 1.0, None)
        delta_S = S*(a + (b*epsilon))
        S = delta_S + max(S, 0)
        prices.append(S)
    plt.plot(range(len(prices)), prices)
    plt.show()
