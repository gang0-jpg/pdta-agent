# 10 Explainable AI

## 10.1 Motivation

Modern AI systems are increasingly capable of generating sophisticated investment recommendations.

However, numerical recommendations alone are insufficient.

Investors must understand:

- Why a recommendation was generated.
- Which assumptions influenced the decision.
- Which market conditions were considered.
- Why today's recommendation differs from previous ones.

Without explanation, investors cannot fully trust AI-assisted investment systems.

PDTA therefore considers explainability to be a fundamental requirement rather than an optional feature.

---

## 10.2 Explainability in PDTA

Explainable AI (XAI) in PDTA is designed to translate quantitative investment analysis into human-understandable reasoning.

Rather than presenting only portfolio weights or optimization metrics, PDTA explains the reasoning process behind each recommendation.

For example, instead of reporting:

```
BUY NASDAQ100
```

PDTA aims to explain:

> "NASDAQ100 allocation increased because expected returns improved while portfolio risk remained within the investor's policy constraints."

This transformation allows investors to understand not only **what** was recommended, but also **why**.

---

## 10.3 Relationship with Reflection

Reflection and Explainable AI serve different purposes.

```
Reflection
    AI understands itself

↓

Explainable AI
    AI explains itself to humans
```

Reflection generates internal knowledge.

Explainable AI communicates that knowledge to investors.

Together they establish transparent human-AI collaboration.

---

## 10.4 Sources of Explanation

PDTA generates explanations using multiple sources of information.

These include:

- Current market conditions
- Portfolio optimization results
- Investor Memory
- Difference Analysis
- Investment policy
- Reflection results

By integrating these components, explanations become both quantitative and contextual.

---

## 10.5 Types of Explanations

PDTA supports several categories of explanations.

### Recommendation Explanation

Explain why an investment recommendation was generated.

Example:

> "TOPIX allocation decreased because expected risk increased relative to other assets."

---

### Difference Explanation

Explain why today's recommendation differs from previous executions.

Example:

> "USDJPY allocation increased due to continued JPY depreciation and improved expected return."

---

### Policy Explanation

Explain how investment policy affected recommendations.

Example:

> "Although GOLD was recommended as BUY, the final action became HOLD because the maximum purchase limit was reached."

---

### Historical Explanation

Explain recommendations using historical Investor Memory.

Example:

> "A similar market environment occurred previously, where maintaining USD exposure reduced portfolio volatility."

---

## 10.6 LLM-Assisted Explanation

Future versions of PDTA will employ Large Language Models (LLMs) to generate personalized explanations.

LLMs provide several advantages:

- Natural language generation
- Context awareness
- Interactive dialogue
- User-specific explanation style

Rather than producing fixed templates, explanations become adaptive to the investor's knowledge and preferences.

---

## 10.7 Explainability Pipeline

The explainability process follows the architecture below.

```
Market Data

↓

Optimization

↓

Investor Memory

↓

Difference Analysis

↓

Reflection

↓

LLM

↓

Natural Language Explanation
```

Each stage contributes additional context before the final explanation is generated.

---

## 10.8 Human-Centered AI

PDTA is not designed to replace investor judgment.

Instead, Explainable AI supports collaboration between human investors and AI agents.

The objective is to enable investors to understand:

- the recommendation,
- the reasoning,
- the uncertainty,
- and the assumptions behind every decision.

Explainability therefore strengthens trust rather than automation.

---

## 10.9 Future Directions

Future Explainable AI research within PDTA includes:

- Interactive investment dialogue
- Counterfactual explanations
- Personalized explanation styles
- Multilingual explanation
- Voice-based investment assistants
- Explanation quality evaluation

These capabilities will transform PDTA from a recommendation engine into an intelligent investment partner.

---

## 10.10 Summary

Explainable AI is the communication layer of PDTA.

Investor Memory preserves experience.

Difference Analysis identifies change.

Reflection creates knowledge.

Explainable AI shares that knowledge with investors.

Together these components establish transparent, trustworthy, and collaborative AI-assisted investment.

The ultimate objective is not merely to generate better recommendations.

It is to enable investors to understand, trust, and continuously improve their investment decisions alongside AI.
