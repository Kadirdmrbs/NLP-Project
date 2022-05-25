import streamlit as st
import joblib
import time
model = joblib.load('text_clf_lsvc.joblib')

Review = st.text_input('Enter Review')

ok = st.button('Predict')

if ok:
    with st.spinner('Classifying ...'):
        time.sleep(2)
        answer = model.predict([Review])
        if answer == ['neg']:
            st.subheader("This review is negative")
        else:
            st.subheader("This review is positive")
        st.success('Done!')