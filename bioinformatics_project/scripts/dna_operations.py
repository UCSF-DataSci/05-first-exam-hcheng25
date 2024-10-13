import argparse
parser = argparse.ArgumentParser(description = 'Return complement, reverse, and reverse complement of a given DNA sequence.')
parser.add_argument('-s','--sequence', help = "The DNA sequence to be operated on")
args = parser.parse_args()

def complement(sequence):
    nuc_comp = str.maketrans({'A':'T','T':'A','C':'G','G':'C'})
    complement = sequence.translate(nuc_comp)
    return complement

def reverse(sequence):
    reverse = []
    for i in range(len(sequence)):
        reverse.append(sequence[-i-1])
    reverse = ''.join(reverse)
    return reverse

def reverse_complement(sequence):
    # Use other two functions to first reverse, then make complement
    revcomp = complement(reverse(sequence))
    return revcomp

if __name__ == "__main__":
    sequence = args.sequence
    comp = complement(sequence)
    rev = reverse(sequence)
    revcomp = reverse_complement(sequence)
    print(f"Original sequence: {sequence}\nComplement: {comp}\nReverse: {rev}\nReverse complement: {revcomp}")