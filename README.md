# Portfolio Digital Twin Agent (PDTA)

> GPU-powered AI Agent for Portfolio Optimization and Market Digital Twin

Portfolio Digital Twin Agent (PDTA) は、AI・GPU・モンテカルロシミュレーションを活用したポートフォリオ最適化プラットフォームです。

本プロジェクトは **io.net Agent Cloud** を活用し、大量のポートフォリオをGPUで並列評価することを目的としています。

現在は NumPy によるCPU版を実装しており、今後 CuPy によるGPU高速化、io.net Agent Cloud対応、LLMによる市場シナリオ生成へ発展させます。

---

# Features

現在実装済み

- 市場データ取得（Yahoo Finance）
- 日次リターン計算
- Monte Carlo Portfolio Generation
- 100,000 Portfolio Simulation
- Annualized Return
- Annualized Risk
- Sharpe Ratio
- Current Portfolio Evaluation
- Efficient Frontier Plot

---

# Current Assets

現在対応している資産

| Asset | Symbol |
|--------|---------|
| TOPIX | 1306.T |
| NASDAQ100 | 1545.T |
| Gold ETF | 1326.T |
| J-REIT | 1343.T |
| US Treasury Bond | IEF |
| USD/JPY | JPY=X |
| JPY Cash | Internal |

---

# Agent Architecture

```
MarketAgent
        │
        ▼
ReturnAgent
        │
        ▼
PortfolioGeneratorAgent
        │
        ▼
OptimizerAgent
        │
        ▼
CurrentPortfolioAgent
        │
        ▼
ReportAgent
```

将来的には

```
ScenarioAgent

GPU Engine

LLM Agent

Market Digital Twin

io.net Agent Cloud
```

を追加予定です。

---

# Workflow

```
Market Data

        │

        ▼

Daily Returns

        │

        ▼

100,000 Portfolios

        │

        ▼

Risk / Return / Sharpe

        │

        ▼

Efficient Frontier

        │

        ▼

Current Portfolio Evaluation
```

---

# Current Portfolio

現在は以下の資産配分を評価しています。

| Asset | Weight |
|--------|--------|
| TOPIX | 14% |
| NASDAQ100 | 0% |
| Gold | 5% |
| J-REIT | 4% |
| US Bond | 8% |
| USD Cash | 23% |
| JPY Cash | 46% |

---

# Output

実行すると

```
data/

prices.csv

returns.csv

portfolios.csv

portfolio_results.csv

output/

frontier.png
```

が生成されます。

---

# How to Run

```bash
pip install -r requirements.txt

python main.py
```

---

# Current Version

## PDTA v0.5

Completed

- Project Skeleton
- MarketAgent
- ReturnAgent
- PortfolioGeneratorAgent
- OptimizerAgent
- CurrentPortfolioAgent
- ReportAgent
- Efficient Frontier
- JPY Cash Support

---

# Roadmap

## v0.6

- Improved Efficient Frontier
- Better Visualization
- Current Portfolio Highlight

---

## v0.7

GPU Acceleration

- CuPy
- CUDA

---

## v0.8

io.net Agent Cloud

- Distributed GPU Execution
- Large-scale Portfolio Evaluation

---

## v0.9

LLM Integration

- Market Scenario Generation
- Economic Forecast
- Robust Portfolio Optimization

---

## v1.0

Portfolio Digital Twin

- AI Agents
- Market Digital Twin
- GPU Computing
- io.net
- LLM
- Monte Carlo Simulation

---

# Technology Stack

- Python
- NumPy
- Pandas
- Matplotlib
- SciPy
- yfinance
- GitHub
- Cursor
- io.net (planned)
- CuPy (planned)

---

# Research Topics

- Portfolio Optimization
- Efficient Frontier
- Monte Carlo Simulation
- GPU Computing
- AI Agents
- Market Digital Twin
- Financial Digital Twin
- Robust Portfolio Optimization

---

# Disclaimer

This project is intended for research, education, technology demonstrations, and community presentations.

It is **NOT** investment advice.

---

# LT Presentation

Portfolio Digital Twin Agent

**GPUで10万通りのポートフォリオを最適化してみた**

データ分析・AI × データサイエンスコミュニティ 京橋もくもく組

---

# Author

岡 善治

GitHub

https://github.com/gang0-jpg/pdta-agent
