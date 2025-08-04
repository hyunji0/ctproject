import streamlit as st
import pandas as pd
#import plotly.figure_factory as ff
import plotly.express as px  # ff보다 많이 씀, 동적인 라이브러리
# import matplotlib.pyplot as plt  정적인 라이브러리
st.set_page_config(layout='wide',page_title='My App')

# html variable
html = '''
<html>
    <head>
        <title>This HTML App</title>
    </head>
    <body>
        <h1>This Long Text!!!</h1>
        <br>
        <hr>
        <h3>This a small text</h3>
    </body>
</html>
'''

with open('!DOCTYPE html.html', 'r', encoding='utf-8') as f:
    filehtml = f.read()
    f.close()

# global variable
url = "https://www.youtube.com/watch?v=XyEOEBsa8I4"

# data app
df = pd.read_csv('./data/data.csv', encoding='cp949')

st.title('This is my first webapp!')
col1, col2 = st.columns((4,1))
with col1:
    with st.expander('Content1...'):
        st.subheader('Content1...')
        st.video(url)
    with st.expander('Content2...'):
        st.subheader('Content2...')
        st.table(df)
        dff=df.groupby(by='name').sum()
        fig = px.bar(dff, x=dff.index, y='math')
        st.plotly_chart(fig)
        st.table(dff)
    with st.expander('Content3_image...'):
        st.subheader('Content3_image...')
        st.image('./images/catdog.jpg')
        #st.write('<h1>This is new title</h1>', unsafe_allow_html=True)
        st.markdown(html, unsafe_allow_html=True)
    with st.expander('Content3_htmlContent...'):
        st.subheader('Content3_htmlContent...')
        import streamlit.components.v1 as htmlviewer
        htmlviewer.html(filehtml, height=800)

with col2:
    with st.expander('Tips...'):
        st.subheader('Tips...')