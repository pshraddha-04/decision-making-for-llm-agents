# Adaptive Uncertainty-Aware Decision Making for Reliable Autonomous LLM Agents

## Overview

Large Language Models (LLMs) are increasingly used to build autonomous agents that reason, answer questions, and use external tools such as RAG and web search. However, these agents can produce hallucinated or unreliable responses, particularly when they lack sufficient knowledge or evidence.

This project introduces an **adaptive decision-making layer** for LLM agents. The agent analyzes the uncertainty and knowledge gap associated with a user query, then considers additional factors — evidence quality, question ambiguity, and task complexity — before an adaptive decision policy selects the most appropriate action:

- **Answer** – when the agent is sufficiently confident
- **Retrieve** – when additional information is required
- **Verify** – when the generated answer or evidence is uncertain
- **Clarify** – when the question is ambiguous
- **Abstain** – when a reliable answer cannot be provided

## Problem Statement

Current LLM agents may answer questions even when uncertain or under-informed. Existing approaches (RAG, self-reflection, fixed uncertainty thresholds) address only specific aspects of reliability and often lead to unnecessary tool usage. This project builds an adaptive approach that jointly considers uncertainty, evidence quality, ambiguity, and task complexity to decide the next best action.

## Research Gaps Addressed

1. Limited uncertainty-aware decision making in existing LLM agents
2. Fixed decision strategies (static thresholds/rules) instead of adaptive ones
3. Reliability factors (uncertainty, evidence quality, ambiguity, complexity) treated separately rather than jointly
4. Over-reliance on retrieval or self-reflection, increasing latency and API cost
5. Limited focus on the reliability–efficiency trade-off

## Objectives

1. Develop an autonomous LLM agent capable of estimating uncertainty and knowledge gaps
2. Design an adaptive decision policy for selecting actions based on multiple reliability factors
3. Reduce hallucinated and unreliable responses
4. Improve the agent's ability to abstain or request clarification when appropriate
5. Minimize unnecessary tool calls, API usage, computational cost, and latency
6. Compare the proposed approach with existing LLM agent strategies using standard evaluation metrics

## Literature Foundations

| Approach | Contribution |
|---|---|
| SAUP (Zhao et al.) | Propagates uncertainty across multi-step agent workflows, not just the final output |
| SelfCheckGPT (Manakul et al.) | Zero-resource hallucination detection via consistency across sampled responses |
| Moskvoretskii et al. | Shows uncertainty-based methods can identify model knowledge as reliably as adaptive retrieval, at lower cost |
| P(True) / P(IK) (Kadavath et al.) | Studies whether LLMs can recognize correctness of their own answers |
| SELAUR (Zhang et al.) | RL framework using entropy/least-confidence/margin-based uncertainty for reward shaping |
| UAG | Detects and quantifies user intent uncertainty via a hierarchical intent tree |

## Tech Stack

- **Language:** Python
- **LLM inference:** Ollama (local), Groq or Gemini (free-tier hosted)
- **Agent framework:** LangChain or LlamaIndex
- **Vector store / RAG:** FAISS or ChromaDB
- **Evaluation:** RAGAS, DeepEval, Scikit-learn
- **Metrics:** Accuracy, Precision, Recall, F1 Score, Calibration, Hallucination Rate, Abstention Rate
- **Backend:** FastAPI
- **Frontend:** Streamlit
- **Compute:** Google Colab or Kaggle Notebooks (free GPU)
- **Datasets:** SQuAD 2.0, HotpotQA, AmbigQA

The full pipeline is achievable on free-tier infrastructure with no cost barrier.

## Project Steps

### Phase 1 — Foundation Setup (Week 1)
- Set up Python environment; install LangChain/LlamaIndex, FAISS/ChromaDB, RAGAS, DeepEval, Scikit-learn
- Configure LLM inference (Ollama locally; Groq or Gemini as free-tier hosted fallback)
- Scaffold FastAPI backend and Streamlit frontend
- Set up Colab/Kaggle notebooks for free GPU access
- Download and preprocess SQuAD 2.0, HotpotQA, and AmbigQA
- Consolidate literature review foundations (SAUP, SelfCheckGPT, P(True)/P(IK), SELAUR, UAG)

### Phase 2 — Uncertainty Estimation Module (Weeks 2–3) ⚠️ highest risk
- Implement multi-signal uncertainty estimation: entropy-based scoring, sampling-consistency checks (SelfCheckGPT-style), and confidence estimates (P(True)/P(IK))
- Build an evidence quality scoring component for retrieved context
- Build an ambiguity detection module for underspecified or multi-interpretation queries
- Schedule buffer time here to absorb overrun risk

### Phase 3 — Adaptive Decision Policy Design (Week 4) ⚠️ highest risk
- Design policy logic that jointly weighs uncertainty, evidence quality, ambiguity, and task complexity
- Implement the five agent actions: Answer, Retrieve, Verify, Clarify, Abstain
- Build a threshold-tuning framework (start rule-based, leave room to move to a learned policy)

### Phase 4 — Agent Integration (Week 5)
- Wire the uncertainty estimator and decision policy into a full agent pipeline (LangChain/LlamaIndex)
- Connect retrieval (FAISS/ChromaDB) and a verification step for low-confidence answers
- Expose the agent via the FastAPI backend and Streamlit frontend for interactive testing

### Phase 5 — Baseline Agents (Weeks 5–6)
Implement four baselines for comparison:
- Plain/normal LLM agent (no uncertainty awareness)
- RAG-based agent
- Self-reflection agent
- Fixed-threshold uncertainty agent

### Phase 6 — Comparative Evaluation (Weeks 6–7)
- Run the proposed agent and all four baselines across SQuAD 2.0, HotpotQA, and AmbigQA
- Evaluate with RAGAS and DeepEval, plus accuracy, precision, recall, F1, calibration, hallucination rate, and abstention rate
- Track efficiency metrics: tool-call count, API cost, latency (the reliability–efficiency trade-off)

### Phase 7 — Analysis & Refinement (Week 7)
- Analyze results across agents and datasets; identify failure modes
- Refine decision policy thresholds based on observed calibration and abstention behavior

### Phase 8 — Documentation & Final Write-up (Week 8)
- Compile results and write the final report
- Clean up the repository, finalize this README, prepare a demo/presentation

## Evaluation Summary

The proposed system is benchmarked against normal LLM agents, RAG-based agents, self-reflection agents, and fixed-threshold uncertainty agents, using RAGAS and DeepEval on SQuAD 2.0, HotpotQA, and AmbigQA.

## Status

Currently in the foundation setup phase, with Weeks 2–4 (uncertainty estimation and policy design) flagged as the highest-risk portion of the timeline and protected with schedule buffer.
