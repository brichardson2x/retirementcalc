#!/bin/bash


docker stop retirementcalc
docker rm retirementcalc
docker pull ${{ secrets.DOCKER_USERNAME }}/retirementcalc:latest
docker run -d --name retirementcalc -p 80:8080 ${{ secrets.DOCKER_USERNAME }}/retirementcalc:latest