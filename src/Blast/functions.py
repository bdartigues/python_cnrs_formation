# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML

__author__ = "benjamindartigues"
__date__ = "$11 nov. 2016 11:03:54$"


def run_qblast(blast_tool,db_type,id):
    result_handle = NCBIWWW.qblast(blast_tool, db_type, id)
    return result_handle

def run_qblast_from_fasta(fasta_string,blast_tool,db_type):
    result_handle = NCBIWWW.qblast(blast_tool, db_type, fasta_string)
    return result_handle

def run_qblast_from_seq_record(record,blast_tool,db_type):
    result_handle = NCBIWWW.qblast(blast_tool, db_type, record.seq)
    return result_handle

def parse_blast_result(result_handle):
    blast_records = NCBIXML.parse(result_handle)
    for blast_record in blast_records:
        print blast_record
        
def get_blast_record_list(result_handle):
    blast_records = NCBIXML.parse(result_handle)
    blast_records = list(blast_records)
    return blast_records

def read_blast_result(result_handle):
    blast_record = NCBIXML.read(result_handle)
    return blast_record

def get_summary(blast_record,e_value_thresh):
   
    for alignment in blast_record.alignments:
        for hsp in alignment.hsps:  
            if hsp.expect < e_value_thresh:
                print('****Alignment****')
                print('sequence:', alignment.title)
                print('length:', alignment.length)
                print('e value:', hsp.expect)
                print(hsp.query[0:75] + '...')
                print(hsp.match[0:75] + '...')
                print(hsp.sbjct[0:75] + '...')