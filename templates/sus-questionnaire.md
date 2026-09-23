# System Usability Scale (SUS) Questionnaire

Give this to participants after the session. Ask them to respond quickly, without overthinking. Each item is answered on a scale from 1 (strongly disagree) to 5 (strongly agree).

1. I think that I would like to use this system frequently.
2. I found the system unnecessarily complex.
3. I thought the system was easy to use.
4. I think that I would need the support of a technical person to be able to use this system.
5. I found the various functions in this system were well integrated.
6. I thought there was too much inconsistency in this system.
7. I would imagine that most people would learn to use this system very quickly.
8. I found the system very cumbersome to use.
9. I felt very confident using the system.
10. I needed to learn a lot of things before I could get going with this system.

## Scoring

- Odd-numbered items: score contribution = response - 1
- Even-numbered items: score contribution = 5 - response
- Add the contributions and multiply by 2.5 for a score from 0 to 100

A score above 68 is generally considered above average. Use `tools/sus_scorer.py` in this repo to score a batch of responses, or open `tools/sus-calculator.html` in a browser for a single questionnaire.

Source: Brooke, J. (1996). SUS: A "quick and dirty" usability scale. In P. W. Jordan et al. (Eds.), *Usability Evaluation in Industry*.
