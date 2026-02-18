import numpy as np


def simulate_gbm(S0: float,
                 r: float,
                 sigma: float,
                 T: float,
                 steps: int,
                 n_paths: int):
    """
    Simulate stock price paths using Geometric Brownian Motion (GBM).

    dS = rS dt + sigma S dW

    Parameters
    ----------
    S0 : float
        Initial stock price
    r : float
        Risk-free rate
    sigma : float
        Volatility
    T : float
        Time horizon (years)
    steps : int
        Number of time steps
    n_paths : int
        Number of simulated paths

    Returns
    -------
    time_grid : np.ndarray
        Time points
    paths : np.ndarray
        Simulated price paths (n_paths x steps+1)
    """

    dt = T / steps
    time_grid = np.linspace(0, T, steps + 1)

    # Generate random normal shocks
    Z = np.random.standard_normal((n_paths, steps))

    # Drift and diffusion components
    drift = (r - 0.5 * sigma**2) * dt
    diffusion = sigma * np.sqrt(dt) * Z

    # Log returns
    log_returns = drift + diffusion

    # Cumulative sum for log price evolution
    log_price_paths = np.cumsum(log_returns, axis=1)

    # Insert initial price
    log_price_paths = np.hstack(
        (np.zeros((n_paths, 1)), log_price_paths)
    )

    paths = S0 * np.exp(log_price_paths)

    return time_grid, paths
