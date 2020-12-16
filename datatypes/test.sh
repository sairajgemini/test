#!/usr/bin/env bash

directory="Test"

if [ ! -d $directory ]; then
  mkdir $directory
else
  echo "Directory exists"
fi
