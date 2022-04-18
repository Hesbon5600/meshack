FROM python:3.10-slim

ENV MICRO_SERVICE=/portfolio-app
# set work directory


RUN mkdir -p $MICRO_SERVICE

# where the code lives
WORKDIR $MICRO_SERVICE

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# The default user that should be used
ARG USER_ID=1000
ARG GROUP_ID=1000
ARG APP_USER=appuser

# Create user and group
RUN groupadd -g ${GROUP_ID} ${APP_USER} && useradd -u ${USER_ID} -g ${APP_USER} -s /bin/sh ${APP_USER}

# Install ca certificates
RUN apt-get update \
    && apt-get install curl ca-certificates -y --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip


COPY ./poetry.lock $MICRO_SERVICE
COPY ./pyproject.toml $MICRO_SERVICE

# install dependencies
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH /root/.local/bin:$PATH

RUN poetry config virtualenvs.create false

RUN poetry install --no-dev


RUN chown -R ${APP_USER}:${APP_USER} /root
RUN chmod 755 /root

# copy project
COPY --chown=${APP_USER}:${APP_USER} . $MICRO_SERVICE

RUN mkdir -p $MICRO_SERVICE/staticfiles

RUN chmod -R a+rwx $MICRO_SERVICE

# Set the default user
USER ${APP_USER}


CMD ["/bin/bash", "-c", "/portfolio-app/docker/start_api.sh"]
