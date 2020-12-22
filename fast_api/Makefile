# pipでの依存関係の解決 (.pipディレクトリに依存関係を全て入れる)
setup:
	pip3 install --upgrade pip
	pip3 install -r requirements.txt -t ./.pip
	
test:
	python -m pytest -v