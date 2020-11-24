#!/usr/bin/python3
import subprocess
import os
#input what you want to search for
organism_input = input("which species you want to search: ")
protein_input = input("which protein you want to search: ")
print("try to looking for the ",protein_input," of ",organism_input)

#use edirect to search the protein database with what you input above
try:
	os.system(f'esearch -db protein -query "{organism_input} [organism] AND {protein_input}*[PROT] " | efetch -db protein -format fasta > rawprotset.fa')
except:
	print("There is something wrong, maybe you should review what you type")

#check the searching protein exists or not
if os.path.exists("/localdisk/home/s2127878/Assignment2/rawprotset.fa"):
	#get the number of proteins and make this number clear
	prot_number = os.popen('grep -c ">" rawprotset.fa').readlines()
	number_p = prot_number[0].replace('\n','')
	#check the number is not equal to 0
	if int(number_p) != 0:
		print("We find it and there are ",number_p," sequences.")
		#if the number is over 1000, use 'seqkit' to get 1000 sequences
		if int(number_p) > 1000:
        		print("There are more than 1000 sequences, we need to decrease the number")
        		os.system('seqkit sample -n 1000 rawprotset.fa -o protset_1p.fa')
		else:
			#this is for making filename uniform, and good for next step
        		os.rename("rawprotset.fa","protset_1p.fa")

	else: 
		print("We don't find any sequences,please type your input exactly")
		os.remove("rawprotset.fa")
