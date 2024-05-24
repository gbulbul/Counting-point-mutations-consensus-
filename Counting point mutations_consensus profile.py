dict_rosalind_to_dna={}
dict_rosalind_to_dna['Rosalind_1'] ='ATCCAGCT'
dict_rosalind_to_dna['Rosalind_2'] ='GGGCAACT'
dict_rosalind_to_dna['Rosalind_3']='ATGGATCT'
dict_rosalind_to_dna['Rosalind_4']='AAGCAACC'
dict_rosalind_to_dna['Rosalind_5']='TTGGAACT'
dict_rosalind_to_dna['Rosalind_6']='ATGCCATT'
dict_rosalind_to_dna['Rosalind_7']='ATGGCACT'
d0,d1,d2,d3,d4,d5,d6,d7={},{},{}, {}, {},{}, {},{}
list_0, list_1,list_2,list_3,list_4,list_5,list_6,list_7=[],[],[],[],[],[],[],[]
for key in dict_rosalind_to_dna.keys():
    list_0.append(dict_rosalind_to_dna.get(key)[0])
    list_1.append(dict_rosalind_to_dna.get(key)[1])
    list_2.append(dict_rosalind_to_dna.get(key)[2])
    list_3.append(dict_rosalind_to_dna.get(key)[3])
    list_4.append(dict_rosalind_to_dna.get(key)[4])
    list_5.append(dict_rosalind_to_dna.get(key)[5])
    list_6.append(dict_rosalind_to_dna.get(key)[6])    
    list_7.append(dict_rosalind_to_dna.get(key)[7])


class CountPerString:
      def Count_to_dict(liste):
            d={}
            d['A'] = liste.count('A')
            d['C']= liste.count('G')
            d['G'] = liste.count('C')
            d['T'] = liste.count('T')
            return d
d0 = CountPerString.Count_to_dict(list_0)
d1 = CountPerString.Count_to_dict(list_1)
d2 = CountPerString.Count_to_dict(list_2)
d3= CountPerString.Count_to_dict(list_3)
d4= CountPerString.Count_to_dict(list_4)
d5 = CountPerString.Count_to_dict(list_5)
d6= CountPerString.Count_to_dict(list_6)
d7= CountPerString.Count_to_dict(list_7)

keys_bases = [k for k in d1.keys()]

d_base_to_count = {k: (d0[k], d1[k], d2[k], d3[k], d4[k], d5[k], d6[k], d7[k]) for k in keys_bases}
import pandas as pd
import numpy as np
df = pd.DataFrame.from_dict(d_base_to_count, orient='index')
df
print(df.to_string(index=True, header=False))
#print(df.max())
maxValueIndex = df.idxmax()
consensus_base=maxValueIndex.to_numpy()
consensus_base=consensus_base.reshape(1,8)
#print(consensus_base)
consensus_base=pd.DataFrame(consensus_base)
print('consensus base:', consensus_base.to_string(index=False, header=False))
  
   
