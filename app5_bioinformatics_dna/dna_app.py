#DNA -> Deoxyribonucleic acid
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image
import requests

url_icon="https://github.com/dhiraj1008/Streamlit_apps-data_science-/blob/main/app5_bioinformatics_dna/vector-cartoon-dna-icon.jpg"
response = requests.get(url_icon)
image = Image.open(response.content)
newimage=image.resize((500,400))
st.image(newimage,use_column_width=True)

#page title

st.write("""
# DNA  Nucleotide Count Web App

This app counts the nucleotide composition of query DNA !

***
""")
#*** is similar to hr tag in html


#input text box
st.header("Enter DNA Sequence")

sequence_input = "DNA Query\ngaacgcgaatgcctctctctctttcgatgggtatgccaattgtccacattcactcgtgttgcctcctctttgccaacacgcaagacaccag\naaacgcgtcaaccaaagagaaaaagacgccgacaacgggcagcactcgcgagagacaaaggttatcgcgttgtgttattatacattcgcatcc\ngggtcaactttagtccgttgaacatgcttcttgaaaacctagttctcttaaaataacgttttagaagttttggtcttcagATGTCTGATTCGCTAAATCATCCA\nTCGAGTTCTACGGTGCATGCAGATGATGGATTCGAGCCACCAACATCTCCGGAAGACAACAACAAAAAACCGT\nCTTTAGAACAAATTAAACAGGAAAGAGAAGCGTTGTTTACGgttagttacctattagctgcaa\ngttttgaaaaagcggaatctgtaaaaagcggaatctgtaaaaaaaacatctaaggaataattctgaaaagaaaaagtttctaaatgt\ntaatcggaatccaatttttatgaaattatttaaaaaaaaactaaaattagtttctaaaaaatttttctaaagtaattggaccatgtgaaggtacaccc\nacttgttccaatatgccatatctaactgtaaaataatttgattctcatgagaatatttttcagGATCTATTCGCAGATCGTCGACGAAGCGCTC\nGTTCTGTGATTGAAGAAGCTTTCCAAAACGAACTCATGAGTGCTGAACCAGTCCAGCCAAACGTGCCGAATCCACATTgtgagttggaaatttttat\nttgataaccaagagaaaaaaagttctacctttttttcaaaaacctttccaaaaatgattccatctgatataggat\ntaagaaaaatattttccgaaatctctgcttttcagCGATTCCCATTCGTTTCCGTCATCAACCAGTTGCTGGACCTGCTCATGATGTTTTCGGAGACGCGGTGCATTCAATTTTTCAAA\nAAATAATGTCCAGgtatacactatttttgcatatttttcttgccaaatttggtcaaaaaccgtagtacaacccaaaaagtttc\nttcatttcagAGGAGTGAACGCGGATTATAGTCATTGGATGTCATATTGGATCGCGTTGGGAATCGACAAAAAAACACAAATGAAC\nTATCATATGAAACCGTTTTGCAAAGATACTTATGCAACTGAAGGCTCCTTAGgtaggttagtcttttctaggcacagaagagtgagaaaattctaaatttctgagca\ngtctgctttttgttttccttgagtttttacttaaagctcttaaaagaaatctaggcgtgaagttcgagccttgtaccataccacaacagcattccaaatgttacagAAGCGAAACAAACATTTACTGATAAAATCAGGTCAGCTGTTGAGGAAATTATCTGGAAGTCCGCTGAATATTGTGATATTCTTAGCGAGAAGTGGACAGGAATTCATG\nTGTCGGCCGACCAACTGAAAGGTCAAAGAAATAAGCAAGAAGATCGTTTTGTGGCTTATCCAAATGGACAATACATGAATCGTGGACAGgttagtgcgaatcggggactcaagatttactgaaatagtgaagag\naaaacaaaagaaaactatattttcaaaaaaaatgagaactctaataaacagaatgaaaaacattcaaagctacagtagtatttccagctggagtttccagagccaaaaaaatgcgagtattactgtagttttgaaattgg\ntttctcactttacgtacgattttttgatttttttttcagactcttcatatgaaaaaaaatcatgttttctcctttacaagatttttttgatctcaaaacatttccagAGTGACATTTCACTTCTTGCGGTGTTCGATGGGCATGGCGGACACGAGTGCTCTCAATA"

sequence = st.text_area("Sequence Input",sequence_input,height=310)
sequence=sequence.splitlines()
sequence=sequence[1:]#skip the first element of list
sequence="".join(sequence).upper()#concatinate the list and converting to upper case.
 

st.write("***")

#prin the input data sequence

st.header("Input(DNA Query)")
sequence

#DNA Nucleotide count

st.header("Output(DNA Nucleotide Count)")
st.subheader("1.Print dictionary")


def DNA_nucleotide_count(seq):
    dict1 = dict([
         ('A',seq.count('A')),
         ('T',seq.count('T')),
         ('G',seq.count('G')),
         ('C',seq.count('C'))
    ])
    return dict1

x=DNA_nucleotide_count(sequence)
x

## Print text
st.subheader("2.Print text")
st.write('There are '+str(x['A'])+' adenine (A)')
st.write('There are '+str(x['T'])+' thynine (T)')
st.write('There are '+str(x['G'])+' adenine (guanine)')
st.write('There are '+str(x['C'])+' thymine (cytosine)')

# Display DataFrame
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(x,orient='index')
df = df.rename({0:'count'},axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index':'nucleotide'})
st.write(df)


# Display Bar Chart using matplotlib 

st.subheader('4.Display Bar Chart')
p=plt.bar(df['nucleotide'],df['count'],label='DNA_count')
plt.legend()
plt.title("DNA Nucleotide Count")
plt.xlabel("nucleotide")
plt.ylabel('count')
st.pyplot(plt.show())
st.set_option('deprecation.showPyplotGlobalUse', False)
