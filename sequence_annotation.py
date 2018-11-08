#!/usr/bin/env python

import Bio
import sys
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord

if len(sys.argv)==2 and sys.argv[1]=="-h":

	print(help(SeqRecord))
	exit(-1)

simple_seq = Seq("GATC")




simple_seq_r = SeqRecord(simple_seq)
print(simple_seq_r)



####seq_record from fasta

###https://github.com/biopython/biopython/blob/master/Tests/GenBank/NC_005816.fna


from Bio import SeqIO
record = SeqIO.read("seq.fasta", "fasta")
print(record)



record = SeqIO.read("NC005816.gb", "genbank")
print(record)
