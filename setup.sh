#!/bin/bash


make clean
docker compose build
make up
echo "##############################"
echo "setup complete"
echo "##############################"
