# Appendices

# Appendix A. Current PDTA Implementation

The current implementation of the Portfolio Digital Twin Agent (PDTA) is developed in Python and follows a modular AI agent architecture.

The project currently includes:

- MarketAgent
- ReturnAgent
- ScenarioAgent
- PortfolioGeneratorAgent
- OptimizerAgent
- CurrentPortfolioAgent
- DecisionAgent
- PolicyAgent
- MemoryAgent
- DifferenceAnalyzer

Future versions will introduce ReflectionAgent, ExplanationAgent, PersonaAgent, and TwinAgent.

---

# Appendix B. Technology Stack

Current implementation technologies include:

| Component | Technology |
|-----------|------------|
| Language | Python 3.11 |
| Database | PostgreSQL 16 |
| Storage | JSONB |
| Data Analysis | pandas |
| Numerical Computing | NumPy |
| Portfolio Optimization | Monte Carlo Simulation |
| Visualization | Matplotlib |
| Version Control | Git / GitHub |

Future versions may additionally employ:

- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)
- Knowledge Graphs
- Reinforcement Learning
- Multi-Agent Frameworks

---

# Appendix C. Repository Structure

```
pdta-agent/

├── agents/
├── database/
├── docs/
│   └── whitepaper/
├── optimizer/
├── output/
├── tests/
├── main.py
├── README.md
└── requirements.txt
```

The modular repository structure reflects the AI agent architecture described in this White Paper.

---

# Appendix D. Investor Memory Example

A simplified Investor Memory record is shown below.

```json
{
  "version": "v0.3",
  "market": {
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
  ]
}
```

Investor Memory is stored using PostgreSQL JSONB, allowing flexible schema evolution and AI-friendly structured storage.

---

# Appendix E. Current Research Status

Completed:

- Portfolio Optimization
- Scenario Analysis
- Investor Memory
- Difference Analysis

In Progress:

- Reflection
- Explainable AI

Planned:

- Persona Learning
- Investor Digital Twin

Future:

- Multi-Agent Digital Twins
- Collaborative Investor Twins

---

# Appendix F. Glossary

| Term | Description |
|------|-------------|
| PDTA | Portfolio Digital Twin Agent |
| Investor Memory | Persistent investment history |
| Difference Analysis | Detection of changes between investment histories |
| Reflection | AI evaluation of previous investment decisions |
| Explainable AI | Human-understandable investment reasoning |
| Persona Learning | Behavioral modeling of investors |
| Investor Digital Twin | Computational representation of an investor |

---

# Appendix G. Reproducibility

The objective of PDTA is to provide a reproducible research framework.

The following components support reproducibility:

- Modular AI agents
- Persistent Investor Memory
- Version-controlled source code
- PostgreSQL JSONB storage
- Open documentation
- Public GitHub repository

Future work will include:

- Benchmark datasets
- Standard evaluation protocols
- Experimental reproducibility guidelines

---

# Appendix H. Future White Paper Editions

This White Paper represents Version 1.0 of the conceptual design.

Future editions are expected to incorporate:

- ReflectionAgent implementation
- Explainable AI implementation
- Persona Learning experiments
- Investor Digital Twin evaluation
- Academic validation
- Case studies

The White Paper will evolve together with the PDTA research project.

---

# Appendix I. About the Author

**Zenji Oka**

Portfolio Digital Twin Agent (PDTA)

Independent Research Project

Research Interests

- Artificial Intelligence
- Digital Twins
- Behavioral Finance
- Explainable AI
- Multi-Agent Systems
- Human–AI Collaboration

This White Paper documents the current vision and research direction of the Portfolio Digital Twin Agent project.
