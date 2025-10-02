import streamlit as st
import sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

@st.cache_data
def load_data():
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names

df, target_names = load_data()

model=RandomForestClassifier()
model.fit(df.iloc[:,:-1],df['species'])

st.sidebar.title("Input Features")
sepal_length = st.sidebar.slider("Sepal Length", float(df.sepal length.min()), float(df.sepal length.max()), float(df.sepal length.mean()))
