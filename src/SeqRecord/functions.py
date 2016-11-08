# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

__author__ = "benjamindartigues"
__date__ = "$7 nov. 2016 11:40:41$"


from Bio import SeqIO


def read_fasta_file_with_one_sequence(fasta_file):
    record = SeqIO.read(fasta_file, "fasta")
    return record

def read_fasta_file_with_multiple_sequence(fasta_file):
    seq_record = SeqIO.parse(fasta_file, "fasta")
    return seq_record



