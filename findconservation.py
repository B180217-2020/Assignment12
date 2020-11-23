#!/usr/bin/python3
import subprocess
import os
import pandas as pd

prot_number = os.popen('grep -c ">" protset_1p.fa').readlines()
number_p = prot_number[0].replace('\n','')
if int(number_p) >= 250:
	print("The number of sequence is over or equal 250, you need to select one protein, and we will find the 250 sequences which are most similar with your input")
	
	os.system('clustalo -i protset_1p.fa -t Protein --distmat-out=protmatrix.txt --full')

	#We need to modify the Pairwise distance matrix to a proper format for choosing the most similar sequences.
	os.system('sed -i "1d" protmatrix.txt')
	protmatrix = open('protmatrix.txt')
	for line in protmatrix.readlines():
		with open('protmatrix_modify.txt','a') as m:
			m.write(' '.join(line.split()).join('\r\n'))
	protmatrix.close()
	protmatrix_modify = pd.read_csv('protmatrix_modify.txt',sep=' ',  header=None)
	header = protmatrix_modify.iloc[:,0].values.tolist()
	protmatrix_modify.index= header 
	protmatrix_modify.drop(columns=0,inplace=True)
	protmatrix_modify.columns= header 
	print("After modifying, this is Pairwise distance matrix!\n",protmatrix_modify)
	print("This is the list of proteins we found\n",header)
	favor_prot=input("which protein you get interested with,we'll find the 250 sequences which are most similar with your input")
	protmatrix_modify.sort_values([favor_prot.upper()],ascending=True,inplace=True)
	favor_prot250 = list(table.index)[:250]
	favor_prot250 = '\n'.join(favor_prot250)
	favor_prot250_w = open("favor_prot250.text","w")
	favor_prot250_w.write(f"{favor_prot250}")
	favor_prot250_w.close()
	subprocess.call("/localdisk/data/BPSM/Assignment2/pullseq -i protset_1p.fa -n favor_prot250.text > protset_2p.fa",shell=True)
	os.system('clustalo -i protset_2p.fa -t Protein -o protset_toplotcon.fa')
	os.system('plotcon -sequences protset_toplotcon.fa -winsize 4 -graph')
else:
	os.system('clustalo -i protset_1p.fa -t Protein --distmat-out=protmatrix.txt --full -o protset_toplotcon.fa')
	os.system('sed -i "1d" protmatrix.txt')
	protmatrix = open('protmatrix.txt')
	for line in protmatrix.readlines():
		with open('protmatrix_modify.txt','a') as m:
			m.write(' '.join(line.split()).join('\r\n'))
	protmatrix.close()
	protmatrix_modify = pd.read_csv('protmatrix_modify.txt',sep=' ',  header=None)
	header = protmatrix_modify.iloc[:,0].values.tolist()
	protmatrix_modify.index= header 
	protmatrix_modify.drop(columns=0,inplace=True)
	protmatrix_modify.columns= header 
	print("After modifying, this is Pairwise distance matrix!\n",protmatrix_modify)
	print("This is the list of proteins we found\n",header)
	os.system('plotcon -sequences protset_toplotcon.fa -winsize 4 -graph x11')
	
