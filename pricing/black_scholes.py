import numpy as np
from scipy.stats import norm


def black_scholes_price(S0: float,
                        K: float,
                        r: float,
                        sigma: float,
                        T: float,
                        option_type: str = "call"):
    """
    Black-Scholes analytical option pricing formula.
    """

    d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == "call":
        price = S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S0 * norm.cdf(-d1)
    else:
        raise ValueError("option_type must be 'call' or 'put'")

    return price
