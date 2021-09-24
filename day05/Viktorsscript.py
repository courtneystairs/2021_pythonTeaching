#!/path/to/python

"""
Description:
    Takes a list of accession numbers and retrieves the protein sequences from NCBI
    then outputs a table summarizing the length and taxonomy of each sequence

Dependencies:
  Biopython
  pandas (v=??)


Examples:
 (1) python Viktorsscript.py -i list_of_accessions -o table_output
 
Author:
 US

"""
#################### IMPORTS ################################

import argparse
from Bio import SeqIO
from Bio import Entrez
import pandas as pd
import time 

################ DEFINITIONS ################################

################ ARGUMENTS ##################################

parser = argparse.ArgumentParser(description='Takes a list of accession numbers and retrieves the protein sequences from NCBI then outputs a table summarizing the length and taxonomy of each sequence')
parser.add_argument("-a", "--accession", required=True, help="This is a list of accesion number to retrieve, one entry per line")
parser.add_argument("-o", "--outprefix",  required=False, help="output", default="default_output")
parser.add_argument("-t", "--tax_level",  required=False, help="The number of taxonomic levels, you want back", default="5")
args = parser.parse_args()


# Argument variables
accession_arg = args.accession
outprefix_arg = args.outprefix
tax_level_arg = int(args.tax_level)



file_as_list = open(accession_arg).readlines()
for i in range(0, len(file_as_list)):
    file_as_list[i] = file_as_list[i].strip() #Remove newline characters

#Get the data from the database.
Entrez.email = "viktor.persson@tmb.lth.se"
handle = Entrez.efetch(db="protein", id=file_as_list, rettype="gb", retmode="text")
records = list(SeqIO.parse(handle, "genbank"))
handle.close()

#Make a list containing dictionaries
listOfDicts = []
for oneRecord in records: #Make dictionaries from the genbank records
  listOfDicts.append({'Accession':oneRecord.id, 
                      'length':len(oneRecord.seq), 
                      'domain':oneRecord.annotations["taxonomy"][0], 
                      'user_defined_taxonomy_levels':'_'.join(oneRecord.annotations["taxonomy"][0:tax_level_arg])})

#Convert to a DataFrame.
df = pd.DataFrame(listOfDicts)

df.to_csv(outprefix_arg)
