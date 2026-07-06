# Vision

# Portfolio Digital Twin Agent (PDTA)

> **Building AI that understands investors, not just markets.**

---

# Research Vision

Portfolio Digital Twin Agent (PDTA) is an open-source research project exploring how Artificial Intelligence can **model, remember, explain, and ultimately predict the decision-making process of an individual investor**.

Rather than focusing solely on portfolio optimization, PDTA aims to build an **Investor Digital Twin**—an AI that continuously learns how a particular investor thinks, reacts, and makes investment decisions over time.

The ultimate research question is:

> **Can an AI understand how an investor makes decisions?**

---

# Why PDTA?

Traditional investment systems focus on one of the following:

- Market prediction
- Portfolio optimization
- Robo-advisors
- Risk management

These systems attempt to answer:

> **"What is the optimal portfolio?"**

PDTA asks a different question:

> **"What would this investor do under today's market conditions?"**

This shift from **portfolio-centric AI** to **investor-centric AI** is the core concept of PDTA.

---

# Beyond Portfolio Optimization

Most portfolio optimization systems stop here.

```
Market Data

↓

Portfolio Optimization

↓

Recommendation
```

PDTA continues beyond optimization.

```
Market Data

↓

Portfolio Optimization

↓

Recommendation

↓

Decision

↓

Investment Policy

↓

Investor Memory

↓

Difference Analysis

↓

Reflection

↓

Learning

↓

Investor Digital Twin

↓

Future Recommendation
```

The goal is not only to optimize a portfolio.

The goal is to understand the investor.

---

# Investor Memory

Human investors remember.

They remember

- previous market crashes
- successful investments
- unsuccessful decisions
- emotional reactions
- changes in investment philosophy

These memories influence future decisions.

PDTA introduces **Investor Memory** to reproduce this process.

Each execution records

- market conditions
- current portfolio
- optimized portfolio
- investment recommendation
- investment policy
- execution results

into PostgreSQL using **JSONB**.

Investor Memory becomes the foundation for long-term learning.

---

# Difference Analysis

Memory alone is not sufficient.

Human investors compare.

They naturally ask questions such as:

- What changed since yesterday?
- Why has the recommendation changed?
- Why did GOLD become HOLD?
- Why is USD allocation increasing?

PDTA introduces **Difference Analysis** to answer these questions.

Difference Analysis compares successive Investor Memories and identifies changes in

- target allocations
- investment actions
- investment policy
- portfolio characteristics

---

# Reflection

Remembering is not enough.

Learning requires reflection.

Future versions of PDTA will include a Reflection Agent capable of evaluating previous investment decisions.

Typical questions include:

- Was this recommendation reasonable?
- Did market conditions change significantly?
- Was the investment policy consistent?
- What can be learned from this execution?

Reflection transforms historical data into investment knowledge.

---

# Learning

Repeated memories become experience.

Repeated experience becomes investment philosophy.

PDTA gradually learns

- preferred asset classes
- reaction to market corrections
- reaction to inflation
- reaction to exchange-rate movements
- long-term investment preferences

This accumulated knowledge forms an **Investor Persona**.

---

# Investor Digital Twin

The long-term objective is to build an AI capable of answering

> **"What would this investor do today?"**

instead of merely answering

> **"What is the mathematically optimal portfolio?"**

An Investor Digital Twin continuously evolves by combining

- optimization
- memory
- comparison
- reflection
- learning

into a single intelligent system.

---

# Research Themes

PDTA combines several research areas.

- Portfolio Optimization
- Digital Twin
- AI Agents
- Investor Memory
- Explainable AI
- Behavioral Finance
- Large Language Models (LLMs)
- Reinforcement through Reflection

---

# Technical Foundation

Current implementation includes

- Monte Carlo Portfolio Optimization
- Multi-scenario Analysis
- Decision Agent
- Policy Agent
- PostgreSQL
- JSONB Investor Memory
- Memory Agent
- Difference Analyzer

Future development will include

- Reflection Agent
- LLM Explanation
- Investor Persona Learning
- Behavior Prediction
- Digital Twin API

---

# Background

The concept of PDTA originates from experience in Electronic Design Automation (EDA).

For decades, Digital Twins have been successfully applied to semiconductor design, manufacturing, and industrial systems.

EDA creates a digital representation of semiconductor designs before fabrication.

PDTA applies the same philosophy to investment.

Instead of creating a Digital Twin of silicon,

PDTA creates a Digital Twin of an investor.

The objective is not simply to optimize investments.

The objective is to reproduce, understand, and eventually predict how an investor makes decisions.

---

# Philosophy

Markets change every day.

Investors change over years.

Understanding the investor is ultimately more valuable than predicting the market.

---

# Mission

Our mission is simple.

Build an AI that not only recommends investments,

but also understands

**why an investor makes those decisions.**
