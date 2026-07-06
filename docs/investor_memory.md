# Investor Memory

## Purpose

Investor Memory stores every execution of PDTA.

Unlike traditional portfolio optimization software,
PDTA remembers how investment decisions were made.

This enables

- history analysis
- behavioral analysis
- reflection
- future prediction

---

## Memory Structure

```text
Run

↓

Market

↓

Portfolio

↓

Recommendation

↓

Decision

↓

Policy

↓

Investor Note
```

Stored as JSONB.

---

## Example

```json
{
  "market": {
    "scenario_count": 6
  },

  "portfolio": {
    "JPY": 0.46,
    "USDJPY": 0.23
  },

  "recommendation": [
    {
      "Asset":"NASDAQ100",
      "Action":"BUY"
    }
  ],

  "decision": {
      "expected_return":0.11,
      "risk":0.08
  },

  "policy":[
      {
          "Asset":"GOLD",
          "AdjustedAction":"HOLD"
      }
  ]
}
```

---

## Why JSONB?

JSONB provides

- flexible schema
- SQL search
- indexing
- future LLM integration

---

## Future

Investor Memory will become

```
Memory

↓

Reflection

↓

Learning

↓

Investor Digital Twin
```

