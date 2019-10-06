#!/bin/bash

echo "This might take a while.."
cat /dev/urandom | grep -a --color=always "Hello world!"
