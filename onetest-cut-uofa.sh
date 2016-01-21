#!/bin/sh

for filename in test2/*; do
    echo -e "\n*****Test is starting for: $filename*****\n"
    rm -f ./test/*
    cp $filename ./test/
    for ((i=0; i<7; i++)); do
        
        filesize=$(stat --printf="%s" $filename)
	filesize=$(($filesize/1048576))

	ssh -i copy soham@coldlake.cs.ualberta.ca rm -f "./test/*"
        printf "\n*****remote test folder is cleaned*****\n"

	printf "$filesize " >> OneUofAInter.txt
	TIMEFORMAT="%R"; { time scp -i copy $filename soham@coldlake.cs.ualberta.ca:./test/; } 2>> OneUofAInter.txt
        printf "\n*****Intermediate trasnfer to UofA is done*****\n"
	
	(wc -c < $filename) | ssh -i copy soham@coldlake.cs.ualberta.ca 'cat > ./currentfileSize.txt' #writing the current file size to read it at the remote place
        ssh -i copy soham@coldlake.cs.ualberta.ca jre/bin/java -jar cloud-storage.jar --debug false --deepDebug false --test ./test/ --sepODrFile OneUofARemote.txt --onlyUp true --all false --sepODrive true --script true --iter 1 --odriveDirect false
        printf "\n*****file uploaded from UofA successfully*****\n"

	sleep 30s	

	ssh -i copy soham@coldlake.cs.ualberta.ca rm -f "./test/*"
        printf "\n*****remote test folder is cleaned*****\n"

	printf "$filesize " >> OneUofAInterWorm.txt
	TIMEFORMAT="%R"; { time onehelper-uofa.sh $filename; } 2>> OneUofAInterWorm.txt
        printf "\n*****Cut through transfer done*****\n"
	
	sleep 30s

	wc -c < $filename > ./currentfileSize.txt
	jre/bin/java -jar cloud-storage.jar --debug false --deepDebug false --test ./test/ --sepODrFile OneDirectUofA.txt --onlyUp true --all false --sepODrive true --script true --iter 1 --odriveDirect false
	echo -e "\n*****$filename uploaded directly successfully*****\n"
	
	sleep 30s
	
	ssh -i copy soham@coldlake.cs.ualberta.ca rm -f "./test/*"
        printf "\n*****remote test folder is cleaned*****\n"
    done
    rm -rf ./test/*
done
