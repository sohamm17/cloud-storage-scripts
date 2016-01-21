#!/bin/sh

for filename in test2/*; do
    echo -e "\n*****Test is starting for: $filename*****\n"
    rm -f ./test/*
    cp $filename ./test/
    for ((i=0; i<7; i++)); do
        
        filesize=$(stat --printf="%s" $filename)
	filesize=$(($filesize/1048576))

	ssh -i copy tsinghua_mmlab@planetlab5.eecs.umich.edu rm -f "./test/*"
        printf "\n*****remote test folder is cleaned*****\n"

	printf "$filesize " >> OneUMichInter.txt
	TIMEFORMAT="%R"; { time scp -i copy $filename tsinghua_mmlab@planetlab5.eecs.umich.edu:./test/; } 2>> OneUMichInter.txt
        printf "\n*****Intermediate trasnfer to UMich is done*****\n"
	
	(wc -c < $filename) | ssh -i copy tsinghua_mmlab@planetlab5.eecs.umich.edu 'cat > ./currentfileSize.txt' #writing the current file size to read it at the remote place
        ssh -i copy tsinghua_mmlab@planetlab5.eecs.umich.edu jre/bin/java -jar cloud-storage.jar --debug false --deepDebug false --test ./test/ --sepODrFile OneUMichRemote.txt --onlyUp true --all false --sepODrive true --script true --iter 1 --odriveDirect false
        printf "\n*****file uploaded from UMich successfully*****\n"

	sleep 30s	

	ssh -i copy tsinghua_mmlab@planetlab5.eecs.umich.edu rm -f "./test/*"
        printf "\n*****remote test folder is cleaned*****\n"

	printf "$filesize " >> OneUMichInterWorm.txt
	TIMEFORMAT="%R"; { time onehelper-umich.sh $filename; } 2>> OneUMichInterWorm.txt
        printf "\n*****Cut through transfer done*****\n"
	
	sleep 30s

	wc -c < $filename > ./currentfileSize.txt
	jre/bin/java -jar cloud-storage.jar --debug false --deepDebug false --test ./test/ --sepODrFile OneDirectUMich.txt --onlyUp true --all false --sepODrive true --script true --iter 1 --odriveDirect false
	echo -e "\n*****$filename uploaded directly successfully*****\n"
	
	sleep 30s
	
	ssh -i copy tsinghua_mmlab@planetlab5.eecs.umich.edu rm -f "./test/*"
        printf "\n*****remote test folder is cleaned*****\n"
    done
    rm -rf ./test/*
done
