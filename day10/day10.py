import glob


def transcript(dna):
    rna = {'A':'U', 'C':'G', 'T':'A', 'G':'C'}
    mrna = ''
    for i in dna:
        mrna += rna[i]
    return mrna

def translate(dna):
    mrna = transcript(dna)
    num = 0
    start = 0
    stop = 0
    for i in mrna:
        if i == 'A':
            if mrna[num:num+3] == 'AUG':
                start = num
        if i == 'U':
            if mrna[num:num+3] == 'UAA' or mrna[num:num+3] == 'UGA' or mrna[num:num+3] == 'UAG':
                stop = num
        num += 1
    if start == 0:
        return ""
    else:
        sum = (stop-start)/3
        amino = ""
        for i in range(sum):
            amino += codon[mrna[start-1:start+2]]
        return amino

file_name = "codon.txt"
codon = {}
with open(file_name,'r')as file:
    for line in file:
        if len(line) != 11:
            codon[str(line.split(' ')[1])] = str(line.split(' ')[2])
protein_dict = {}
x = glob.glob('seq.fa')
num=0
for i in x:
    if len(i) == 5:
        protein_dict[i[0:]] = translate(x[num+1])
    num += 1