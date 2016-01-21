#!/bin/sh

scp -i copy $1 tsinghua_mmlab@planetlab5.eecs.umich.edu:./test/ &
sleep 1s
ssh -i copy tsinghua_mmlab@planetlab5.eecs.umich.edu jre/bin/java -jar cloud-storage.jar --debug false --deepDebug false --test ./test/ --sepDrFile DropUMichRemoteCutThrough.txt --onlyUp true --all false --sepDrop true --script true --iter 1 --dropDirect false
