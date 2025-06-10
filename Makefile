PYTHON=python3
VENV=.venv

.PHONY: venv check-fmt check-tests check-all clean

venv:
	$(PYTHON) -m venv $(VENV)
	. $(VENV)/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

check-fmt:
	. $(VENV)/bin/activate && black --check core main.py

check-tests:
	. $(VENV)/bin/activate && pytest tests/ -v --cov=core

check-all: check-fmt check-tests

clean:
	rm -rf __pycache__ core/**/__pycache__ tests/**/__pycache__
	rm -rf .pytest_cache .coverage htmlcov
	rm -rf $(VENV) 