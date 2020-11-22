#!/usr/bin/python3
import subprocess
import os

organism_input = input("which species you want to search: ")
protein_input = input("which protein you want to search: ")
try:
	os.system(f'esearch -db protein -query "{organism_input}[organism] AND {protein_input}[PROT] NOT Partial" | efetch -db protein -format fasta > rawprotset.fq')
	print("try to looking for the ",protein_input," of ",organism_input)
except:
	print("There is something wrong, maybe you should review what you type")
if os.path.exists("/localdisk/home/s2127878/Assignment2/rawprotset.fq"):
	prot_number = os.popen('grep -c ">" rawprotset.fq').readlines()
	number_p = prot_number[0].replace('\n','')
	print("We find it and there are ",number_p," sequences.")
if int(number_p) > 1000:
	print("There are more than 1000 sequences, we need to decrease the number")
	os.system('seqkit sample -n 1000 rawprotset.fq -o protset_1p.fq')
else:
	os.rename("rawprotset.fq","protest_1p.fq")

