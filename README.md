# UX Research Toolkit

Ready-to-use templates and small tools for running usability studies. Built from practice: these are the documents I actually use when planning tests, evaluating interfaces, and reporting findings.

## Templates

| File | What it is |
| ---- | ---------- |
| `templates/usability-test-plan.md` | Full test plan: goals, participants, tasks, metrics, schedule |
| `templates/task-scenarios.md` | How to write task scenarios that do not lead the participant |
| `templates/heuristic-evaluation.md` | Heuristic evaluation worksheet based on Nielsen's 10 heuristics |
| `templates/sus-questionnaire.md` | The 10-item System Usability Scale questionnaire |
| `templates/consent-form.md` | Participant consent form template for usability sessions |
| `templates/findings-report.md` | Structure for reporting findings with severity ratings |

## Tools

| File | What it does |
| ---- | ------------ |
| `tools/sus_scorer.py` | Scores SUS questionnaires from a CSV file (Python, standard library only) |
| `tools/sus-calculator.html` | Interactive SUS calculator that runs in the browser, no setup needed (HTML + CSS + JS) |

## Quick start

Score a batch of SUS responses:

```bash
python3 tools/sus_scorer.py responses.csv
```

Or open `tools/sus-calculator.html` in any browser for a single questionnaire.

## Background

The System Usability Scale (SUS) is a 10-item questionnaire (Brooke, 1996) that produces a score from 0 to 100. A score above 68 is generally considered above average. The scoring implemented here follows the published method: odd-numbered items contribute (response - 1), even-numbered items contribute (5 - response), and the total is multiplied by 2.5.
