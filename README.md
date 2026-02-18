# 📈 Quantitative Monte Carlo Option Pricing Engine

A modular, statistically validated Monte Carlo simulation engine for pricing European options under **Geometric Brownian Motion (GBM)**, benchmarked against the **Black-Scholes analytical solution**, and extended with **risk analytics and convergence diagnostics**.

---

## 🚀 Overview

This project implements a production-style Monte Carlo pricing framework designed to demonstrate:

- Stochastic process simulation (GBM)
- Risk-neutral option pricing
- Statistical confidence intervals
- Convergence diagnostics
- Value-at-Risk (VaR) and Conditional VaR (CVaR)
- Modular software architecture

The engine validates numerical pricing results against the Black-Scholes closed-form solution and provides statistical confidence bounds for estimator reliability.

---

## 🧠 Mathematical Foundation

### 1️⃣ Geometric Brownian Motion

The stock price follows:

dSₜ = r Sₜ dt + σ Sₜ dWₜ

Under the risk-neutral measure:

Sₜ = S₀ · exp[(r − ½σ²)T + σWₜ]

The implementation is fully vectorized using NumPy for computational efficiency.

---

### 2️⃣ Monte Carlo Pricing

European Call Option Price:

C = e^(−rT) · E[max(Sₜ − K, 0)]

Estimated using:

Ĉ = e^(−rT) · (1/N) Σ max(Sₜ⁽ⁱ⁾ − K, 0)

Includes 95% confidence interval:

Ĉ ± 1.96 · (σ / √N)

---

### 3️⃣ Black-Scholes Benchmark

Closed-form analytical solution:

C = S₀ N(d₁) − K e^(−rT) N(d₂)

Used to verify:

- Monte Carlo convergence
- Statistical consistency

---

## 📊 Features

- ✔ Vectorized GBM simulation  
- ✔ Monte Carlo pricing (Call & Put)  
- ✔ Black-Scholes analytical benchmark  
- ✔ 95% Confidence Interval estimation  
- ✔ Convergence diagnostics (MC → BS)  
- ✔ Terminal distribution visualization  
- ✔ VaR (95%, 99%)  
- ✔ CVaR (Expected Shortfall)  
- ✔ CLI parameter configuration  
- ✔ Modular project structure  

---

## 🏗 Project Structure

```
new_quant_project/
│
├── main.py
│
├── models/
│   └── gbm.py
│
├── pricing/
│   ├── monte_carlo.py
│   └── black_scholes.py
│
├── risk/
│   └── metrics.py
│
├── visualization/
│   └── plots.py
```

### Design Principles

- **Separation of concerns**
- **Modular scalability**
- **Vectorized computation**
- **Statistical validation**
- **CLI-driven experimentation**

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
```

### Dependencies

- numpy  
- scipy  
- matplotlib  

---

## ▶️ Usage

Run with default parameters:

```bash
python main.py
```

Run with custom parameters:

```bash
python main.py --S0 100 --K 105 --sigma 0.3 --paths 50000
```

### CLI Arguments

| Argument | Description |
|----------|------------|
| `--S0` | Initial stock price |
| `--K` | Strike price |
| `--r` | Risk-free rate |
| `--sigma` | Volatility |
| `--T` | Time to maturity |
| `--steps` | Time steps |
| `--paths` | Number of Monte Carlo paths |
| `--seed` | Random seed |

---

## 📈 Output

The program generates:

- Simulated GBM paths  
- Terminal price distribution  
- Monte Carlo convergence plot  
- Option pricing comparison (MC vs Black-Scholes)  
- 95% confidence interval  
- VaR & CVaR statistics  

Example output:

```
Monte Carlo Call: 10.2211
Black-Scholes Call: 10.4506
Difference: -0.2295

95% Confidence Interval:
[9.9376 , 10.5045]

VaR 95%: 73.80
CVaR 95%: 68.09
```

---

## 🔬 Validation Strategy

The model is validated through:

1. Analytical benchmarking against Black-Scholes  
2. Convergence diagnostics as number of paths increases  
3. Statistical confidence interval containment  
4. Risk metric analysis of terminal distribution  

---

## 💡 Engineering Highlights

- Fully vectorized Monte Carlo simulation
- Confidence interval estimation for statistical rigor
- Convergence diagnostics for numerical validation
- Modular architecture for extensibility
- Clean CLI interface for experimentation

---

## 📚 Future Extensions

- Greeks estimation (Delta, Vega)
- Variance reduction techniques
- American option pricing
- Jump diffusion models
- Heston stochastic volatility model
- Parallel computation optimization

---

## 👨‍💻 Author

**Rudra Raj**  
Quantitative Finance & Systems Engineering Enthusiast  

---

