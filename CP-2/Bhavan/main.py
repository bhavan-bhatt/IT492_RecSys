import folium
import streamlit as st
import pandas as pd
from streamlit_folium import st_folium
import pandas as pd 
import numpy as np
from gensim.models import Word2Vec as w2v
import matplotlib.pyplot as plt
from numpy.linalg import norm
from numpy import dot
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from math import radians, cos, sin, asin, sqrt, atan2
import joblib

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

meta_df = pd.read_json('data/business_with_embeddings.json')
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

def convert_user_input(user_input):
    ps = PorterStemmer()
    sw = stopwords.words('english')  
    vectorizer = joblib.load('tfidf_vectorizer.pkl')
    user_tokens = word_tokenize(user_input.lower())
    user_tokens = [ps.stem(token) for token in user_tokens if token.isalnum() and token not in sw]
    user_text = ' '.join(user_tokens)
    user_vector = vectorizer.transform([user_text])
    return user_vector



def find_business(user_input):
    user_vector = convert_user_input(user_input)
    similar_business = []
    for categories in meta_df['category_embeddings']:
        cosine_similarities = cosine_similarity(user_vector, categories)
        similar_business.append(cosine_similarities.max())
    similar_business = np.where(np.array(similar_business)>=0.8)[0]
    similar_business_df = meta_df.iloc[similar_business]
    return similar_business_df

with st.sidebar:
    st.title("Google Maps")
    st.write("**CP2 for IT492 RecSys.**")
    st.write("***Submitted by***")
    st.caption("Team T7: Gnosis")
    st.caption("Bhavan Bhatt (202311021)")
    st.caption("Pratham Patel (202311022)")
    st.caption("Nishit Munjani (202311026)")
    st.caption("Viraj Prajapati (202311069)")

selected = st.text_input("Seach...")
button_clicked = st.button("OK")


if selected:
        check = find_business(selected)
        st.text(check.iloc[0]['name'])
        st.text(check.iloc[1]['name'])
        st.text(check.iloc[2]['name'])
        st.text(check.iloc[3]['name'])
        st.text(check.iloc[4]['name'])
        center = [46.5739667965278,-98.338623046875]
        zoom_start=6

        coord_1 = [check.iloc[0]['latitude'],check.iloc[0]['longitude']]
        coord_2 = [check.iloc[1]['latitude'],check.iloc[1]['longitude']]
        coord_3 = [check.iloc[2]['latitude'],check.iloc[2]['longitude']]
        coord_4 = [check.iloc[3]['latitude'],check.iloc[3]['longitude']]
        coord_5 = [check.iloc[4]['latitude'],check.iloc[4]['longitude']]
        m = folium.Map(location=center, zoom_start=zoom_start, tiles="OpenStreetMap")
        folium.Marker(
        coord_1, popup=check.iloc[0]['name'], tooltip=check.iloc[0]['name']
        ).add_to(m)
        folium.Marker(
        coord_2, popup=check.iloc[1]['name'], tooltip=check.iloc[1]['name']
        ).add_to(m)
        folium.Marker(
        coord_3, popup=check.iloc[2]['name'], tooltip=check.iloc[2]['name']
        ).add_to(m)
        folium.Marker(
        coord_4, popup=check.iloc[3]['name'], tooltip=check.iloc[3]['name']
        ).add_to(m)
        folium.Marker(
        coord_5, popup=check.iloc[4]['name'], tooltip=check.iloc[4]['name']
        ).add_to(m)
        st_data = st_folium(m,width=725,height=400)

