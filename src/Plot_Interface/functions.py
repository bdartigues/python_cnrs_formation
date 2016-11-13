# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from matplotlib import pylab
from Bio import SeqIO
__author__ = "benjamindartigues"
__date__ = "$11 nov. 2016 11:42:16$"

def histogram(fasta_file):
    sizes = [len(rec) for rec in SeqIO.parse(fasta_file, "fasta")]
    
    pylab.hist(sizes, bins=20)
    pylab.title("%i orchid sequences\nLengths %i to %i" \
    % (len(sizes),min(sizes),max(sizes)))
    pylab.xlabel("Sequence length (bp)")
    pylab.ylabel("Count")
    pylab.show()

def plot_gc_values(gc_values):
    pylab.plot(gc_values)
    pylab.title("%i orchid sequences\nGC%% %0.1f to %0.1f" \
    % (len(gc_values),min(gc_values),max(gc_values)))
    pylab.xlabel("Genes")
    pylab.ylabel("GC%")
    pylab.show()
