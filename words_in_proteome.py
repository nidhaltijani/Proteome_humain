import gzip 
import re
import tkinter as tk
from tkinter import messagebox
import tkinter.scrolledtext as st
def read_words(file):
    L=[]
    with open(file, 'rt') as f:
        content=f.readlines()
        for line in content :
            line=line.strip()
            if len(line)>=3:
                L.append(line.upper())
    return L

#f=gzip.open('UP000005640_9606.fasta.gz','rb')
#file_content=f.readlines()
f='UP000005640_9606.fasta.gz'
mots="english-common-words.txt"

def read_sequences(f):
    my_file=gzip.open(f,'rt',encoding='utf8')
    file_content=my_file.readlines()
    
    res={}
    temp=[]
    for line in file_content:
        temp.append(line)
        #print(temp)
    ln="".join(map(str,temp))
    temp2=ln.split(">sp|")
    
    del temp2[0]
    #print(temp2[:10])
    for seq in temp2:
        ls=seq.split("|")
        ls2=re.split("SV=.*\n",ls[1],1)
        #print(ls2[1].replace("\n", ""))
        res[ls[0]]=ls2[1].replace("\n", "")
        
        
    #print(temp2[:10])
    
    return res

def search_words_in_proteome(words,dict):
    res={}
    for word in words:
        count=0
        occ=0
        for val in dict.values():
            if word in val :
                count+=1
                occ+=val.count(word)
        res[word]=count,occ
    for key,val in res.items():
        print(f'{key} found in {val[0]} sequences')
    return res



"""for key,val in res.items():
    print(key)
    print(val)"""


#tout est en marche jusqu'à ici


def find_most_frequent_word(dict):
    max=0
    occ=0
    somme=0
    for key,val in dict.items():
        somme+=val[0]
        if val[0] > max :
            max=val[0]
            most_frequent=key
            occ=val[1]
    print(f'{most_frequent} found in {max} sequences and was found {occ} times')
    print(f'the percentage of the sequences containing this word compared to the total number of sequences containing english words is {(max/somme)*100}%')
    occ1=0
    max1=0
    for key,val in dict.items():
        if val[1] > occ1 :
            occ1=val[1]
            most_frequent1=key
            max1=val[0]
    print(f'{most_frequent1} was found {occ1} times and was found in {max1} sequences')
    #test
    return most_frequent,occ,max,most_frequent1,occ1,max1
    
    


result=read_sequences(f)
l=read_words(mots)
res=search_words_in_proteome(l,result)
m_f,occ,ma,mf1,occ1,ma1=find_most_frequent_word(res)


#GUI part
def show_most_freq():
    messagebox.showinfo("Most frequent words",f'{m_f} found in {occ} sequences and was found {ma} times \n \
                        {mf1} was found in {occ1} sequences and was found {ma1} times')

window = tk.Tk()
#title = tk.Label(text="Mini projet LPE-BI réalisé par Imen Ameur")
#title.pack()
window.title("Mini projet LPE-BI réalisé par Imen Ameur")
#test=tk.Label(text=f'{m_f} was found {occ} times and was found in {ma} sequences')
#test.pack()

btn_words=tk.Button(text="most frequent word",command=show_most_freq)
btn_words.pack()
#test  
text_area = st.ScrolledText(window,
                            width = 30, 
                            height = 8, 
                            font = ("Times New Roman",
                                    15))

#text_area.grid(column = 0, pady = 10, padx = 10)

# Inserting Text which is read only
for key,val in res.items() :
    text_area.insert(tk.INSERT,f'{key} found in {val[0]} sequences \n')

# Making the text read only
text_area.configure(state ='disabled') 
text_area.pack()
#end test
#RUN the gui 
window.mainloop()

"""result=read_sequences(f)
i=0
for key,val in result.items():
    print(key)
    print(val)
    i+=1
    if i ==5 :
        break"""
"""l=read_words(mots)
print(l)"""