from pprint import pprint
import nltk
import streamlit as st
import sys
nltk.download('stopwords')
sys.path.append('../text_gen/')
from main import QGen
qg = QGen()
payload = {"input_text":'''Law of Segregation
This law is based on the fact that the alleles do not show any blending
and that both the characters are recovered as such in the F2
 generation
though one of these is not seen at the F1
 stage. Though the parents contain
two alleles during gamete formation, the factors or alleles of a pair segregate
from each other such that a gamete receives only one of the two factors.
Of course, a homozygous parent produces all gametes that are similar
while a heterozygous one produces two kinds of gametes each having
one allele with equal proportion.'''}
output = qg.predict_mcq(payload)
pprint (output)
st.write(output)