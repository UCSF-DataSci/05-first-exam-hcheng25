mkdir -p bioinformatics_project/data
mkdir -p bioinformatics_project/scripts
mkdir -p bioinformatics_project/results

touch bioinformatics_project/scripts/generate_fasta.py
touch bioinformatics_project/scripts/dna_operations.py
touch bioinformatics_project/scripts/find_cutsites.py

touch bioinformatics_project/results/cutsite_summary.txt

touch bioinformatics_project/data/random_sequence.fasta

touch bioinformatics_project/README.md
echo "# Data
Contains generated random sequence
# Results
Contains results for cutsite script
# Scripts
Contains fasta generation, cutsite locator, and dna operation scripts" > bioinformatics_project/README.md