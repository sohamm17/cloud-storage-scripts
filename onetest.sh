#!/bin/sh

for filename in test2/*; do
    echo -e "\n*****Test is starting for: $filename*****\n"
    rm -f ./test/*
    cp $filename ./test/
    for ((i=0; i<7; i++)); do
	ssh -i copy soham@coldlake.cs.ualberta.ca rm -f "./test/*"
        printf "\n*****remote test folder is cleaned*****\n"

        filesize=$(stat --printf="%s" $filename)
	filesize=$(($filesize/1048576))

	printf "$filesize " >> OneColdInter.txt
	TIMEFORMAT="%R"; { time rsync -e "ssh -i copy" $filename soham@coldlake.cs.ualberta.ca:./test/; } 2>> OneColdInter.txt
        printf "\n*****Intermediate trasnfer is done*****\n"
        
	#ssh -i copy soham@coldlake.cs.ualberta.ca jre/bin/java -jar cloud-storage.jar --debug false --deepDebug false --test ./test/ --sepODFile OneColdRemote.txt --onlyUp true --all false --sepODrive true --script true --iter 1
        #printf "\n*****file uploaded from coldlake successfully*****\n"

	sleep 1m

	ssh -i copy tsinghua_mmlab@planetlab5.eecs.umich.edu rm -f "./test/*"
        printf "\n*****remote test folder is cleaned*****\n"

        filesize=$(stat --printf="%s" $filename)
	filesize=$(($filesize/1048576))

	printf "$filesize " >> OneUMichInter.txt
	TIMEFORMAT="%R"; { time rsync -e "ssh -i copy" $filename tsinghua_mmlab@planetlab5.eecs.umich.edu:./test/; } 2>> OneUMichInter.txt
        printf "\n*****Intermediate trasnfer is done*****\n"
        
	#ssh -i copy tsinghua_mmlab@planetlab5.eecs.umich.edu jre/bin/java -jar cloud-storage.jar --debug false --deepDebug false --test ./test/ --sepODFile OneUMichRemote.txt --onlyUp true --all false --sepODrive true --script true --iter 1
        #printf "\n*****file uploaded from umich successfully*****\n"

	sleep 1m

        jre/bin/java -jar cloud-storage.jar --debug false --deepDebug false --test ./test/ --sepODFile OneDirect.txt --onlyUp true --all false --sepODrive true --script true --iter 1
	echo -e "\n*****$filename uploaded directly successfully*****\n"

	sleep 1m
    done
done
