#!/bin/bash

curl -i http://127.0.0.1:8000/ && \
curl -i http://127.0.0.1:8000/this_is_a_404 && \
curl -i http://127.0.0.1:8000/manage_file && \
curl -i -H "Content-Type: application/json" -X POST -d '{"axion":"read"}' http://127.0.0.1:8000/manage_file && \
curl -i -H "Content-Type: application/json" -X POST -d '{"axion":"read","action":"read"}' http://127.0.0.1:8000/manage_file && \
curl -i -H "Content-Type: application/json" -X POST -d '{"action":"read"}' http://127.0.0.1:8000/manage_file && \
curl -i -H "Content-Type: application/json" -X POST -d '{"action":"download"}' http://127.0.0.1:8000/manage_file && \
curl -i -H "Content-Type: application/json" -X POST -d '{"action":"read"}' http://127.0.0.1:8000/manage_file 
