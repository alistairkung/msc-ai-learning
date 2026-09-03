# Proposed topic-based repository structure

This branch is a structural draft for review before changing `main`.

## Design rules

1. Organise implementation/test files by **knowledge domain and topic**, not by chronology alone.
2. Preserve lesson identity in filenames: `lessonNN_topic.py` and `test_lessonNN_topic.py` remain a 1:1 learning pair.
3. Keep `lesson_logs/` chronological and centralised. A lesson log answers *when/how did I learn this?*; the topic folders answer *where does this knowledge live?*
4. Do not create one tiny directory per lesson. A topic directory may contain several lesson/test pairs as the learner revisits a subject.
5. Larger MSc projects can later use normal `src/` + `tests/` project structure rather than the lesson convention.

## Proposed domains

```text
foundations/
  python/
  dsa/
  numpy/
  pandas/
  retrieval/

machine_learning/
  fundamentals/
  classification/
  regression/

classical_ai/
  search/

deep_learning/
  tensor_operations/
  autograd/
  pytorch_fundamentals/
  mlp/

lesson_logs/       # unchanged chronological record
```

Future topics such as trees, probabilistic models, reinforcement learning, CNN/RNN, ML theory and projects should be added when actual learning material exists rather than pre-populating empty directories.

## Draft status

This PR intentionally focuses first on whether the taxonomy feels right. Existing test imports were written against the old flat `exercises.*` package and therefore need to be rewritten to the new module paths before this PR should be merged. No learning implementation has been rewritten as part of the structural move.
