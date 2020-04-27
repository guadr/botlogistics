#!/bin/sh
# script to run all logistics services
echo "running tracking services";
python3 tracking/run_listener.py &
python3 tracking/run_updater.py &
python3 tracking/fleet.py;

