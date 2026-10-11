# agent-lab

Minimal Python calculator used to test the Multica + GitHub + Linear
agent workflow end-to-end.

## Layout
- `src/calc.py` — functions under test
- `tests/test_calc.py` — pytest suite

## Known gap
`subtract()` raises `NotImplementedError`. An issue asks for it to be
implemented so the test suite passes. This repo is a scratch target for
demonstrating agent-driven pull requests.

## Run tests locally
```bash
pip install pytest
python -m pytest
```
