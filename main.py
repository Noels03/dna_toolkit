# DNA Toolset/Code testing file
from DNAToolkit import *
from utilities import colored
import random


#create random RNA sequence for testing:
rdmDNAstr = ''.join([random.choice(Nucleotides)
                        for nucl in range(50)])

DNAStr = (validateSeq(rdmDNAstr))

print(f'\nSequence: {colored(DNAStr)}\n')
print(f'[1] + Sequence Length: {len(DNAStr)}\n')
print(colored(f'[2] + Nucleotide Frequency: {countNucFrequency(DNAStr)}\n'))

print(f'[3] + DNA/RNA Transciption: {colored(transcription(DNAStr))}\n')

print(f"[4] + DNA String + Reverse Complement:\n5'  {colored(DNAStr)} 3' ")
print(f"    {''.join(['|' for c in range(len(DNAStr))])}")
print(f"3'  {colored(reverse_complement(DNAStr))} 5'\n")