# Calculus foundations — historical chat-based sequence

This directory records the calculus foundation that was learned interactively in chat **before the repository's numbered lesson workflow was established**.

These sessions are intentionally **not retroactively assigned numbered lessons**. Lessons 01–31 describe the repository's existing implementation chronology; inventing earlier lesson numbers would make that history misleading.

The durable conceptual/retrieval record is:

- `lesson_logs/historical_calculus_foundations.md`

## Reconstructed learning arc

```text
change between two points
→ slope between two points
→ slope at a point
→ intuitive limit / shrinking Δx
→ derivative as local rate of change
→ power rule
→ product rule
→ partial derivatives
→ gradient as a vector of local sensitivities
→ gradient-descent update
→ chain rule through nested functions
→ manual backpropagation
→ Lesson 28: PyTorch autograd + manual gradient descent
```

The central teaching aim was not symbolic-calculus breadth. It was to build enough calculus intuition to understand **why gradient-based machine learning works**, then connect that intuition to executable ML code.

## Evidence boundary

This is a historical reconstruction from recoverable tutoring context and the later learning-state/roadmap records. It is **not a transcript** and should not be treated as evidence that every possible calculus subtopic was covered.

No exercise/test pair is fabricated for these sessions because the original work was primarily conversational and pen-and-paper. Lesson 28 is the point where this conceptual foundation becomes directly represented by repository code and tests.
