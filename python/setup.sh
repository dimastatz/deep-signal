#!/bin/bash

abort()
{
    echo "*** FAILED ***" >&2
    exit 1
}

if [ "$#" -eq 0 ]; then
    echo "No arguments provided. Usage: 
    1. '-local' to build local environment
    2. '-docker' to build and run docker container
    3. '-test' to run linter, formatter and tests"

elif [ $1 = "-local" ]; then
    trap 'abort' 0
    set -e
    echo "Running format, linter and tests"
    rm -rf .venv
    python3 -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r ./requirements.txt

    black deep-signal tests
    pylint --fail-under=9.9 deep-signal tests
    pytest --cov-fail-under=95 --cov deep-signal -v tests

elif [ $1 = "-test" ]; then
    trap 'abort' 0
    set -e
    
    echo "Running format, linter and tests"
    source .venv/bin/activate
    black deep-signal tests
    pylint --fail-under=9.9 deep-signal tests
    pytest --cov-fail-under=95 --cov --log-cli-level=INFO deep-signal -v tests

elif [ $1 = "-docker" ]; then
    echo "Building and running docker image"
    docker stop deep-signal-container
    docker rm deep-signal-container
    docker rmi deep-signal-image
    # build docker and run
    docker build --tag deep-signal-image --build-arg CACHEBUST=$(date +%s) .
    docker run --name deep-signal-container -p 8888:8888 -d deep-signal-image

else
  echo "Wrong argument is provided. Usage:
    1. '-local' to build local environment
    2. '-docker' to build and run docker container
    3. '-test' to run linter, formatter and tests"
fi

trap : 0
echo >&2 '*** DONE ***'