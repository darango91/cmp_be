# Cuidate Mas Pro - Python Backend Repo

This repository contains the backend code for the Cuidate Mas Pro project. It is built using Python and Django.

## Project Structure

The project is structured as a standard Django project with the following main files:

- `wsgi.py`: This is the entry point for WSGI-compatible web servers to serve your project.
- `urls.py`: This file contains the URL declarations for this Django project.
- `settings.py`: This file contains the settings for this Django project.

## Setup

To set up the project on your local machine, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install [uv](https://docs.astral.sh/uv/) if you haven't already (e.g. `curl -LsSf https://astral.sh/uv/install.sh | sh`).
4. Install the required dependencies with `uv sync`. This creates a `.venv` and installs everything from `uv.lock`.
5. Apply database migrations with `uv run python manage.py migrate`.
6. Run the server with `uv run python manage.py runserver`.

Prefix any management command with `uv run` (e.g. `uv run python manage.py makemigrations`), or activate the environment first with `source .venv/bin/activate`.

## Contributing

If you want to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your features or bug fixes.
3. Commit your changes to your branch.
4. Push your changes to your fork.
5. Open a pull request from your fork to the original repository.

Please note that this is a basic README. Depending on the complexity of your project, you might want to add more sections like 'Testing', 'Deployment', etc.
