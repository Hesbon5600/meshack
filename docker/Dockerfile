FROM python:3.10-alpine

ENV MICRO_SERVICE=/portfolio-app
# set work directory


RUN mkdir -p $MICRO_SERVICE

# where the code lives
WORKDIR $MICRO_SERVICE

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# The default user that should be used
ARG USER_ID=1000
ARG GROUP_ID=1000
ARG APP_USER=appuser

# Create user and group
RUN addgroup -g ${GROUP_ID} ${APP_USER} && adduser -D -u ${USER_ID} -G ${APP_USER} -s /bin/sh ${APP_USER}

# Install build dependencies
RUN apk add --no-cache \
    build-base \
    python3-dev \
    libffi-dev \
    openssl-dev \
    postgresql-dev \
    musl-dev \
    cargo \
    curl \
    ca-certificates \
    gcc

# Upgrade pip
RUN python -m pip install --upgrade pip setuptools wheel

ENV POETRY_VERSION=2.1.3

# install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

COPY ./poetry.lock $MICRO_SERVICE
COPY ./pyproject.toml $MICRO_SERVICE

# install dependencies
RUN poetry config virtualenvs.create false

RUN poetry install


RUN chown -R ${APP_USER}:${APP_USER} /root
RUN chmod 755 /root

# copy project
COPY --chown=${APP_USER}:${APP_USER} . $MICRO_SERVICE

RUN mkdir -p $MICRO_SERVICE/staticfiles

RUN chmod -R a+rwx $MICRO_SERVICE

# Set the default user
USER ${APP_USER}

CMD ["/bin/sh", "-c", "/portfolio-app/docker/start_api.sh"]
