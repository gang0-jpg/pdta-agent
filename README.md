# Portfolio Digital Twin Agent (PDTA)

> GPU-powered AI Agent for Portfolio Optimization and Market Digital Twin

PDTA (Portfolio Digital Twin Agent) is an AI framework that aims to realize an **Investor Digital Twin** for personalized investment decision support.

Unlike traditional portfolio optimization tools, PDTA does not simply search for the portfolio with the highest return.

Instead, it models an investor's investment philosophy, risk tolerance, and decision-making process, and searches for a robust portfolio that can withstand a wide range of future market scenarios.

---

# Vision

Traditional portfolio optimization seeks the highest expected return.

PDTA goes one step further.

Instead of finding the "best" portfolio, PDTA aims to build an **Investor Digital Twin** that understands an investor's goals, risk tolerance, investment philosophy, and decision-making process.

The objective is not simply to maximize returns, but to support robust, explainable, and personalized investment decisions under uncertain market conditions.

---

# Features

Current implementation includes:

- MarketAgent
  - Download market prices using Yahoo Finance

- ReturnAgent
  - Calculate daily returns

- PortfolioGeneratorAgent
  - Generate random portfolios (Monte Carlo)

- OptimizerAgent
  - Portfolio optimization
  - Expected Return
  - Risk (Volatility)
  - Sharpe Ratio
  - Maximum Drawdown

- CurrentPortfolioAgent
  - Evaluate the user's current portfolio

- ScenarioAgent
  - Market Scenario Simulation
  - Normal
  - Bull Market
  - Bear Market
  - High Inflation
  - JPY Weak
  - JPY Strong

- ReportAgent
  - Efficient Frontier
  - Scenario Summary Chart

---

# Current Architecture

```
                +----------------+
                | Market Agent   |
                +----------------+
                        |
                        v
                +----------------+
                | Return Agent   |
                +----------------+
                        |
                        v
                +----------------+
                | Scenario Agent |
                +----------------+
                        |
                        v
         +----------------------------+
         | Portfolio Generator Agent  |
         +----------------------------+
                        |
                        v
                +----------------+
                | OptimizerAgent |
                +----------------+
                        |
        +---------------+----------------+
        |                                |
        v                                v
+----------------------+      +----------------------+
| Current Portfolio    |      | Report Agent         |
+----------------------+      +----------------------+
```

---

# Example Output

Current Portfolio

```
Sharpe Ratio

Maximum Drawdown

Expected Return

Risk
```

Best Portfolio

```
Expected Return

Risk

Sharpe Ratio

Maximum Drawdown
```

Scenario Analysis

```
Normal

Bull

Bear

High Inflation

JPY Weak

JPY Strong
```

Efficient Frontier

```
output/frontier.png
```

Scenario Summary

```
output/scenario_summary.png
```

---

# Project Structure

```
pdta-agent/

├── agents/
│   ├── market_agent.py
│   ├── return_agent.py
│   ├── scenario_agent.py
│   ├── portfolio_generator_agent.py
│   ├── optimizer_agent.py
│   ├── current_portfolio_agent.py
│   └── report_agent.py
│
├── backends/
│   ├── __init__.py
│   └── numpy_backend.py
│
├── data/
├── docs/
├── optimizer/
├── output/
├── tests/
│
├── config.py
├── main.py
├── requirements.txt
└── README.md
```

---

# Roadmap

## Version 0.x

- MarketAgent
- Portfolio Optimization
- Monte Carlo Simulation
- Efficient Frontier
- Scenario Simulation
- Maximum Drawdown
- CPU Backend

---

## Version 1.x

- GPU Backend (CuPy)
- io.net Integration
- NVIDIA H100 Support
- 1 Million Portfolios
- 100 Market Scenarios

---

## Version 2.x

Investor Digital Twin

- Personalized Investment Policy
- Portfolio Rebalancing
- Decision Agent
- Portfolio Recommendation
- Robust Score
- AI Portfolio Manager

---

# Future Vision

PDTA evolves toward an **Investor Digital Twin**.

Rather than recommending the same portfolio to every investor, PDTA learns each investor's own:

- Investment philosophy
- Risk tolerance
- Return target
- Rebalancing strategy
- Decision-making style

The ultimate goal is to create an AI agent that behaves like a personal fund manager.

---

# Philosophy

PDTA does not pursue a single "optimal" portfolio.

Instead, it searches for the portfolio that best matches each investor's own investment philosophy, risk tolerance, and long-term objectives.

Every investor is different.

Therefore every Digital Twin should also be different.

---

# Technology

- Python
- Pandas
- NumPy
- Matplotlib
- yfinance
- Monte Carlo Simulation
- GPU Computing
- io.net
- NVIDIA H100
- AI Agents
- Digital Twin

---

# License

MIT License

---

# Author

Yoshiharu Oka

Portfolio Digital Twin Agent (PDTA)

Toward an Investor Digital Twin
