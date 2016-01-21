#!/bin/sh

scp -i copy $1 soham@coldlake.cs.ualberta.ca:./test/ &
sleep 1s
ssh -i copy soham@coldlake.cs.ualberta.ca jre/bin/java -jar cloud-storage.jar --debug false --deepDebug false --test ./test/ --sepODrFile OneUMichRemoteCutThrough.txt --onlyUp true --all false --sepODrive true --script true --iter 1 --odriveDirect false
