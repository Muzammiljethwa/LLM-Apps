<!-- first install poetry -->
pip install poetry

<!-- config venv to be saved in local dir -->
poetry config virtualenvs.in-project true

<!-- activate venv -->
poetry shell

<!-- install dependencies -->
poetry install

<!-- to add new package > alternative to pip install -->
poetry add <package-name>

<!-- run file  -->
python run app.py

<!-- exit poetry shell/ env -->
exit