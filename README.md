# botlogistics
Repository for various logistics services to run on guadr.gonzaga.edu webserver.
The scripts are all ran using a single systemd service. If you're interested in linux, systemd is worth learning about. They provide extensive documentation, tutorials, and manuals [here](https://www.freedesktop.org/wiki/Software/systemd/). 

## Requirements
### ØMQ python bindings
```bash
pip install pyzmq
```

### Create a systemd unit file

create a unit description file in the directiory: ~/.config/systemd/user/
```bash
# make this directory if it does not exist
mkdir -p ~/.config/systemd/user/
```

Within the above directory create a file called botlogistics.service and write the following to the file
```INI
[Unit]
Description=Service for bot tracking and order planning scripts

[Service]
ExecStart=/usr/bin/env bash /home/lhartman3/botlogistics/run.sh

[Install]
WantedBy=default.target
```

You can read more about systemd unit files [here](https://www.freedesktop.org/software/systemd/man/systemd.unit.html)


## Directory Structure
	overview of files in this repo
		.
		├── planning                # contains all services related to planning
		│   ├── planner.py          # given current order queue and fleet status, plan orders
		│   └── queuer.py           # maintain an order queue
		├── README.md
		├── run.sh                  # scripts to run logistics services
		└── tracking                # contains all services related to tracking
			├── fleet.py            # zmq and server that maintains and updates fleet state
			├── listener.py         # zmq server and client to listen to updater and update fleet, respectively
			├── run_listener.py     # script to test listener
			├── run_updater.py      # script to test updater
			└── updater.py          # updated listens to cars for updates and posts to listener server


## Usage
Run all scripts using systemd
```bash
systemctl --user start botlogistics.service
```
