import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.write("st.write")

st.markdown("st.markdown")

st.header("st.header")
st.subheader("st.subheader")
st.caption("st.caption")
st.text("st.text")
st.latex("st.latex")
st.code("st.code")

st.write("tes write *halo* :halo00:")

st.write(923808)

df = pd.DataFrame({
    'column':[1,2,3,4],
    'kolom':[10,20,30,40]
})

st.write(df)

st.write('bawah dataframe',df,'atas dataframe')

df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns = ['a', 'b', 'c']
)

c= alt.Chart(df2).mark_circle().encode(
    x="a",
    y="b",
    size="c",
    tooltip=['a', 'b','c' ],
  
)

st.write(c)