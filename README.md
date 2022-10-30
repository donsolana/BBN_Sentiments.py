# BBN_Sentiments.py

## Introduction :wave:

Big Brother Naija is the most popular reality franchise in Nigeria, but the influence of this show spreads far beyond Nigeria's borders. In this project I partnered with my a friend and Jedi in training to analyse impressions about the show from Twitter. [Seun](https://github.com/Crownthirst), my partner for this project scrapped and organised the data from twitter and also effectively co-managed the project. I built the program for analysing the sentiments with Transformer models, I also built and deployed a web app to provide self serve analytics for interested users.

### How to use  :page_with_curl:

To use this program, you can follow these steps.
1. Ensure you install all the dependences from the `requirements.txt` file (preferrably in a virtual environment).
2. Make sure all the Python files in this repo are in the same folder.
3. Run `app.py` from a runtime or virtual env with all the installed packages.

### Summary of Architecture :triangular_ruler:
Here I summarise how and why the program was built the way it is.
The program is modularised across the files namely:
* `app.py` 
* `preprocess.py`
* `predict.py`

This modular build ensure that each component file is reuseable and can be easily modified or extended for future projects.

1. The app file, when initialised first aquires data from a remote location(github blob).
2. The data is read in as a pandas dataframe.
3. This data frame is then passed to the preprocessing step, where non-alphanumeric characters, and other unwanted objects are cleaned.
4 The process file doesn't include any vectorization or encoding as that is handled my the transformer pipeline.
5. Next, the preprocessed data is passed to the transformer pipeline in the `predict.py` file and the sentiment analysis operation begins.



### Tooling :hammer:
| Function | Tool |
|----------|------|
| Data Wrangling | Pandas|
| Preprocessing | Regex(Re), BS4|
| Sentiment Model| Hugging Face Transformers|

### Improvements :star:
Two other versions of this program exist as Flask files and Serverless APIs for Azure. In future iterations(perharps for next year) we deploy this code and hook it up to a pipeline that wrangles live tweets, analyses them, stores them and serve results as a dashboard.
