# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from Bio import Entrez
from Bio import SeqIO
import os
import sys

__author__ = "benjamindartigues"
__date__ = "$7 nov. 2016 16:42:24$"

Entrez.email = "benjamin.dartigues@u-bordeaux.fr"

def get_available_databases():
    handle = Entrez.einfo()
    result = handle.read()
    return result

def get_available_databases_as_dict():
    handle = Entrez.einfo()
    record = Entrez.read(handle)
    return record

def get_field_for_pubmed_search():
    handle = Entrez.einfo(db="pubmed")
    record = Entrez.read(handle)
    return record["DbInfo"]["FieldList"]

def search_for_paper(word):
    handle = Entrez.esearch(db="pubmed", term=word)
    record = Entrez.read(handle)
    return record["IdList"]

def search_for_author_publication():
    handle = Entrez.esearch(db="pubmed", term="Dartigues B[Author] ")
    record = Entrez.read(handle)
    print record["IdList"]
    
def get_gb_file(gi):
    handle = Entrez.efetch(db="nucleotide", id=gi, rettype="gb", retmode="text")
    print(handle.read())
    
def get_fasta_file_by_gi(gi):
    handle = Entrez.efetch(db="nucleotide", id=gi, rettype="fasta", retmode="text")
    print(handle.read())
    
def get_gb_file_record(gi):
    handle = Entrez.efetch(db="nucleotide", id=gi, rettype="gb", retmode="text")   
    record = SeqIO.read(handle, "genbank")
    handle.close()
    return record

def download_gb_file_record(filename):

    if not os.path.isfile(filename):
        # Downloading...
        net_handle = Entrez.efetch(db="nucleotide", id="186972394", rettype="gb", retmode="text")
        out_handle = open(filename, "w")
        out_handle.write(net_handle.read())
        out_handle.close()
        net_handle.close()
        print("Saved")
    else:
        print("file already exists !!! ")
        
def global_search(term):
    handle = Entrez.egquery(term=term)
    record = Entrez.read(handle)
    for row in record["eGQueryResult"]:
        print(row["DbName"], row["Count"])
        
def get_all_genes():
    handle = open("Homo_sapiens.xml")
    records = Entrez.parse(handle)
    for record in records:
        status = record['Entrezgene_track-info']['Gene-track']['Gene-track_status']
        if status.attributes['value']=='discontinued':
            continue
        geneid = record['Entrezgene_track-info']['Gene-track']['Gene-track_geneid']
        genename = record['Entrezgene_gene']['Gene-ref']['Gene-ref_locus']
        print(geneid, genename)
        


def retrieve_annotation(id_list):

    """Annotates Entrez Gene IDs using Bio.Entrez, in particular epost (to
    submit the data to NCBI) and esummary to retrieve the information.
    Returns a list of dictionaries with the annotations."""

    request = Entrez.epost("gene",id=",".join(id_list))
    try:
        result = Entrez.read(request)
    except RuntimeError as e:
        #FIXME: How generate NAs instead of causing an error with invalid IDs?
        print "An error occurred while retrieving the annotations."
        print "The error returned was %s" % e
        sys.exit(-1)

    webEnv = result["WebEnv"]
    queryKey = result["QueryKey"]
    data = Entrez.esummary(db="gene", webenv=webEnv, query_key =
            queryKey)
    annotations = Entrez.read(data)

    print "Retrieved %d annotations for %d genes" % (len(annotations),
            len(id_list))

    return annotations


def print_data(annotation):
    for gene_data in annotation:
        gene_id = gene_data["Id"]
        gene_symbol = gene_data["NomenclatureSymbol"]
        gene_name = gene_data["Description"]
        print "ID: %s - Gene Symbol: %s - Gene Name: %s" % (gene_id, gene_symbol, gene_name)



