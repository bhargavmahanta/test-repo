# FailCapsule Green-Run Demo

A deliberately tiny, healthy Python project used to demonstrate a **successful**
FailCapsule job (status `success`, exit code `0`).

It matches FailCapsule's supported layout:

- `requirements.txt` at the repository root (installed by the setup stage)
- `tests/test_calculator.py` collected by `python -m pytest -q`

## Run locally

```bash
python -m pip install -r requirements.txt
python -m pytest -q
```

Expected: all tests pass.
