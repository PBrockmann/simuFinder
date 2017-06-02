#!/bin/bash

server='https://vesg.ipsl.upmc.fr/thredds/catalog/work_thredds'

echo 'var input = `'

for dir in `ls -d1 /ccc/work/cont003/thredds/p86caub/*/*/*/*/MONITORING`; do
#for dir in `ls -d1 /ccc/work/cont003/thredds/*/*/*/*/*/MONITORING`; do

	nb=`ls $dir/files | wc -l`
	if [[ $nb -ne 0 ]] ; then
		base=`echo $dir | cut -d/ -f 6-`
		echo $server/$base
	fi

done

echo '`;'
