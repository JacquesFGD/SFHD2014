f = open('A2014100493NVOHBNO4.fasta', 'r')
all = f.read()
all_s = all.split('>')
g = open('formatted.txt', 'w')

#Getting a dictionnary of all sequences, indexed by accession number in uniprot
seq_dict = dict()
for item in all_s:
    temp = item.split('\n')
    seq_dict[temp[0]] = ''.join(temp[1:])
    g.write(temp[0]+'\t'+seq_dict[temp[0]]+'\n')

f.close()
g.close()

#Dictionnary of amino-acid values (taken from last column of the csv)
h = open('Aminoacids.csv', 'r')
reference = dict()
for line in h:
    temp = line.split(',')
    reference[temp[2]] = int(temp[-1].strip())
h.close()

#Turning a sequence in a list of numbers
def Idtonumlist(identifier):
    seq = seq_dict[identifier]
    out = list()
    for letter in seq:
        out.append(reference[letter])
    return out

#print Idtonumlist('P42345')

