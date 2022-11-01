# DNA Toolkit file

import collections
from typing import Counter
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

def translate_seq(seq, init_pos=0):
    #translate DNA seq into aminoacid seq
    return [dna_codons[seq[pos:pos + 3]] for pos in range(init_pos, len(seq) -2, 3)]

def codon_usage(seq, aminoacid):
    #freq of each codon encoding a given aminoacid in a DNA seq
    temp_list = []
    for i in range(0, len(seq) - 2, 3):
        if dna_codons[seq[i:i +3]] == aminoacid:
            temp_list.append(seq[i:i + 3])
    
    freq_dict = dict(collections.Counter(temp_list))
    total_weight = sum(freq_dict.values())
    for seq in freq_dict:
        freq_dict[seq] = round(freq_dict[seq] / total_weight, 2)
    return freq_dict
