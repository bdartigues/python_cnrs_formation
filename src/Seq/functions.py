# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
from Bio.SeqUtils import GC

__author__ = "benjamindartigues"
__date__ = "$7 nov. 2016 19:26:33$"


def create_sequence(seq_string):
    seq = Seq(seq_string, IUPAC.unambiguous_dna)
    return seq

def get_sequence_lenght(seq):
    return len(seq)

def count_letter_in_sequence(seq,letter):
    return seq.count(letter)

def get_gc_content(seq):
    return GC(seq)

def slice_sequence(seq,start,end):
    #return a seq object
    return seq[start:end]

def get_reverse(seq):
    #return a seq object
    return seq[::-1]

def get_string_sequence():
    return str(my_seq)