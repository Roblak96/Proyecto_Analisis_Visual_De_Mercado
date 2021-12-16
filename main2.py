import streamlit as st



st.title('IBEX 35')

#st.header(Image(url= "https://img.s3wfg.com/web/img/images_uploaded/4/d/ibex35cb22.gif"))


empresas = ['Acciona', 'Acellormital', 'Acerinox', 'ACS', 'Aena', 'Almiral', 'Amadeus', 'BBVA', 'Caixabank', 'Cellnex', 'Cieautomotive', 'Colonial', 'Enagas', 'Endesa', 'Ferrovial', 'Grifols', 'Hotels', 'Iberdrola', 'ICAG', 'Inditex', 'Indra', 'Mapfre', 'Merlin', 'Naturgy', 'Pharmamar', 'Redelectrica', 'Repsol', 'Sabadell', 'Santander', 'Solaria', 'Telefonica', 'Viscofan']

st.selectbox("Elige una empresa", ["Elige una opción"] + empresas)