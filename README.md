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
- A PDF file with just a cat;
- A PDF file with text and an image of a cat;
- A PDF file with many, many words, to test if the app works on documents with multiple pages;
- A PDF file with an image that is not a cat.
- A PDF file with an image of a cat AND an image of a dog.

Then I've searched the internet for a list of English stop words, which I found [here](https://gist.github.com/sebleier/554280).
This is from the NLTK library, which, as I learned, is a popular library for natural language processing. It could've helped me but I've decided to keep it simple.

I have subsequently used the PyMuPDF library to extract the text (and eventual image) from the PDF file.

As you can see from the commit history, I've decided to develop the app step-by-step: first I made sure the normal word count was fine, then I added the stop words filter, and finally I added the image detection.
Of course I also needed to convert the text to lowercase to make sure the stop words filter worked properly.
For the image detection, the requirements said that there could be only one image, but I've decided to make it more flexible and detect multiple images in the PDF.
I have implemented it using the PyTorch and Pillow libraries, after reading a bit about my options on various StackOverflow threads.

As a final touch, I've tried customizing the app a bit, changing the theme, title and favicon.
Finally, I've deployed the app on Streamlit Sharing, which you can access by clicking [here](https://pdf-cat-reader.streamlit.app/).

Thanks a lot for the opportunity, I hope you like the app! 😊