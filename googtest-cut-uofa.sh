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

	printf "$filesize " >> GoogUofAInter.txt
	TIMEFORMAT="%R"; { time scp -i copy $filename soham@coldlake.cs.ualberta.ca:./test/; } 2>> GoogUofAInter.txt
        printf "\n*****Intermediate trasnfer to UofA is done*****\n"
	
	(wc -c < $filename) | ssh -i copy soham@coldlake.cs.ualberta.ca 'cat > ./currentfileSize.txt' #writing the current file size to read it at the remote place
        ssh -i copy soham@coldlake.cs.ualberta.ca jre/bin/java -jar cloud-storage.jar --debug false --deepDebug false --test ./test/ --sepGFile GoogUofARemote.txt --onlyUp true --all false --sepGoogle true --script true --iter 1 --googDirect false
        printf "\n*****file uploaded from UofA successfully*****\n"

	sleep 30s	

	ssh -i copy soham@coldlake.cs.ualberta.ca rm -f "./test/*"
        printf "\n*****remote test folder is cleaned*****\n"

	printf "$filesize " >> GoogUofAInterWorm.txt
	TIMEFORMAT="%R"; { time googhelper-uofa.sh $filename; } 2>> GoogUofAInterWorm.txt
        printf "\n*****Cut through transfer done*****\n"
	
	sleep 30s

	wc -c < $filename > ./currentfileSize.txt
	jre/bin/java -jar cloud-storage.jar --debug false --deepDebug false --test ./test/ --sepGFile GoogDirectUofA.txt --onlyUp true --all false --sepGoogle true --script true --iter 1 --googDirect false
	echo -e "\n*****$filename uploaded directly successfully*****\n"
	
	sleep 30s
	
	ssh -i copy soham@coldlake.cs.ualberta.ca rm -f "./test/*"
        printf "\n*****remote test folder is cleaned*****\n"
    done
    rm -rf ./test/*
done
