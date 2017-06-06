#!/bin/bash

#------------------------------------------------------------------
echo 'var input = `'

#------------------------------------------------------------------
server='https://vesg.ipsl.upmc.fr/thredds/catalog/work_thredds'
for dir in `ls -d1 /ccc/work/cont003/thredds/*/*/*/*/*/MONITORING`; do
	if [ -d $dir/files ] ; then
		nb=`ls $dir/files/*.nc | wc -l`
		if [[ $nb -ne 0 ]] ; then
			base=`echo $dir | cut -d/ -f 6- | sed -e 's%/MONITORING%%'`
			echo $server/$base
		fi
	fi
done

#------------------------------------------------------------------
server='https://vesg.ipsl.upmc.fr/thredds/catalog/work'
for dir in `ls -d1 /ccc/work/cont003/dods/public/*/*/*/*/MONITORING`; do
	if [ -d $dir/files ] ; then
		nb=`ls $dir/files/*.nc | wc -l`
		if [[ $nb -ne 0 ]] ; then
			base=`echo $dir | cut -d/ -f 7- | sed -e 's%/MONITORING%%'`
			echo $server/$base
		fi
	fi
done

#------------------------------------------------------------------
echo '`;'

