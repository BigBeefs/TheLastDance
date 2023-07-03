import streamlit as st
import requests
import json

def main():
    st.title("Model Prediction by BigBeefs")
    url_API ="http://localhost:8000/predict"
    rd = st.number_input("Inserisci l'importo dell'R&D")
    admin = st.number_input("Inserisci l'importo dell'Administration")
    marketing = st.number_input("Inserisci l'importo del Marketing ")

    if st.button('GET request'):
        url = url_API
        urlreq=f"?rd={rd}&admin={admin}&marketing={marketing}"
        link = url+urlreq

        response = requests.get(link)
        result =response.json()
        st.success(f"The result is: {result['prediction']}")

    if st.button("POST request"):
        url = url_API
        response =requests.post(url,
                                headers={"Content-Type": "application/json"},
                                data = json.dumps({
                                                   "rd":rd,
                                                   "admin":admin,
                                                   "marketing":marketing,
                                                   })
                                )
        result =response.json()
        st.success(f"The result is: {result['prediction']}")

if __name__ == '__main__':
    main()