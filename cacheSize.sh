#!/bin/bash

SIZE="`du -s --block-size=M ./.cache | cut -f1`"
SIZE=${SIZE%M*}
echo $SIZE
