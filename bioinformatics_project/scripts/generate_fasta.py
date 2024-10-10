import argparse

parser = argparse.ArgumentParser(description = 'Generate a random sequence of nucleotides of length 1,000,000 and output to a specified file.')
parser.add_argument('-l','--length', help = "length of sequence")
parser.add_argument('-o', '--output', help = 'output file')
args = parser.parse_args()

import random

def randfasta(seqlen):
    # generate sequence of nucleotides up to specified length
    sequence = []
    nuc = ['A','T','G','C']
    while len(sequence)<seqlen:
        sequence.append(random.choice(nuc))
    # break sequence into chunks of 80 characters
    temp = []
    for i in range((len(sequence)//80)+1):
        temp.insert(i-1,''.join(sequence[80*(i-1):80*i]))
    temp.insert((len(sequence)//80),''.join(sequence[80*(len(sequence)//80):len(sequence)]))
    temp.remove('')
    # combine chunks into one string separated by line break
    output = '\n'.join(temp)
    return output

if __name__ == "__main__":
    with open(args.output,'wt') as fout:
        print(randfasta(1000000), file = fout)