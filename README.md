# predict_stock_py
Based on the work of ciurana2016 - https://github.com/ciurana2016/predict_stock_py

## Overview
A updated version of the work of ciurana2016. Used as a learning project
where I improved and fixed parts of the code that no longer worked.

As intended in the original version, the code do the folowing:

1. Asks the user for a stock quote from NASDAQ (e.j: AAPL, FB, GOOGL)
2. Uses Tweepy to retrieve tweets about that stock.
3. Uses TextBlob to determine if the majority of the tweets are positive using sentiment analisys and print the result as an suggestion
4. Also downloads the last few years of prices for that stock, and trains a neural net with that data to predict the price for tomorrow.

The folder "data" contains the downloaded csv of the stocks


## Dependencies
* numpy (http://www.numpy.org/)
* tweepy (http://www.tweepy.org/)
* textblob (https://textblob.readthedocs.io/en/dev/)
* requests(http://docs.python-requests.org/en/master/)
* python-dotenv
* keras(https://keras.io/) Runs with [TensorFlow](https://www.tensorflow.org/) or [Theano](http://deeplearning.net/software/theano/), so you will need one of them.


# Usage
Install all the necessary dependencies.
Then just run:
```
python3 main.py
```
It will ask you for a NASDAQ quote, e.j: AAPL, then if the sentiment is positive and the stock you entered exists it will start training the network and give you a result.


# Credits
Credits to
[ciurana2016](https://github.com/ciurana2016/predict_stock_py) and [Siraj](https://github.com/llSourcell) for inspiring me in the AI/Deep Learning 
