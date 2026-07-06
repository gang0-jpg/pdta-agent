# 08 Difference Analysis

## 8.1 Motivation

Investor Memory preserves historical investment decisions.

However, memory alone is insufficient.

To support learning, an AI system must recognize **how investment decisions change over time**.

This capability is provided by **Difference Analysis**.

Rather than simply storing historical records, PDTA continuously compares successive Investor Memory snapshots to identify meaningful changes in investment behavior.

Difference Analysis therefore represents the transition from **memory** to **understanding**.

---

## 8.2 Why Difference Matters

Investment decisions are rarely static.

Even when market conditions remain relatively stable, recommended portfolio allocations may gradually change as:

- Market prices evolve
- Portfolio risk changes
- Expected returns change
- Investment policies are updated

Observing these changes is often more informative than observing individual investment decisions.

Difference Analysis focuses on identifying these changes.

---

## 8.3 Comparison Strategy

Each new Investor Memory record is compared with previous records.

Current comparisons include:

- Portfolio allocation targets
- BUY / SELL / HOLD recommendations
- Policy adjustments
- Portfolio risk
- Expected return
- Sharpe Ratio

Each comparison produces structured information describing how investment decisions evolved.

---

## 8.4 Current Implementation

The current DifferenceAnalyzer compares consecutive Investor Memory records.

Typical outputs include:

| Asset | Previous Target | Current Target | Difference | Action Changed |
|--------|----------------:|---------------:|-----------:|---------------|
| NASDAQ100 | 10.3% | 13.9% | +3.6% | No |
| TOPIX | 5.6% | 12.9% | +7.3% | No |
| USDJPY | 34.1% | 42.2% | +8.1% | No |
| GOLD | 21.5% | 21.3% | -0.2% | No |

The current implementation therefore detects quantitative changes while preserving qualitative investment decisions.

---

## 8.5 Stable Decisions

Not every change represents a behavioral change.

For example,

```
BUY NASDAQ100

↓

BUY NASDAQ100
```

The recommendation remains unchanged even though the target allocation increases.

Difference Analysis distinguishes between:

- Stable investment philosophy
- Quantitative portfolio adjustments

This distinction is essential for future behavioral learning.

---

## 8.6 Relationship with Investor Memory

Investor Memory records historical facts.

Difference Analysis extracts relationships between those facts.

```
Investor Memory

↓

Difference Analysis

↓

Behavioral Interpretation
```

Without Investor Memory, no comparison is possible.

Without Difference Analysis, historical records remain isolated observations.

Together they create structured investment knowledge.

---

## 8.7 Toward Reflection

Difference Analysis prepares the input for future Reflection Agents.

Reflection will answer questions such as:

- Why did recommendations change?
- Were previous recommendations successful?
- Which policy adjustments were effective?
- Which investment decisions should be reconsidered?

Difference Analysis therefore acts as the bridge between historical memory and reflective reasoning.

---

## 8.8 Future Extensions

Future versions of Difference Analysis will include:

- Multi-period trend analysis
- Behavioral drift detection
- Investment philosophy stability
- Risk tolerance evolution
- Market regime comparison
- LLM-based interpretation

Rather than comparing only two executions, future versions will analyze long-term behavioral patterns.

---

## 8.9 Design Philosophy

Difference Analysis follows a simple principle.

> **Learning begins with recognizing change.**

An AI system cannot improve if it cannot identify how its previous decisions differ from its current ones.

Difference Analysis provides this capability.

It transforms historical records into meaningful observations that support future learning.

---

## 8.10 Summary

Difference Analysis is the second core innovation of PDTA.

Investor Memory preserves experience.

Difference Analysis interprets experience.

Together they provide the foundation for Reflection, Explainable AI, Persona Learning, and ultimately the Investor Digital Twin.

The purpose of Difference Analysis is not merely to calculate numerical differences.

Its purpose is to understand how investment decisions evolve over time.
