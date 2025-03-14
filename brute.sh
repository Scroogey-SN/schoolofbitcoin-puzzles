#!/bin/sh

if [ ! -f whatisthepassphrase.kdbx ]; then
	echo "whatisthepassphrase.kdbx not found"
	exit 1
fi

if ! keepassxc-cli >/dev/null; then
	echo "keepassxc-cli not found"
	exit 1
fi

touch tested.txt
while read w; do
	if grep -qxF "$w" tested.txt; then
		echo "$w skipped"
		continue
	fi
	echo "$w"
	if echo "$w" | keepassxc-cli db-info whatisthepassphrase.kdbx 2>/dev/null; then
		echo found password "$w"
		echo found password "$w" >>found.txt
		exit 0
	fi
	echo "$w" >>tested.txt
done
