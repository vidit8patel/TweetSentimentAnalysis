# Tweet Sentiment Analysis
Sentiment Analysis of Tweets

This project shows the sentiments of tweets of a dataset i.e., if it is positive or negative. After training various models, Logistic Regression was found to be the best and it is used to predict further new input tweets given by the user.

<a href="https://colab.research.google.com/drive/1CkEBxtG98w0BzTnUneqBZzfyC3hk8Y8r?usp=sharing">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

Installation
To run this project, follow the steps below:

Clone the repository to your local machine using the following command:

bash
Copy code
git clone https://github.com/your-username/sentiment-analysis-tweets.git
Change into the project directory:

bash
Copy code
cd sentiment-analysis-tweets
Create a virtual environment (optional but recommended) and activate it:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # for Linux/Mac
venv\Scripts\activate  # for Windows
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Usage
Once the project is set up, you can run the sentiment analysis tool using Streamlit. Make sure you are in the project directory and the virtual environment is activated (if you created one). Run the following command:

bash
Copy code
streamlit run app.py
This command will start the Streamlit server, and you will see output similar to the following:

arduino
Copy code
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.0.100:8501
Copy the local URL (e.g., http://localhost:8501) into your web browser, and the sentiment analysis tool will be displayed.
