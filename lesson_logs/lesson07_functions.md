# Lesson 07 — Function Arguments

_Status: reconstructed retrospectively from repo + recoverable chat history_

## Curriculum role

This lesson rounded out the initial Python-fundamentals block by making function signatures more expressive: defaults, keyword-only arguments, variable positional arguments and variable keyword arguments.

## What was implemented

Source: `foundations/python/lesson07_functions.py` + `foundations/python/test_lesson07_functions.py`.

Exercises covered:
- default parameter values;
- overriding defaults;
- keyword-only arguments using `*`;
- `*args` for an arbitrary number of positional values;
- `**kwargs` for arbitrary named values.

Representative forms:

```python
def greet(name, language="English"):
    ...


def describe_person(*, name, age):
    ...


def total(*numbers):
    ...


def build_profile(**kwargs):
    ...
```

## Core concepts

- Default arguments make common calls concise while still permitting overrides.
- A bare `*` in a signature makes following parameters keyword-only.
- `*args` arrives inside the function as a tuple.
- `**kwargs` arrives as a dictionary.
- Function signatures are part of API design: they communicate which arguments are optional, positional, or required by name.

## Chat-history context

Recoverable history explicitly lists defaults, `*args`, and `**kwargs` among the early Python exercises. Given the learner's backend/API background, the useful framing is function-signature design rather than beginner syntax drills.

## Cold-retrieval question bank

1. What happens when a caller omits a parameter that has a default value?
2. What does the `*` mean in `def f(*, name, age)`?
3. What type is `numbers` inside `def total(*numbers)`?
4. What type is `kwargs` inside `def build_profile(**kwargs)`?
5. When might keyword-only arguments make an API safer/readable?
6. Write a function with a default exponent of 2 but allow callers to override it.
7. Contrast `*args` with passing one list argument.
8. Contrast `**kwargs` with passing one dictionary argument.

## Retrieval blueprint

1. default argument;
2. keyword-only argument;
3. `*args`;
4. `**kwargs`;
5. explain why signatures matter for API clarity.

## Mastery signal

The learner can read unfamiliar Python signatures containing defaults, `*`, `*args`, and `**kwargs` without hesitation and can choose an appropriate form when designing small APIs.
