import folium
import streamlit as st
import pandas as pd
from streamlit_folium import st_folium

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

# local_css("styles.css")
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

with st.sidebar:
    st.title("Google Maps")
    st.write("**CP2 for IT492 RecSys.**")
    st.write("***Submitted by***")
    # linkedin_badge: https://www.linkedin.com/pulse/how-create-linkedin-badge-your-website-amy-wallin/
    st.caption("Team T7: Gnosis")
    st.caption("Bhavan Bhatt (202311021)")
    st.caption("Bhavan Bhatt (202311021)")
    st.caption("Bhavan Bhatt (202311021)")
    st.caption("Bhavan Bhatt (202311021)")
    # st.write("**Questions and answers sourced from:**")
    # st.caption(" 82 Product Owner Interview Questions to Avoid Hiring Imposters")
    # st.caption("By Stefan Wolpers | Version 8.01 | 2022-01-17")
    # st.caption("https://berlin-product-people.com/")
    # st.caption(
    #     "Download link: https://age-of-product.com/42-scrum-product-owner-interview-questions/"
    # )
    # st.write("Copyright notice:")
    # st.caption(
    #     "No part of this publication or its text may be made publicly available or, excepting personal use, reproduced, or distributed or translated into other languages without the prior written permission of Berlin Product People GmbH. If you would like permission to reproduce or otherwise publish any part or all of this publication or its text, including translations thereof, write to us at info@berlin-product-people.com addressed “Attention: Permissions Request.”"
    # )
    # st.caption("Materials in the app used with permission of Stefan Wolpers")





selected = st.text_input("Seach...")
button_clicked = st.button("OK")


if selected:
    col1, col2 = st.columns(2)
    with col1:
        center = [46.5739667965278,-98.338623046875]
        zoom_start=6
        data = pd.read_json('CP-2/meta-North_Dakota.json',lines=True)
        coord = [data['latitude'][0],data['longitude'][0]]
        m_type_1 = "cartodbdark_matter"
        m_type_2 = "cartodbpositron"
        m_type_3 = "OpenStreetMap"
        m = folium.Map(location=center, zoom_start=zoom_start, tiles=m_type_3)
        folium.Marker(
        coord, popup="Liberty Bell", tooltip="Liberty Bell"
        ).add_to(m)
        st_data = st_folium(m,width=400)
    with col2:
        st.write("Check")
    # with col4:
    #     st.text(name[3])
    #     st.image(posters[3])
    # with col5:
    #     st.text(name[4])
        # st.image(posters[4])


