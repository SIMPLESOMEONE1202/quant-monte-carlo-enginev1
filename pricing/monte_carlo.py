import numpy as np


def monte_carlo_price(paths: np.ndarray,
                      K: float,
                      r: float,
                      T: float,
                      option_type: str = "call",
                      return_ci: bool = False):
    """
    Monte Carlo option pricing with optional confidence interval.
    """

    terminal_prices = paths[:, -1]

    if option_type == "call":
        payoff = np.maximum(terminal_prices - K, 0)
    elif option_type == "put":
        payoff = np.maximum(K - terminal_prices, 0)
    else:
        raise ValueError("option_type must be 'call' or 'put'")

    discounted_payoff = np.exp(-r * T) * payoff

    price = np.mean(discounted_payoff)

    if return_ci:
        std_error = np.std(discounted_payoff, ddof=1) / np.sqrt(len(discounted_payoff))
        ci_low = price - 1.96 * std_error
        ci_high = price + 1.96 * std_error
        return price, std_error, ci_low, ci_high

    return price
