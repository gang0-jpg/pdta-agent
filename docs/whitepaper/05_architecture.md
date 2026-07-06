# 05 Overall Architecture

## 5.1 Design Philosophy

Portfolio Digital Twin Agent (PDTA) is designed as a modular AI framework.

Rather than implementing a single monolithic application, PDTA separates the investment process into independent AI agents, each responsible for a specific task.

This modular architecture provides several advantages:

- Separation of responsibilities
- Easy extensibility
- Independent testing
- Future integration of new AI components
- Continuous evolution of the Investor Digital Twin

Each agent produces structured outputs that become inputs to the next stage of the investment pipeline.

This design enables both reproducibility and long-term learning.

---

## 5.2 Overall Workflow

The current PDTA workflow consists of the following stages.

```
Market Data
      │
      ▼
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
DecisionAgent
      │
      ▼
PolicyAgent
      │
      ▼
Investor Memory
      │
      ▼
Difference Analyzer
```

Each stage has a clearly defined responsibility and communicates using structured data.

---

## 5.3 Layered Architecture

PDTA may also be viewed as a layered architecture.

```
Presentation Layer
    White Paper
    Reports
    Charts

──────────────

Decision Layer
    Decision Agent
    Policy Agent

──────────────

Optimization Layer
    Optimizer
    Portfolio Generator

──────────────

Analysis Layer
    Return Agent
    Scenario Agent

──────────────

Market Layer
    Market Agent

──────────────

Memory Layer
    PostgreSQL
    Investor Memory
```

This layered architecture simplifies future extensions while maintaining a clear separation of responsibilities.

---

## 5.4 Current Implementation

Version 0.3 currently implements:

- Market data acquisition
- Return calculation
- Scenario evaluation
- Portfolio optimization
- Current portfolio evaluation
- Recommendation generation
- Policy adjustment
- Investor Memory
- Difference Analysis

These components already form a complete investment analysis pipeline.

---

## 5.5 Planned Architecture

Future versions will extend the architecture with additional AI agents.

```
Investor Memory
        │
        ▼
Reflection Agent
        │
        ▼
Explanation Agent
        │
        ▼
Persona Learning
        │
        ▼
Investor Digital Twin
```

These components will allow PDTA to move beyond portfolio optimization toward continuous investor modeling.

---

## 5.6 Architectural Principles

The PDTA architecture follows five design principles.

1. Modular AI Agents

Each component has a single responsibility.

2. Persistent Memory

Historical investment information is preserved rather than discarded.

3. Explainability

Investment recommendations should be understandable.

4. Continuous Learning

The framework evolves through accumulated investor experience.

5. Human-Centered AI

PDTA is designed to assist investors, not replace them.

These principles provide the foundation for the long-term evolution of the Investor Digital Twin.
