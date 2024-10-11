# Usage: running script will generate a random 1,000,000 unit long sequence of nucleotides in the bioinformatics_project/data/random_sequence.fasta file

import random
import os

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
    # adding final chunk if length of sequeence is not divisible by 80
    temp.insert((len(sequence)//80),''.join(sequence[80*(len(sequence)//80):len(sequence)]))
    temp.remove('')
    # combine chunks into one string separated by line breaks
    output = '\n'.join(temp)
    return output

if __name__ == "__main__":
    path = os.path.join(os.pardir, 'data/random_sequence.fasta')
    with open(path,'wt') as fout:
        print(randfasta(1000000), file = fout)