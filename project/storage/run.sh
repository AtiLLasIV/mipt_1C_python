#!/bin/bash
docker build -t my_postgres .
docker run -d --rm --name pg_container -p 5432:5432 my_postgres