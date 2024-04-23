import streamlit as st
import glob
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.express as px


st.title('Graphs')
# Extract file names
filepaths = glob.glob('2023-10-2*.txt')
print(filepaths)

# Read files and extract values
fecha = []
positive = []
negative = []

for filename in filepaths:
    with open(filename, 'r') as file:
        note = file.read()
    analyzer = SentimentIntensityAnalyzer()
    result = analyzer.polarity_scores(note)
    positive.append(result['pos'])
    negative.append(result['neg'])
    fecha.append(filename.strip('.txt'))


# Positive plot
st.subheader('Grafico de positividad')

figure = px.line(x=fecha, y= positive, labels={'x': 'Fecha', 'y': 'valor'})
st.plotly_chart(figure)

# Negative plot
st.subheader('Grafico de negatividad')

figure = px.line(x=fecha, y=negative, labels={'x': 'Fecha', 'y': 'valor'})
st.plotly_chart(figure)
