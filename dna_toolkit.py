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
    #return ''.join([dna_reverse_complement[nuc] for nuc in seq])[::-1]

    #Pythonic approach, faster solution
    #not using a dictionary approach(not brute force)
    mapping = str.maketrans('ATCG', "TAGC")
    return seq.translate(mapping)[::1]

def gc_content(seq):
    ##GC Content in a DNA/RNA sequence
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100)


def gc_content_subsec(seq, k=20):
    #GC Content in a DNA/RNA sub-seqeunce length k, k=20  by default
    res = []
    for i in range(0, len(seq) - k + 1, k):
        subseq = seq[i:i + k]
        res.append(gc_content(subseq))
    return res

# def countNucFrequency(seq):
# return dict(collections.Counter(seq))