#!/bin/sh

scp -i copy $1 tsinghua_mmlab@planetlab5.eecs.umich.edu:./test/ &
sleep 1s
ssh -i copy tsinghua_mmlab@planetlab5.eecs.umich.edu jre/bin/java -jar cloud-storage.jar --debug false --deepDebug false --test ./test/ --sepODrFile OneUMichRemoteCutThrough.txt --onlyUp true --all false --sepODrive true --script true --iter 1 --odriveDirect false
