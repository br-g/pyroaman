install:
	python3 -m pip install -U -r requirements.txt

test:
	python3 -m pip install pytest pytest-cov
	pytest -s --cov=pyroaman tests/

type_check:
	python3 -m pip install mypy
	mypy pyroaman/

lint:
	python3 -m pip install pylint
	pylint --disable=missing-docstring pyroaman/
