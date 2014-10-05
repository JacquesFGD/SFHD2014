import Image
f = open('MAFT_mTOR_PTEN_PDK1_AMPK.txt', 'r')
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
h = open('AminoacidsColors.csv', 'r')
reference = dict()
for line in h:
    temp = line.split(',')
    reference[temp[2]] = int(temp[-3]), int(temp[-2]), int(temp[-1].strip())
h.close()

#Turning a sequence in a list of numbers
def Idtonumlist(identifier):
    seq = seq_dict[identifier]
    out = list()
    for letter in seq:
        out.append(reference[letter])
    return out

l = seq_dict.keys()
size = len(seq_dict[l[1]])

for num in range(1000):
    im = Image.new('RGB', (2,2))
    im.putpixel((0,0), reference[seq_dict[l[1]][num]])
    im.putpixel((0,1), reference[seq_dict[l[2]][num]])
    im.putpixel((1,0), reference[seq_dict[l[1]][num]])
    im.putpixel((1,1), reference[seq_dict[l[1]][num]])
    im.resize((100,100))
    im.save('PNG/'+str(num)+'.bmp')


        



