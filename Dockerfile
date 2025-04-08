FROM python:3.13 as python-base

# https://python-poetry.org/docs#ci-recommendations
ENV POETRY_VERSION=2.1.2
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv

# Tell Poetry where to place its cache and virtual environment
ENV POETRY_CACHE_DIR=/opt/.cache

# Create stage for Poetry installation
FROM python-base as poetry-base

# Creating a virtual environment just for poetry and install it with pip
RUN python3 -m venv $POETRY_VENV \
	&& $POETRY_VENV/bin/pip install -U pip setuptools \
	&& $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

# Create a new stage from the base python image
FROM python-base as clicker-app

# Copy Poetry to app image
COPY --from=poetry-base ${POETRY_VENV} ${POETRY_VENV}

# Add Poetry to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"

# Add flask path
ENV FLASK_APP=capybara_clicker
ENV FLASK_PORT=8090

WORKDIR /app

# Copy Dependencies
COPY poetry.lock pyproject.toml ./

# Copy python project
COPY capybara_clicker ./capybara_clicker

# Create fake readme for poetry
RUN touch README.md

# [OPTIONAL] Validate the project is properly configured
RUN poetry check

# Install Dependencies
RUN poetry install --no-interaction --no-cache --without dev

# Copy Application
COPY . /app

# Run Flask at port 5000
EXPOSE ${FLASK_PORT}
CMD [ "poetry", "run", "python", "-m", "flask", "run", "--host=0.0.0.0", "--port=${FLASK_PORT}"]