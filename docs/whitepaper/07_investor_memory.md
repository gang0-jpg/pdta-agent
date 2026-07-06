# 07 Investor Memory

## 7.1 Motivation

Traditional portfolio optimization systems typically perform calculations, generate recommendations, and then discard the intermediate decision process.

As a result, every execution begins without knowledge of previous investment decisions.

PDTA adopts a different approach.

Investment decisions should accumulate over time.

Every recommendation, portfolio adjustment, and market observation contributes to a growing body of investor knowledge.

This persistent knowledge base is called **Investor Memory**.

Investor Memory enables PDTA to learn from historical investment behavior rather than treating each portfolio optimization as an isolated event.

---

## 7.2 Design Philosophy

Investor Memory is designed according to three fundamental principles.

### Persistence

Investment history should never be discarded.

Every execution becomes part of the investor's accumulated experience.

### Traceability

Every recommendation should be traceable back to:

- Market conditions
- Portfolio composition
- Optimization results
- Investment policy

### Future Learning

Historical investment records provide the foundation for:

- Reflection
- Explainable AI
- Persona Learning
- Investor Digital Twin

Investor Memory therefore serves as the long-term knowledge base of PDTA.

---

## 7.3 Database Architecture

PDTA stores Investor Memory using PostgreSQL.

Rather than designing a large number of normalized tables, PDTA stores investment snapshots using **JSONB**.

This approach provides several advantages:

- Flexible schema evolution
- Efficient storage
- Native JSON querying
- Compatibility with AI-generated data
- Easy integration with Large Language Models

The database therefore acts not only as persistent storage but also as structured long-term memory.

---

## 7.4 Memory Structure

Each Investor Memory record contains a complete snapshot of one PDTA execution.

Typical fields include:

- Execution time
- PDTA version
- Market conditions
- Portfolio allocation
- Optimization results
- Investment recommendation
- Policy adjustment
- Investor notes

This snapshot-based design allows every execution to be reproduced and analyzed independently.

---

## 7.5 Example Memory Record

```json
{
  "version": "v0.3",
  "market": {
    "USDJPY": 162.3,
    "scenario_count": 6
  },
  "portfolio": {
    "JPY": 0.46,
    "USDJPY": 0.23,
    "GOLD": 0.05
  },
  "recommendation": [
    {
      "Asset": "NASDAQ100",
      "Action": "BUY"
    }
  ],
  "policy": [
    {
      "Asset": "NASDAQ100",
      "AdjustedAction": "BUY"
    }
  ],
  "investor_note": "Automatic PDTA run"
}
```

The JSONB representation allows PDTA to preserve structured investment history while remaining flexible enough to accommodate future extensions.

---

## 7.6 Investor Memory Workflow

Each execution of PDTA generates a new memory record.

```
Market Data

↓

Portfolio Optimization

↓

Recommendation

↓

Policy Adjustment

↓

Investor Memory

↓

Historical Database
```

Unlike temporary program variables, Investor Memory persists across multiple executions.

---

## 7.7 Relationship with MemoryAgent

MemoryAgent provides the interface between the AI agents and PostgreSQL.

Its responsibilities include:

- Reading historical memories
- Retrieving recent investment history
- Comparing previous executions
- Supplying historical context to future AI agents

MemoryAgent transforms the database into an active component of the AI framework.

---

## 7.8 Relationship with Difference Analysis

Investor Memory alone stores history.

Difference Analysis extracts meaning from history.

By comparing consecutive Investor Memory records, PDTA identifies:

- Portfolio allocation changes
- Recommendation changes
- Policy changes
- Stable investment behavior

Investor Memory provides the data.

Difference Analysis provides interpretation.

---

## 7.9 Toward Reflection

Investor Memory represents the first stage of continuous learning.

Future Reflection Agents will analyze historical memories and answer questions such as:

- Why did recommendations change?
- Which investment decisions proved effective?
- Which decisions should be reconsidered?
- How has the investor's behavior evolved?

Investor Memory therefore enables AI systems to learn from experience rather than relying solely on current market data.

---

## 7.10 Summary

Investor Memory is one of the defining innovations of PDTA.

Instead of treating each execution independently, PDTA preserves investment history as structured knowledge using PostgreSQL JSONB.

This persistent memory enables historical comparison, behavioral analysis, reflection, explainability, and ultimately the construction of an Investor Digital Twin.

Rather than storing data for archival purposes alone, Investor Memory stores experience.

Experience is the foundation upon which the Investor Digital Twin is built.
