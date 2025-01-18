#!/bin/sh

go build -o go_api .
./go_api
#go run main.go

exec "$@"