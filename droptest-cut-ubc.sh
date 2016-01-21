#!/bin/sh

for filename in test2/*; do
    echo -e "\n*****Test is starting for: $filename*****\n"
    rm -f ./test/*
    cp $filename ./test/
    for ((i=0; i<7; i++)); do
        
        filesize=$(stat --printf="%s" $filename)
	filesize=$(($filesize/1048576))

	ssh -i copy tsinghua_mmlab@planetlab2.cs.ubc.ca rm -f "./test/*"
        printf "\n*****remote test folder is cleaned*****\n"

	printf "$filesize " >> DropUBCInter.txt
	TIMEFORMAT="%R"; { time scp -i copy $filename tsinghua_mmlab@planetlab2.cs.ubc.ca:./test/; } 2>> DropUBCInter.txt
        printf "\n*****Intermediate trasnfer to UBC is done*****\n"
	
        ssh -i copy tsinghua_mmlab@planetlab2.cs.ubc.ca jre/bin/java -jar cloud-storage.jar --debug false --deepDebug false --test ./test/ --sepDrFile DropUBCRemote.txt --onlyUp true --all false --sepDrop true --script true --iter 1 --dropDirect false
        printf "\n*****file uploaded from UBC successfully*****\n"

	sleep 30s	

	ssh -i copy tsinghua_mmlab@planetlab2.cs.ubc.ca rm -f "./test/*"
        printf "\n*****remote test folder is cleaned*****\n"

	printf "$filesize " >> DropUBCInterWorm.txt
	TIMEFORMAT="%R"; { time helper-ubc.sh $filename; } 2>> DropUBCInterWorm.txt
        printf "\n*****Cut through transfer done*****\n"
	
	sleep 30s

	jre/bin/java -jar cloud-storage.jar --debug false --deepDebug false --test ./test/ --sepDrFile DropDirectUBC.txt --onlyUp true --all false --sepDrop true --script true --iter 1 --dropDirect false
	echo -e "\n*****$filename uploaded directly successfully*****\n"
	
	sleep 30s
	
	ssh -i copy tsinghua_mmlab@planetlab2.cs.ubc.ca rm -f "./test/*"
        printf "\n*****remote test folder is cleaned*****\n"
    done
    rm -rf ./test/*
done
