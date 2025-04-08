# ============ Stage: Base Python Image =============
FROM python:3.13 AS python-base

ENV POETRY_VERSION=2.1.2
ENV POETRY_HOME=/opt/poetry
ENV POETRY_VENV=/opt/poetry-venv
ENV POETRY_CACHE_DIR=/opt/.cache

# ============ Stage: Poetry Installation ============
FROM python-base AS poetry-base

# Create a separate virtual environment only for Poetry
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install --upgrade pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==$POETRY_VERSION

# ============ Stage: Final App Image ===============
FROM python-base AS clicker-app

# -- 1) Install MySQL client (and clean up apt cache)
RUN apt-get update \
    && apt-get install -y default-mysql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy the Poetry virtualenv from the poetry-base stage
COPY --from=poetry-base ${POETRY_VENV} ${POETRY_VENV}

# Add Poetry to PATH
ENV PATH="${PATH}:${POETRY_VENV}/bin"

# Flask environment variables
ENV FLASK_APP="capybara_clicker.app"
ENV FLASK_PORT=8090

WORKDIR /app

# Copy main dependency files
COPY pyproject.toml poetry.lock ./

# Copy your main python package
COPY capybara_clicker ./capybara_clicker

# Create a fake readme for Poetry validation
RUN touch README.md

# Validate and install dependencies
RUN poetry check
RUN poetry install --no-interaction --no-cache --without dev

# Copy the remainder of your source code
COPY . /app

# Copy your run script to /usr/bin and make it executable
COPY --chmod=755 run_app.sh ./app

# Expose the chosen port
EXPOSE ${FLASK_PORT}

# Run the Flask app via the script
CMD ["/app/run_app.sh"]