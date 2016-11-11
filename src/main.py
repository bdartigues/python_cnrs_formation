#!/usr/bin/python
#here call all the module created
#import functions
from Seq.functions import *
from SeqRecord.functions import *
from NCBI.functions import *
from Blast.functions import *
from Plot_Interface.functions import *

import os

def get_or_create_dir(dirname):
    if not os.path.isdir(dirname):
        os.makedirs(dirname)
    return dirname
root_dir = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
data_dir = get_or_create_dir(os.path.join(root_dir,'data/'))

if __name__ == "__main__":


#####SEQ PART 
    fasta_file="ls_orchid.fasta"
    sequence=create_sequence('GATCGATGGGCCTATATAGGATCGAAAATCGC')
    #print get_sequence_lenght(sequence)
    #print count_letter_in_sequence(sequence,"G")
    #print get_gc_content(sequence)
    #print slice_sequence(sequence,3,8)
    #print get_reverse(sequence)
    
#####SEQ RECORD PART
    
    #seq_record=read_fasta_file_with_multiple_sequence(data_dir+fasta_file)
    #for record in seq_record:
    #    print(record.id)
    #    print(repr(record.seq))
    #    print(len(record))
 
    #xml_result=get_available_databases()
    #dict_record=get_available_databases_as_dict()
    
    
#####NCBI PART 
    #record=get_field_for_pubmed_search()
    #record=search_for_paper("biopython")
    #search_for_author_publication()
    #gi="186972394"
    #get_gb_file(gi)
    #get_fasta_file_by_gi(gi)
    #gb_record=get_gb_file_record(gi)
    #print gb_record
    #filename = data_dir+"gi_"+gi+".gbk"
    #download_gb_file_record(filename)
    
    ###EGQUERY PART
    
    #global_search("potyvirus")
    
    #get_all_genes()
    #BLAST PART

    
    
    #handle=run_qblast("blastn", "nt", "8332116")
    #save_file = open(data_dir+"my_blast.xml", "w")
    #save_file.write(handle.read())
    #save_file.close()
    #handle.close()
    #result_handle = open(data_dir+"my_blast.xml")
    #parse_blast_result(result_handle)
    #blast_record=read_blast_result(result_handle)
    #E_VALUE_THRESH = 0.04
    #get_summary(blast_record,E_VALUE_THRESH)
    
    
    
    #fasta_string = open(data_dir+fasta_file).read()
    #run_qblast_from_fasta(fasta_string,"blastn", "nt")
    #record = SeqIO.read(data_dir+fasta_file, format="fasta")
    #run_qblast_from_seq_record(record,"blastn", "nt")
    
    
    
    #PLOT INTERFACE
    
    histogram(data_dir+fasta_file)
    
    plot_gc_values(get_gc_values(read_fasta_file_with_multiple_sequence(data_dir+fasta_file)))
    # here get some files using the NCBI biopython access.
    # Searching, downloading, and parsing GenBank records
    # Searching, downloading, and parsing Entrez Nucleotide records
    
    # Using Seq and Seq record, SeqIO pour parser et stocker les sequences.
    # essayer avec fichiers simples ou des fichiers contenant des alignement multiples.
    # utiliser CLustal
    # Parsing Swiss-Prot records
    # Retrieving a Swiss-Prot record
    # essayer de lancer un blast et de recuperer ses resultats.
    
    
