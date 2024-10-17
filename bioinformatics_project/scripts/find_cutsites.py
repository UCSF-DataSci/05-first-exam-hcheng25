import argparse
parser = argparse.ArgumentParser(description = 'Locate inputted cutsites within an inputted sequence, and find pairs that are 80-120 kbp apart.')
parser.add_argument('-s','--sequence', help = "The DNA sequence to be operated on")
parser.add_argument('-c','--cutsite', help = "Cutsite of interest, ex: 'G|GATCC'")
args = parser.parse_args()

import os

def cutcount(sequence, cutsite):
    cutsite = cutsite.replace('|', '')
    count = sequence.count(cutsite)
    return count

def cutloc(sequence, cutsite): # make a list of locations of cuts in sequence
    cutbase = cutsite.replace('|', '') # cutbase is the cutsite sequence without pipe indicating cut
    loclist = []
    # find cut relative to cutsite
    for i in range(len(cutsite)):
        if cutsite[i] == '|': cutloc = i
    # make list of locations
    for i in range(len(sequence)):
        if sequence[i:i+len(cutsite)-1] == cutbase:
            loclist.append(i+cutloc)
    return loclist

def cutpairs(locations, mindist, maxdist): # count pairs that are between mindist and maxdist apart
    paircount = 0
    for i in range(len(locations)):
        for j in range(i, len(locations)):
            if locations[j]-locations[i]>mindist and locations[j]-locations[i]<maxdist:
                paircount += 1
    return paircount

def firstfive(locations, mindist, maxdist): # list first five pairs that are between mindist and maxdist apart
    firstfive = []
    for i in range(len(locations)):
        for j in range(i, len(locations)):
            if locations[j]-locations[i]>mindist and locations[j]-locations[i]<maxdist:
                if len(firstfive)<5: firstfive.append(f'{locations[i]} - {locations[j]}')
                else: break
    return firstfive

if __name__ == "__main__":
    with open(args.sequence, 'rt') as fout: # import sequence as fasta and convert to uppercase
        fasta = fout.read()
        fasta = fasta.strip()
        fasta = fasta.upper()
    cutsite = args.cutsite.upper() # convert cutsite to uppercase
    resultpath = 'bioinformatics_project/results/cutsite_summary.txt'
    locs = cutloc(fasta, cutsite)
    thefive = firstfive(locs, 80000, 120000)
    with open(resultpath,'wt') as fout:
        print('Analyzing cut site: ', cutsite, '\n', file=fout)
        print('Total cut sites found: ', cutcount(fasta, cutsite), '\n', file=fout)
        print('Cut site pairs 80-120 kbp apart: ', cutpairs(locs, 80000, 120000), '\n', file=fout)
        print('First five pairs:\n1. ', thefive[0], '\n2. ', thefive[1], '\n3. ', thefive[2], '\n4. ', thefive[3], '\n5. ', thefive[4], file=fout)