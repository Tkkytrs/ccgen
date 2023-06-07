#!/bin/bash

# Define the command mappings
declare -A command_mapping
command_mapping["--tkkytrs-bin-chk"]=".cmds/bin.py"
command_mapping["--tkkytrs-cc-gen"]=".cmds/gen.py"
command_mapping["--tkkytrs-cc-live"]=".cmds/live.py"
command_mapping["--tkkytrs-cc-chkout"]=".cmds/ckout.py"

# Check if a command argument is provided
if [[ $# -gt 0 ]]; then
    # Get the command argument
    command=$1

    # Check if the command exists in the mapping
    if [[ -v command_mapping["$command"] ]]; then
        # Get the file path associated with the command
        file_path=${command_mapping["$command"]}

        # Check if the file exists
        if [[ -f $file_path ]]; then
            # Execute the file
            python3 "$file_path"
        else
            echo "File does not exist: $file_path"
        fi
    else
        echo "Invalid command: $command"
    fi
else
    echo "No command provided."
fi
