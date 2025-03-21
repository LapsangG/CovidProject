import streamlit as st
import pickle as pk
import pandas as pd

st.title('Covid 19')
st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS3f4i8jHMxo2XI77yeT9c9CnT15AhimeusfQ&s')

with open('Covid_Classification.pickle', 'rb') as filename:
    model=pk.load(filename)

#create form
Cough_symptoms=st.radio("Enter cough symtoms: ",[True,False])
Fever=st.radio("Enter Fever symtoms: ",[True,False])
Sore_throat=st.radio("Enter sore throat symtoms: ",[True,False])
Shortness_of_breath=st.radio("Enter shortness of breath symtoms: ",[True,False])
Headache=st.radio("Enter Headache symtoms: ",[True,False])
Known_contact=st.radio("Pick the point of contact: ",["Abroad","Contact with confirmed", "Other"])

d={'Abroad': 0, 'Contact with confirmed': 1,"Other":2}
df=pd.DataFrame(
    [[Cough_symptoms, Fever, Sore_throat, Shortness_of_breath, Headache, d[Known_contact]]],
    columns=['Cough_symptoms','Fever','Sore_throat','Shortness_of_breath','Headache','Known_contact']
)
if st.button("Predict"):
    result=model.predict(df)
    if int(result[0]==1):
        st.error(f"I am sorry to say that you have Covid 19 because result= {result[0]}")
    else:
        st.success(f"You dont have covid 19 because result= {result[0]}")
