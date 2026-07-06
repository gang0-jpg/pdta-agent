# PDTA Agent Architecture

## Agent Overview

PDTA is composed of multiple autonomous agents.

Each agent has a single responsibility.

```
Market

↓

Return

↓

Scenario

↓

Portfolio Generator

↓

Optimizer

↓

Decision

↓

Policy

↓

Memory

↓

Difference

↓

Reflection

↓

Explanation

↓

Investor Digital Twin
```

---

# Current Agents

## MarketAgent

Collects market prices.

Input

None

Output

prices.csv

---

## ReturnAgent

Calculates returns and covariance.

Input

prices.csv

Output

returns.csv

---

## ScenarioAgent

Creates market scenarios.

Examples

- Bull
- Bear
- Inflation
- JPY Weak
- JPY Strong

---

## PortfolioGeneratorAgent

Generates

100,000 random portfolios.

---

## OptimizerAgent

Calculates

- Return
- Risk
- Sharpe Ratio
- Maximum Drawdown

---

## DecisionAgent

Creates investment recommendations.

---

## PolicyAgent

Applies investment policy.

Example

BUY GOLD

↓

HOLD GOLD

---

## MemoryAgent

Reads Investor Memory.

Functions

latest()

history()

compare_last_two()

---

## DifferenceAnalyzer

Analyzes changes between Investor Memories.

Current

- Target allocation
- Investment action

Future

- Portfolio difference
- Risk difference
- Return difference

---

# Planned Agents

## ReflectionAgent

Purpose

Evaluate previous investment decisions.

Example

Why did NASDAQ100 remain BUY?

---

## ExplanationAgent

Uses LLM.

Converts Difference Analysis into natural language.

Example

"USD allocation increased because
expected return improved."

---

## PersonaAgent

Learns investor behavior.

Example

This investor buys NASDAQ
only after large corrections.

---

## PredictionAgent

Predicts

"What would this investor do today?"

---

# Final Architecture

```
Market

↓

Optimization

↓

Decision

↓

Policy

↓

Memory

↓

Difference

↓

Reflection

↓

LLM Explanation

↓

Persona

↓

Prediction

↓

Investor Digital Twin
```
