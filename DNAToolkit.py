# DNA Toolkit file

import collections
from structures import *

#Checks sequence to make sure it is a DNA string

def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq

#counts nucleotides
def countNucFrequency(seq):
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0 }
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict

def transcription(seq):
    # DNA -> RNA Transcription
    return seq.replace("T", "U")

def reverse_complement(seq):
    return ''.join([dna_reverse_complement[nuc] for nuc in seq])[::-1]




# def countNucFrequency(seq):
# return dict(collections.Counter(seq))