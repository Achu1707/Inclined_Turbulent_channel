#!/bin/bash

# path to seeder executable
seeder_path=~/apes/seeder/build/seeder
# path to musubi executable
musubi_path=~/apes/musubi/build/musubi
# path to execute harvester
harvester_path=~/apes/seeder/build/sdr_harvesting

# Remove old directories
rm -rf tracking mesh restart output *.db

# Create directories for Seeder and Musubi output
mkdir mesh tracking restart output

# Run Seeder
$seeder_path seeder.lua
# Run Harvester
$harvester_path sdr_harvester.lua

# Run Musubi
mpirun --oversubscribe -np 4 $musubi_path musubi.lua
# Create plots
#python plot_track.py
