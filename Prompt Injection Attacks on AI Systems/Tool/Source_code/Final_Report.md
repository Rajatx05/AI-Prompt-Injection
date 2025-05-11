# Final Report: Prompt Injection Attacks on AI Systems

## Executive Summary
Prompt injection is a critical vulnerability in LLMs. This project explores the mechanics, risks, and basic defenses.

## Methodology
- Surveyed recent papers
- Developed example attacks
- Built sanitization and output filtering methods
- Created labeled prompt dataset

## Results
- Attacks bypass basic prompt structure easily
- Simple blacklist-based sanitization catches some inputs
- Logistic regression achieves ~90% accuracy on synthetic data

## Conclusion
Prompt injection poses real risks, especially in unrestricted LLM usage. Continued research is essential.

## References
- OpenAI safety documentation
- Microsoft AI Red Team guidelines
- Prompt injection papers (CWE-2022-42890, etc.)
