# App purpose
I wrote this app as a test for Octostar.
The application should let the user upload a PDF file.
Then, the app should count the words in the PDF file and display the result to the user, without counting stop words.
Additionally, if there's an image in the PDF and said image contains a cat, the app should display a message to the user.

# How to run the application
Assuming you have Streamlit installed, you can run the app by executing the following command in your terminal:

```bash
streamlit run app.py
```

If you don't have Streamlit installed, you can install it by running the following command:

```bash
pip install streamlit
```

# Explanation
I first went through the Streamlit documentation to understand how to use the library and create a simple app.

First, I've created 3 documents to test the app:
- A PDF file with text only;
- A PDF file with text and an image of a cat;
- A PDF file with many, many words, to test if the app works on documents with multiple pages;

Then I've searched the internet for a list of English stop words, which I found [here](https://gist.github.com/sebleier/554280). 

I have subsequently used the PyMuPDF library to extract the text (and eventual image) from the PDF file.

Finally, I've deployed the app on Streamlit Sharing, which you can access by clicking [here](https://share.streamlit.io/).
