
# 🔄 OPTION PRICING WORKFLOW

```mermaid
flowchart TD

A[Input Parameters]

A --> B[Generate GBM Paths]

B --> C[Simulate Terminal Prices]

C --> D[Calculate Option Payoffs]

D --> E[Discount Payoffs]

E --> F[Monte Carlo Price]

F --> G[Compute Confidence Interval]

G --> H[Compare with Black-Scholes]

H --> I[Generate Pricing Report]
```

---

# ⚡ MONTE CARLO PRICING SEQUENCE DIAGRAM

```mermaid
sequenceDiagram

participant User
participant CLI
participant GBM
participant MC
participant BS
participant Risk
participant Visualization

User->>CLI: Run Simulation

CLI->>GBM: Generate Paths

GBM-->>MC: Simulated Price Paths

MC->>MC: Calculate Payoffs

MC->>MC: Discount Payoffs

MC-->>BS: Request Benchmark Price

BS-->>MC: Analytical Option Price

MC->>Risk: Compute VaR & CVaR

Risk-->>MC: Risk Metrics

MC->>Visualization: Send Results

Visualization-->>User: Charts & Reports
```

---

# 📊 MONTE CARLO CONVERGENCE DIAGRAM

```mermaid
flowchart LR

P1[1K Paths]
--> P2[5K Paths]
--> P3[10K Paths]
--> P4[25K Paths]
--> P5[50K Paths]
--> P6[100K Paths]

P1 --> MC1[MC Estimate]
P2 --> MC2[MC Estimate]
P3 --> MC3[MC Estimate]
P4 --> MC4[MC Estimate]
P5 --> MC5[MC Estimate]
P6 --> MC6[MC Estimate]

MC1 --> BS[Black-Scholes Benchmark]
MC2 --> BS
MC3 --> BS
MC4 --> BS
MC5 --> BS
MC6 --> BS

BS --> Result[Convergence Validation]
```

---

# 📈 RISK ANALYTICS PIPELINE

```mermaid
flowchart TD

A[Terminal Price Distribution]

A --> B[Portfolio Returns]

B --> C[Sort Outcomes]

C --> D[VaR 95%]

C --> E[VaR 99%]

D --> F[CVaR 95%]

E --> G[CVaR 99%]

F --> H[Risk Report]
G --> H
```

---

# 📂 PROJECT STRUCTURE ARCHITECTURE

```mermaid
flowchart TB

Root[new_quant_project]

Root --> Main[main.py]

Root --> Models[models]
Models --> GBM[gbm.py]

Root --> Pricing[pricing]
Pricing --> MC[monte_carlo.py]
Pricing --> BS[black_scholes.py]

Root --> Risk[risk]
Risk --> Metrics[metrics.py]

Root --> Visualization[visualization]
Visualization --> Plots[plots.py]
```

---