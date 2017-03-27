#!/bin/bash

ifconfig_vcan0=$(echo $(ifconfig) | grep "vcan0")
if [ "${ifconfig_vcan0}" == "" ]; then
	sudo ip link add name vcan0 type vcan
	sudo ifconfig vcan0 up
fi

mkfifo vcanlog