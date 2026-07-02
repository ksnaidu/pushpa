#!/bin/bash

MOVIES=("RRR", "pushpa", "HIT")

echo "First movie: ${MOVIES[0]}"
echo "last movie: ${MOVIES[2]}"
echo "last movie: ${MOVIES[3]}"

echo "All movies: ${MOVIES[@]}"

##Sort the array

SORTED_MOVIES=($(printf "%s\n" "${MOVIES[@]))"

echo "All movies in alphabetical order:"
echo "${SORTED_MOVIES[@]}"


## special varaibles in shell:

if you want all varaibles passed to script:  $@
Number of variables passed: $#
Script name: $0
Present working Directory: $PWD
Home directory of the user who is running the script: $HOME
which user is running the script: $USER
PID of the current user:  $$
PID of the last command running in background: $!