#!/bin/bash
#This script sends a JSON POST request to a URL passed as the first argument
curl -s -H "Contetn-Type: application/json" -d @$2 $1
