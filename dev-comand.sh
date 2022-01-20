#!/bin/bash

# COMMAND=$1
# ARGS=$2

export COMPOSE_FILE=local.yml

delete_migrations(){
  local app=$1

  sudo find ./bk_service/$app/migrations/* -delete
  sudo touch ./bk_service/$app/migrations/__init__.py
}

while getopts c:a:d:f: options; do
  case $options in
      c) COMMAND=$OPTARG;;
      a) ARGS=$OPTARG;;
      d) DIR=$OPTARG;;
      f) FUNTION=$OPTARG;;

  esac
done

echo "COMMAND = $COMMAND; ARGS = $ARGS ; DIR = $DIR ; FUNTION = $FUNTION"

case $COMMAND in
  "loaddata")
    echo "loading data..."
    python manage.py loaddata flights/fixtures/airport.json
    python manage.py loaddata flights/fixtures/airline.json
    python manage.py loaddata flights/fixtures/agent.json
    python manage.py loaddata flights/fixtures/itinerary.json
    python manage.py loaddata flights/fixtures/leg.json
    #echo "from django.contrib.auth import get_user_model ; User = get_user_model(); User.objects.create_superuser(username='admin' , email='admin@admin.com', password='admin1234')" | python manage.py shell 
    ;;
  *)

    echo "command $COMMAND no found:"
    echo ""
    echo "The available commands:"
    echo ""

    echo -e "- loaddata"
    echo -e "- run-env"
    echo -e "- clear-db"

esac






