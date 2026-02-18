import matplotlib.pyplot as plt
import numpy as np


def plot_paths(time_grid, paths, n_display=20):
    plt.figure(figsize=(10, 6))
    for i in range(min(n_display, paths.shape[0])):
        plt.plot(time_grid, paths[i], alpha=0.6)

    plt.title("Simulated GBM Paths")
    plt.xlabel("Time")
    plt.ylabel("Stock Price")
    plt.tight_layout()


def plot_distribution(terminal_prices):
    plt.figure(figsize=(8, 5))
    plt.hist(terminal_prices, bins=50, density=True, alpha=0.7)
    plt.title("Terminal Price Distribution")
    plt.xlabel("Price")
    plt.ylabel("Density")
    plt.tight_layout()
    

def plot_convergence(S0, K, r, sigma, T, steps, max_paths=20000, step_size=1000):
    from models.gbm import simulate_gbm
    from pricing.monte_carlo import monte_carlo_price
    from pricing.black_scholes import black_scholes_price

    import numpy as np

    path_range = np.arange(step_size, max_paths + step_size, step_size)
    mc_estimates = []

    for n in path_range:
        _, paths = simulate_gbm(S0, r, sigma, T, steps, n)
        price = monte_carlo_price(paths, K, r, T, option_type="call")
        mc_estimates.append(price)

    bs_price = black_scholes_price(S0, K, r, sigma, T, "call")

    plt.figure(figsize=(8, 5))
    plt.plot(path_range, mc_estimates)
    plt.axhline(bs_price)
    plt.title("Monte Carlo Convergence")
    plt.xlabel("Number of Paths")
    plt.ylabel("Call Price Estimate")
    plt.tight_layout()
    
