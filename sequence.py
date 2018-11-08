#!/usr/bin/env python

import Bio
from Bio.Seq import Seq


###get some help
print(help(Seq))



my_seq = Seq("AGTACACTGGT")
print(my_seq)


from Bio.Alphabet import IUPAC
my_seq = Seq('GATCGATGGGCCTATATAGGATCGAAAATCGC', IUPAC.unambiguous_dna)
print(len(my_seq))
print(my_seq.count("G"))
print(100 * float(my_seq.count('G') + my_seq.count('C')) / len(my_seq))



from Bio.SeqUtils import GC

print(GC(my_seq))


####SLicing a sequence

print(my_seq[:5])

###get reverse complement
print(my_seq)
print(my_seq[::-1])


#####write fasta files

fasta_format_string = ">Name\n%s\n" % my_seq
print(fasta_format_string)


####concatenate sequences

protein_seq = Seq("EVRNAK", IUPAC.protein)
dna_seq = Seq("ACGT", IUPAC.unambiguous_dna)
#print(protein_seq# + dna_seq)


####get complement sequence and reverse complement

print("sequence {s}".format(s=my_seq))
print("sequence complement {s}".format(s=my_seq.complement()))
print("sequence reverse_complement {s}".format(s=my_seq.reverse_complement()))


####transcribe sequence

coding_dna = Seq("ATGGCCATTGTAATGGGCCGCTGAAAGGGTGCCCGATAG", IUPAC.unambiguous_dna)
template_dna = coding_dna.reverse_complement()
messenger_rna = coding_dna.transcribe()
print("messenger rna {m}".format(m=messenger_rna))  

##another way to do it

messenger_rna=template_dna.reverse_complement().transcribe()
print("messenger rna {m}".format(m=messenger_rna))  


protein_aa=messenger_rna.translate()
print("protein aa {p}".format(p=protein_aa))



######
from Bio.Data import CodonTable

standard_table = CodonTable.unambiguous_dna_by_name["Standard"]
print(standard_table)


  











