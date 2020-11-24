#!/bin/bash
echo "scan the protein sequences of interest with motifs from the PROSITE database"
echo "This is the simple motif information of each proteins, if you want to check the detailed motif information, please check the motiffile/proteinname.motif" > motifsummary.txt
echo "This is also simple motif information include all the motifs in the protein dataset" > allmotifs.txt
mkdir motiffile
while read onesequence
	do 
	echo $onesequence > onesequence.txt
	/localdisk/data/BPSM/Assignment2/pullseq -i protset_1p.fa -n onesequence.txt > motiffile/$onesequence.fa
	patmatmotifs -sequence motiffile/$onesequence.fa -outfile motiffile/$onesequence.motif

	#extract motif names from the .motif and make every rows we extract into one row connected with ",".
	x=$(awk '/Motif/ {print$NF};' motiffile/$onesequence.motif | sed ':a ; N;s/\n/,/ ; t a ; ')

	#check whether what we extract motif names exist or not, and collect the information into the motifsummary.txt
	if [ ! $x ]; then
		echo $onesequence 'have none motif' >> motifsummary.txt
	else
		echo $onesequence 'have' $x 'motif' >> motifsummary.txt
		echo $onesequence 'have' $x 'motif' >> allmotifs.txt
	fi
	done < favor_protset.text
cat allmotifs.txt
