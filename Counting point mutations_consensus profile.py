dict_rosalind_to_dna={}
dict_rosalind_to_dna['Rosalind_1'] ='ATCCAGCT'
dict_rosalind_to_dna['Rosalind_2'] ='GGGCAACT'
dict_rosalind_to_dna['Rosalind_3']='ATGGATCT'
dict_rosalind_to_dna['Rosalind_4']='AAGCAACC'
dict_rosalind_to_dna['Rosalind_5']='TTGGAACT'
dict_rosalind_to_dna['Rosalind_6']='ATGCCATT'
dict_rosalind_to_dna['Rosalind_7']='
#print(dict_rosalind_to_dna)
d0={}
d1={}
d2={}
d3={}
d4={}
d5={}
d6={}
d7={}
d_base_to_count={}
list_0=[]
list_1=[]
list_2=[]
list_3=[]
list_4=[]
list_5=[]
list_6=[]
list_7=[]

list_0_count_A=0
list_0_count_T=0
list_0_count_C=0
list_0_count_G=0
list_1_count_A=0
list_1_count_T=0
list_1_count_C=0
list_1_count_G=0
list_2_count_A=0
list_2_count_T=0
list_2_count_C=0
list_2_count_G=0
list_3_count_A=0
list_3_count_T=0
list_3_count_C=0
list_3_count_G=0
list_4_count_A=0
list_4_count_T=0
list_4_count_C=0
list_4_count_G=0
list_5_count_A=0
list_5_count_T=0
list_5_count_C=0
list_5_count_G=0
list_6_count_A=0
list_6_count_T=0
list_6_count_C=0
list_6_count_G=0
list_7_count_A=0
list_7_count_T=0
list_7_count_C=0
list_7_count_G=0
for key in dict_rosalind_to_dna.keys():
    list_0.append(dict_rosalind_to_dna.get(key)[0])
    if len(list_0)==7:
        #print(list_0)
        list_0_count_A=list_0.count('A')
        list_0_count_G=list_0.count('G')
        list_0_count_C=list_0.count('C') 
        list_0_count_T=list_0.count('T')
        d0['A']=list_0_count_A
        d0['C']=list_0_count_C
        d0['G']=list_0_count_G
        d0['T']=list_0_count_T
        #print(d0)
    list_1.append(dict_rosalind_to_dna.get(key)[1])
    if len(list_1)==7:
        #print(list_1)
        list_1_count_A=list_1.count('A')
        list_1_count_G=list_1.count('G')
        list_1_count_C=list_1.count('C') 
        list_1_count_T=list_1.count('T')
        d1['A']=list_1_count_A
        d1['C']=list_1_count_C
        d1['G']=list_1_count_G
        d1['T']=list_1_count_T
        #print(d1)
    list_2.append(dict_rosalind_to_dna.get(key)[2])
    if len(list_2)==7:
        #print(list_2)
        list_2_count_A=list_2.count('A')
        list_2_count_G=list_2.count('G')
        list_2_count_C=list_2.count('C') 
        list_2_count_T=list_2.count('T')
        d2['A']=list_2_count_A
        d2['C']=list_2_count_C
        d2['G']=list_2_count_G
        d2['T']=list_2_count_T
        #print(d2)
    list_3.append(dict_rosalind_to_dna.get(key)[3])
    if len(list_3)==7:
        #print(list_3)
        list_3_count_A=list_3.count('A')
        list_3_count_G=list_3.count('G')
        list_3_count_C=list_3.count('C') 
        list_3_count_T=list_3.count('T')
        d3['A']=list_3_count_A
        d3['C']=list_3_count_C
        d3['G']=list_3_count_G
        d3['T']=list_3_count_T
        #print(d3)
    list_4.append(dict_rosalind_to_dna.get(key)[4])
    if len(list_4)==7:
        #print(list_4)
        list_4_count_A=list_4.count('A')
        list_4_count_G=list_4.count('G')
        list_4_count_C=list_4.count('C') 
        list_4_count_T=list_4.count('T')
        d4['A']=list_4_count_A
        d4['C']=list_4_count_C
        d4['G']=list_4_count_G
        d4['T']=list_4_count_T
        #print(d4)
    list_5.append(dict_rosalind_to_dna.get(key)[5])
    if len(list_5)==7:
        #print(list_5)
        list_5_count_A=list_5.count('A')
        list_5_count_G=list_5.count('G')
        list_5_count_C=list_5.count('C') 
        list_5_count_T=list_5.count('T')
        d5['A']=list_5_count_A
        d5['C']=list_5_count_C
        d5['G']=list_5_count_G
        d5['T']=list_5_count_T
        #print(d5)
    list_6.append(dict_rosalind_to_dna.get(key)[6])
    if len(list_6)==7:
        #print(list_6)
        list_6_count_A=list_6.count('A')
        list_6_count_G=list_6.count('G')
        list_6_count_C=list_6.count('C') 
        list_6_count_T=list_6.count('T')
        d6['A']=list_6_count_A
        d6['C']=list_6_count_C
        d6['G']=list_6_count_G
        d6['T']=list_6_count_T
        #print(d6)
    list_7.append(dict_rosalind_to_dna.get(key)[7])
    if len(list_7)==7:
        #print(list_7)
        list_7_count_A=list_7.count('A')
        list_7_count_G=list_7.count('G')
        list_7_count_C=list_7.count('C') 
        list_7_count_T=list_7.count('T')
        d7['A']=list_7_count_A
        d7['C']=list_7_count_C
        d7['G']=list_7_count_G
        d7['T']=list_7_count_T
        #print(d7)

keys_bases = [k for k in d1.keys()]

d_base_to_count = {k: (d0[k], d1[k], d2[k], d3[k], d4[k], d5[k], d6[k], d7[k]) for k in keys_bases}

#print(d_base_to_count)
#for key, value in d_base_to_count.items():

    #print(f"{key}: {value}")
import pandas as pd
import numpy as np
df = pd.DataFrame.from_dict(d_base_to_count, orient='index')
df
print(df.to_string(index=True, header=False))
#print(df.max())
maxValueIndex = df.idxmax()
concensus_base=maxValueIndex.to_numpy()
concensus_base=concensus_base.reshape(1,8)
#print(concensus_base)
concensus_base=pd.DataFrame(concensus_base)
print('consensus base:', concensus_base.to_string(index=False, header=False))
