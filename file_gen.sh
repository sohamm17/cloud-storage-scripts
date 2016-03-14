#!/bin/bash

echo -e "\n Creating file ..."
a="./"
#for k in `seq 1 10`;
#do
     dd if=/dev/urandom of="${a}file$1MB.blob" bs=1048576 count=$1 >/dev/null 2>&1
#done

echo -e "\n End!"
