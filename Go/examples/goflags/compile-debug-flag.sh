#!/bin/bash/
go build -o daemon_debug daemon/daemon.go
go build -ldflags="-w -s" -o daemon_no_debug daemon/daemon.go
