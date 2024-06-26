poetry-config-list:
	poetry config --list
mypy:
	mypy .
ruff:
	ruff check .
ruff-fix:
	ruff check --fix .
pre-push: mypy ruff
install-linting-req:
	pip3 install -r requirements-linting.txt
install-testing-req:
	pip3 install -r requirements-testing.txt
install-req:
	pip3 install -r requirements.txt
upgrade-pip:
	pip3 install --upgrade pip
venv-remove:
	rm -rf .venv
venv-activate:
	source .venv/bin/activate
venv-setup:
	python3 -m venv .venv
clean-package:
	rm -Rf ./build; rm -Rf ./dist; rm -Rf ./.eggs; rm -Rf ./*.egg-info; rm -Rf ./**/*.egg-info; rm -Rf ./.coverage; 
clean-pycache:
	rm -Rf ./.pytest_cache; rm -Rf ./**/__pycache__; rm -Rf ./**/**/__pycache__; rm -Rf ./**/**/**/__pycache__; rm -Rf ./**/**/**/**/__pycache__;rm -Rf ./**/**/**/**/**/__pycache__;rm -Rf ./**/**/**/**/**/**/__pycache__;
clean: clean-package clean-pycache
install-dev-req: upgrade-pip install-linting-req install-testing-req install-req
install-prod-req: upgrade-pip install-req
run-dev-server:
	python3 src/main.py
run-new-server:
	python3 src/main_new.py