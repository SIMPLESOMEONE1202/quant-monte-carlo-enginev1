import argparse
import logging
import numpy as np

from models.gbm import simulate_gbm
from pricing.monte_carlo import monte_carlo_price
from pricing.black_scholes import black_scholes_price
from risk.metrics import compute_risk_metrics
from visualization.plots import plot_convergence, plot_paths, plot_distribution





def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Quantitative Monte Carlo Option Pricing Engine"
    )

    parser.add_argument("--S0", type=float, default=100.0, help="Initial stock price")
    parser.add_argument("--K", type=float, default=100.0, help="Strike price")
    parser.add_argument("--r", type=float, default=0.05, help="Risk-free rate")
    parser.add_argument("--sigma", type=float, default=0.2, help="Volatility")
    parser.add_argument("--T", type=float, default=1.0, help="Time to maturity (years)")
    parser.add_argument("--steps", type=int, default=252, help="Time steps")
    parser.add_argument("--paths", type=int, default=10000, help="Number of simulation paths")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")

    return parser.parse_args()


def main():
    args = parse_arguments()

    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    np.random.seed(args.seed)

    logging.info("Simulating Geometric Brownian Motion paths...")

    time_grid, paths = simulate_gbm(
        S0=args.S0,
        r=args.r,
        sigma=args.sigma,
        T=args.T,
        steps=args.steps,
        n_paths=args.paths
    )

    logging.info("Computing Monte Carlo option prices...")

    mc_call, se_call, ci_low_call, ci_high_call = monte_carlo_price(
    paths, args.K, args.r, args.T,
    option_type="call",
    return_ci=True
)

    mc_put = monte_carlo_price(paths, args.K, args.r, args.T, option_type="put")

    logging.info("Computing Black-Scholes benchmark prices...")

    bs_call = black_scholes_price(args.S0, args.K, args.r, args.sigma, args.T, "call")
    bs_put = black_scholes_price(args.S0, args.K, args.r, args.sigma, args.T, "put")

    logging.info("Computing risk metrics...")

    terminal_prices = paths[:, -1]
    risk_results = compute_risk_metrics(terminal_prices)

    print("\n==== Option Pricing Results ====")
    print(f"Monte Carlo Call: {mc_call:.4f}")
    print(f"Black-Scholes Call: {bs_call:.4f}")
    print(f"Difference: {mc_call - bs_call:.6f}\n")

    print("\n==== Monte Carlo Confidence Interval (95%) ====")
    print(f"Standard Error: {se_call:.6f}")
    print(f"CI Lower Bound: {ci_low_call:.4f}")
    print(f"CI Upper Bound: {ci_high_call:.4f}")


    from visualization.plots import plot_convergence

    plot_convergence(
    args.S0,
    args.K,
    args.r,
    args.sigma,
    args.T,
    args.steps,
    max_paths=20000,
    step_size=2000
)


    


    print(f"Monte Carlo Put: {mc_put:.4f}")
    print(f"Black-Scholes Put: {bs_put:.4f}")
    print(f"Difference: {mc_put - bs_put:.6f}")

    print("\n==== Risk Metrics (Terminal Price Distribution) ====")
    for key, value in risk_results.items():
        print(f"{key}: {value:.4f}")

    plot_paths(time_grid, paths)
    plot_distribution(terminal_prices)

    import matplotlib.pyplot as plt
    plt.show()


if __name__ == "__main__":
    main()
    
