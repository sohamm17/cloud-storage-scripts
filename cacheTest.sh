#!/bin/bash

printf "Prepend Caching Experiments"
prependFile="CacheDataPrepend.txt"

for ((min=128; min<=512; min=min*2)); do
	for ((max=1024; max<=1024 && max>min; max=max*2)); do
		for ((i=1; i<=7; i++)); do
			ssh -i copy -oStrictHostKeyChecking=no $1 'rm -f ./.cache/*'
			ssh -i copy -oStrictHostKeyChecking=no $1 'rm -f ./test/*'
			printf "100,$min,$max," >> $prependFile
			jre/bin/java -jar cloud-cache-client.jar file100MB.blob $1 ./test/ 0 $min $max >> $prependFile 2>> CacheTestError.txt &
			PID=$!
			wait $PID
			printf "," >> $prependFile
			ssh -i copy -oStrictHostKeyChecking=no $1 ./cacheSize.sh >> $prependFile
			#printf "\n" >> $prependFile
			printf "100 MB Transferred, $max, $min\n"
			for ((sz=10; sz<=50; sz=sz+10)); do
				./file_gen.sh $sz
				cp file"$sz"MB.blob file1"$sz"MB.blob
				cat file100MB.blob >> file1"$sz"MB.blob
				printf "1$sz,$min,$max," >> $prependFile
				jre/bin/java -jar cloud-cache-client.jar file1"$sz"MB.blob $1 ./test/ 0 $min $max >> $prependFile 2>> CacheTestError.txt &
				PID=$!
				wait $PID
				printf "," >> $prependFile
				ssh -i copy -oStrictHostKeyChecking=no $1 ./cacheSize.sh >> $prependFile
				#printf "\n" >> $prependFile
				printf "1$sz MB Transferred, $max, $min\n"
			done
		done
	done
	printf "$max,$min,One Round Done\n"
done
#SIZE="`du -s --block-size=M "$1" | cut -f1`"
#echo "$SIZE"
#SIZE=${SIZE%M*}
#echo $SIZE
