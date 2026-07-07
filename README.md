# LLM-as-Judge Evaluation Pipeline

A production-style evaluation pipeline that uses a Large Language Model (LLM) as an automated judge to evaluate AI-generated responses. The system generates structured verdicts, compares multiple configurations, measures evaluation quality, detects judge bias, and produces detailed evaluation reports.

---

# Features

- Structured LLM judging pipeline
- Explicit multi-criterion evaluation rubric
- Pointwise evaluation
- Pairwise A/B comparison
- Position bias detection
- Adversarial probe evaluation
- Robust JSON parsing with malformed JSON recovery
- Pydantic schema validation
- Prompt and raw response logging
- Token usage tracking
- Latency tracking
- Test-retest consistency evaluation
- Score distribution analysis
- Configurable judge model
- Environment variable support

---

# Project Structure

```
llm-as-judge/
│
├── app/
│   ├── bias.py
│   ├── comparison.py
│   ├── config.py
│   ├── judge.py
│   ├── logger.py
│   ├── parser.py
│   ├── prompts.py
│   ├── report.py
│   └── schemas.py
│
├── evaluation/
│   ├── reports/
│   ├── test_suites/
│   ├── answer_validate.py
│   ├── score_distribution.py
│   └── test_retest.py
│
├── logs/
│
├── compare_configs.py
├── run_suite.py
├── requirements.txt
├── README.md
└── .env
```

---

# Architecture

```
Test Suite
      │
      ▼
Judge Prompt Builder
      │
      ▼
Gemini Judge
      │
      ▼
Raw JSON Response
      │
      ▼
JSON Recovery
      │
      ▼
Schema Validation
      │
      ▼
Structured Verdict
      │
      ▼
Evaluation Report
```

---

# Evaluation Rubric

Each response is scored on:

- Correctness
- Faithfulness
- Completeness
- Instruction Following
- Tone & Safety

Each criterion receives:

- Score
- Rationale

The judge also returns:

- Overall Score
- Pass / Fail
- Summary

---

# Bias Handling

The project implements several bias mitigation strategies:

## Position Bias

- Pairwise comparison
- Forward and reverse ordering
- Flip rate calculation

## Verbosity Bias

- Verbose-but-wrong probe
- Terse-but-correct probe

## Sycophancy

- Confidently incorrect answers
- Style-based probe evaluation

## Judge Validation

- Test-retest consistency
- Adversarial evaluation
- Score distribution analysis

---

# Running the Project

## Install

```bash
pip install -r requirements.txt
```

## Run Evaluation Suite

```bash
python run_suite.py
```

## Compare Configurations

```bash
python compare_configs.py
```

## Judge Validation

```bash
python -m evaluation.answer_validate
```

## Test-Retest

```bash
python -m evaluation.test_retest
```

## Score Distribution

```bash
python -m evaluation.score_distribution
```

---

# Configuration

Environment variables:

```
GEMINI_API_KEY
JUDGE_MODEL
```

---

# Results

The evaluation pipeline generates:

- Structured verdicts
- Evaluation reports
- Config A vs Config B comparison
- Pass rate
- Mean score
- Position bias metrics
- Token usage
- Latency metrics

---

# Future Improvements

- Multiple judge models
- Judge ensembles
- Cohen's Kappa evaluation
- YAML test suite support
- Web dashboard
- Human-in-the-loop review
- Additional bias detection techniques

---

# Technologies Used

- Python
- Google Gemini API
- Pydantic
- JSON
- Logging
- dotenv
