# 01 Executive Summary

Portfolio Digital Twin Agent (PDTA) is an open-source research project that explores a new generation of AI-assisted investment systems.

Traditional portfolio optimization techniques focus primarily on identifying mathematically optimal asset allocations using historical returns, portfolio risk, and statistical optimization methods. While these approaches are effective for quantitative analysis, they rarely attempt to model the investor behind the portfolio.

PDTA introduces a different perspective.

Instead of optimizing portfolios alone, PDTA aims to understand how investors make decisions.

The central concept of the project is the **Investor Digital Twin**—a computational model that continuously learns an investor's investment philosophy, risk tolerance, behavioral characteristics, and decision-making process.

To support this vision, PDTA combines several complementary technologies into a unified AI framework.

Current components include:

- Monte Carlo Portfolio Optimization
- Scenario-Based Portfolio Evaluation
- Investor Memory using PostgreSQL JSONB
- Historical Difference Analysis
- AI Agent Architecture

Future versions will introduce:

- Reflection Agents for self-evaluation of past decisions
- Explainable AI using Large Language Models (LLMs)
- Persona Learning for modeling long-term investment behavior
- Continuous learning from accumulated investment history

Unlike conventional investment systems that answer:

> **"What is the mathematically optimal portfolio?"**

PDTA ultimately seeks to answer a different question:

> **"What would this investor do under today's market conditions?"**

This shift represents a transition from **portfolio-centric optimization** toward **investor-centric decision modeling**.

Investor Memory plays a central role in this framework.

Every execution of PDTA stores market conditions, portfolio states, optimization results, recommendations, policy decisions, and investor notes in PostgreSQL using JSONB. These historical records provide the foundation for future reflection, behavioral analysis, and digital twin construction.

The long-term objective of the project is not simply to improve investment recommendations.

Rather, PDTA aims to build an **Investor Digital Twin** capable of simulating, explaining, and continuously improving investment decisions through interaction with both historical experience and current market conditions.

This White Paper documents the motivation, design philosophy, architecture, implementation, and future research direction of the Portfolio Digital Twin Agent project.

PDTA is designed as a living research framework, evolving together with its source code, documentation, and accumulated investor knowledge.
