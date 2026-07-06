# Portfolio Digital Twin Agent (PDTA)

> **A Memory-Centric AI Framework for Building an Investor Digital Twin**

PDTA (Portfolio Digital Twin Agent) is an open-source research project that explores the next generation of AI-assisted investment systems.

Unlike traditional portfolio optimization tools, PDTA does not simply search for the mathematically optimal portfolio.

Instead, PDTA models an investor's investment philosophy, risk tolerance, behavioral characteristics, and decision-making process to build an **Investor Digital Twin**.

The long-term goal is to create an AI capable of answering:

> **"What would this investor do under today's market conditions?"**

rather than simply answering:

> **"What is the mathematically optimal portfolio?"**

---

# Vision

Traditional investment systems focus on:

- Market prediction
- Portfolio optimization
- Robo-advisors
- Risk management

PDTA introduces a different perspective.

Instead of optimizing portfolios alone, PDTA attempts to model the investor.

The project combines

- Portfolio Optimization
- Investor Memory
- Difference Analysis
- Reflection
- Explainable AI
- Persona Learning

to build an **Investor Digital Twin**.

---

# Current Features

## Portfolio Optimization

- Monte Carlo Portfolio Optimization
- Efficient Frontier
- Expected Return
- Portfolio Risk
- Sharpe Ratio
- Maximum Drawdown

---

## AI Agents

Current implementation includes:

### MarketAgent

- Download market prices using Yahoo Finance

### ReturnAgent

- Calculate daily returns

### ScenarioAgent

Generate market scenarios:

- Normal
- Bull Market
- Bear Market
- High Inflation
- JPY Weak
- JPY Strong

### PortfolioGeneratorAgent

Generate random portfolios using Monte Carlo simulation.

### OptimizerAgent

Evaluate

- Expected Return
- Risk
- Sharpe Ratio
- Maximum Drawdown

### CurrentPortfolioAgent

Evaluate the current portfolio.

### DecisionAgent

Generate investment recommendations.

### PolicyAgent

Apply investment policy constraints.

### MemoryAgent

Manage Investor Memory stored in PostgreSQL.

### DifferenceAnalyzer

Compare historical investment decisions and identify changes.

---

# Investor Memory

One of the core innovations of PDTA is **Investor Memory**.

Every execution records

- Market conditions
- Portfolio status
- Optimization results
- Recommendations
- Investment policy
- Investor notes

using PostgreSQL **JSONB**.

This enables long-term analysis of investment behavior.

---

# Current Architecture

```
                Market Agent
                     │
                     ▼
               Return Agent
                     │
                     ▼
              Scenario Agent
                     │
                     ▼
      Portfolio Generator Agent
                     │
                     ▼
              Optimizer Agent
                     │
         ┌───────────┴───────────┐
         ▼                       ▼
 Current Portfolio         Decision Agent
                                 │
                                 ▼
                          Policy Agent
                                 │
                                 ▼
                         Investor Memory
                                 │
                                 ▼
                        Difference Analyzer
```

---

# Project Structure

```
pdta-agent/

├── agents/
├── database/
├── docs/
│
├── vision.md
├── architecture.md
├── investor_memory.md
├── roadmap.md
├── research.md
├── agents.md
│
└── whitepaper/
    ├── README.md
    ├── 00_cover.md
    ├── 01_executive_summary.md
    ├── ...
│
├── optimizer/
├── output/
├── tests/
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Roadmap

## Version 0.1

- Portfolio Optimization
- Monte Carlo Simulation
- Efficient Frontier

---

## Version 0.2

- PostgreSQL
- Investor Memory (JSONB)

---

## Version 0.3

- MemoryAgent
- DifferenceAnalyzer

---

## Version 0.4

- ReflectionAgent

---

## Version 0.5

- Explainable AI
- LLM Integration

---

## Version 0.6

- Persona Learning

---

## Version 1.0

**Investor Digital Twin**

---

# White Paper

The design philosophy, system architecture, and long-term vision of PDTA are documented in the White Paper.

See:

```
docs/whitepaper/
```

The White Paper evolves together with the source code.

---

# Future Vision

PDTA evolves beyond portfolio optimization.

```
Market Data

↓

Portfolio Optimization

↓

Recommendation

↓

Investor Memory

↓

Difference Analysis

↓

Reflection

↓

Persona Learning

↓

Investor Digital Twin
```

The objective is not only to recommend investments.

The objective is to understand how an investor makes investment decisions.

---

# Technology

- Python
- Pandas
- NumPy
- Matplotlib
- PostgreSQL
- JSONB
- yfinance
- Monte Carlo Simulation
- AI Agents
- Large Language Models (LLMs)

---

# License

MIT License

---

# Author

**Zenji Oka**

Portfolio Digital Twin Agent (PDTA)

> **Building AI that understands investors, not just markets.**
