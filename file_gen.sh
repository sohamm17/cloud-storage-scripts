#!/bin/bash

echo -e "\n Creating file ..."
a="/home/sohamgrad/workspace/DropBox/"
#for k in `seq 1 10`;
#do
     dd if=/dev/urandom of="${a}file500MB.blob" bs=1048576 count=500 >/dev/null 2>&1
#done

echo -e "\n End!"
