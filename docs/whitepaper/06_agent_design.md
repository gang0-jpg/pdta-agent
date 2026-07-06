# 06 Agent Design

## 6.1 Design Philosophy

Portfolio Digital Twin Agent (PDTA) adopts a modular multi-agent architecture.

Each AI agent is responsible for a single task within the investment workflow. Rather than implementing all functionality in one large application, PDTA decomposes the investment process into specialized components.

This design provides several advantages:

- Clear separation of responsibilities
- Easy maintenance and testing
- Flexible replacement of individual components
- Future extensibility
- Continuous evolution of the Investor Digital Twin

Each agent communicates through structured data, allowing the overall system to remain modular and reproducible.

---

## 6.2 Current Agent Architecture

The current implementation consists of the following agents.

```
MarketAgent
      │
      ▼
ReturnAgent
      │
      ▼
ScenarioAgent
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
DecisionAgent
      │
      ▼
PolicyAgent
      │
      ▼
MemoryAgent
      │
      ▼
DifferenceAnalyzer
```

Each agent performs a well-defined task within the investment pipeline.

---

## 6.3 Agent Descriptions

### MarketAgent

Responsibilities:

- Download market prices
- Retrieve historical asset data
- Prepare datasets for analysis

Output:

- Historical market prices

---

### ReturnAgent

Responsibilities:

- Calculate daily returns
- Prepare return matrices
- Support portfolio optimization

Output:

- Daily return data

---

### ScenarioAgent

Responsibilities:

- Generate market scenarios
- Apply hypothetical market shocks
- Evaluate portfolio robustness

Typical scenarios include:

- Normal Market
- Bull Market
- Bear Market
- High Inflation
- JPY Weakening
- JPY Strengthening

---

### PortfolioGeneratorAgent

Responsibilities:

- Generate Monte Carlo portfolios
- Produce random portfolio weights
- Prepare optimization candidates

Output:

- Candidate portfolios

---

### OptimizerAgent

Responsibilities:

Evaluate each portfolio using:

- Expected Return
- Portfolio Risk
- Sharpe Ratio
- Maximum Drawdown

Output:

- Portfolio evaluation results

---

### CurrentPortfolioAgent

Responsibilities:

- Evaluate the investor's current portfolio
- Compare current allocation with optimized portfolios

Output:

- Current portfolio metrics

---

### DecisionAgent

Responsibilities:

- Compare optimized portfolios with the current portfolio
- Generate investment recommendations

Typical outputs include:

- BUY
- SELL
- HOLD

---

### PolicyAgent

Responsibilities:

Apply investment policy constraints.

Examples include:

- Maximum buy amount
- Maximum sell amount
- Risk management rules
- Position adjustment policies

PolicyAgent transforms mathematical recommendations into practical investment actions.

---

### MemoryAgent

Responsibilities:

Persist investment history.

Stored information includes:

- Market conditions
- Portfolio composition
- Optimization results
- Recommendations
- Policy decisions
- Investor notes

MemoryAgent uses PostgreSQL JSONB to preserve structured investment history.

---

### DifferenceAnalyzer

Responsibilities:

Compare historical Investor Memory.

The analyzer identifies:

- Target allocation changes
- Recommendation changes
- Policy changes
- Stable investment behavior

Difference analysis provides the first step toward behavioral learning.

---

## 6.4 Planned Agents

Future versions of PDTA will introduce additional AI agents.

### ReflectionAgent

Evaluate previous investment decisions.

Generate lessons learned from historical investment behavior.

---

### ExplanationAgent

Generate natural-language explanations using Large Language Models (LLMs).

Explain:

- Why recommendations changed
- Why portfolio weights changed
- Why investment policy was applied

---

### PersonaAgent

Learn long-term investment behavior.

Identify:

- Investment philosophy
- Risk preference
- Behavioral characteristics

PersonaAgent represents the long-term behavioral model of an investor.

---

### TwinAgent

The final integration layer.

TwinAgent combines:

- Investor Memory
- Difference Analysis
- Reflection
- Persona Learning

to construct a complete Investor Digital Twin.

---

## 6.5 Agent Collaboration

Rather than acting independently, the agents cooperate through a sequential workflow.

```
Market

↓

Analysis

↓

Optimization

↓

Decision

↓

Memory

↓

Learning
```

Each execution of PDTA enriches Investor Memory, enabling future agents to learn from accumulated investment history.

---

## 6.6 Design Principles

The PDTA Agent Architecture follows five principles.

### 1. Single Responsibility

Each agent performs one clearly defined task.

---

### 2. Modular Design

Agents can be replaced or extended independently.

---

### 3. Persistent Memory

Historical decisions are preserved for future learning.

---

### 4. Explainability

Investment decisions should be understandable by investors.

---

### 5. Continuous Learning

Every execution contributes to the long-term construction of the Investor Digital Twin.

---

## 6.7 Summary

The modular AI Agent architecture forms the foundation of PDTA.

Current agents provide market analysis, optimization, recommendation generation, and persistent memory.

Future agents will introduce reflection, explanation, persona learning, and behavioral modeling.

Together, these agents transform PDTA from a portfolio optimization system into a continuously evolving Investor Digital Twin framework.
