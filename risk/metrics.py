import numpy as np


def compute_risk_metrics(terminal_prices: np.ndarray):
    """
    Compute basic risk statistics from terminal price distribution.
    """

    mean_price = np.mean(terminal_prices)
    std_dev = np.std(terminal_prices)

    var_95 = np.percentile(terminal_prices, 5)
    var_99 = np.percentile(terminal_prices, 1)

    cvar_95 = terminal_prices[terminal_prices <= var_95].mean()
    cvar_99 = terminal_prices[terminal_prices <= var_99].mean()

    prob_loss = np.mean(terminal_prices < mean_price)

    return {
        "Mean": mean_price,
        "Std Dev": std_dev,
        "VaR 95%": var_95,
        "VaR 99%": var_99,
        "CVaR 95%": cvar_95,
        "CVaR 99%": cvar_99,
        "Probability Below Mean": prob_loss
    }
