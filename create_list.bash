#!/bin/bash


#------------------------------------------------------------------
server='https://vesg.ipsl.upmc.fr/thredds/catalog/work_thredds'

# DRS with 4 levels after login
for dir in `ls -d1 /ccc/work/cont003/thredds/*/*/*/*/*/MONITORING`; do
	if [ -d $dir/files ] ; then
		nb=`ls $dir/files/*.nc 2>/dev/null | wc -l`
		if [[ $nb -ne 0 ]] ; then
			base=`echo $dir | cut -d/ -f 6- | sed -e 's%/MONITORING%%'`
			echo $server/$base
		fi
	fi
done

#------------------------------------------------------------------
server='https://vesg.ipsl.upmc.fr/thredds/catalog/work'

# DRS with 3 levels after login
for dir in `ls -d1 /ccc/work/cont003/dods/public/*/*/*/*/MONITORING`; do
	if [ -d $dir/files ] ; then
		nb=`ls $dir/files/*.nc 2>/dev/null | wc -l`
		if [[ $nb -ne 0 ]] ; then
			base=`echo $dir | cut -d/ -f 6- | sed -e 's%/MONITORING%%'`
			echo $server/$base
		fi
	fi
done

# DRS with 4 levels after login
for dir in `ls -d1 /ccc/work/cont003/dods/public/*/*/*/*/*/MONITORING`; do
	if [ -d $dir/files ] ; then
		nb=`ls $dir/files/*.nc 2>/dev/null | wc -l`
		if [[ $nb -ne 0 ]] ; then
			base=`echo $dir | cut -d/ -f 7- | sed -e 's%/MONITORING%%'`
			echo $server/$base
		fi
	fi
done

#------------------------------------------------------------------
