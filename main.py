import sys
import requests
import numpy as np
from inc import twitter

from keras.models import Sequential
from keras.layers import Dense
from textblob import TextBlob

# Where the csv file will live
FILE_NAME = 'data/historical.csv'

def stock_sentiment(quote, num_tweets):
    list_of_tweets = twitter.q(quote, num_tweets)
    positive, null = 0, 0

    for tweet in list_of_tweets:
        blob = TextBlob(tweet.text).sentiment

        if blob.subjectivity == 0:
            null += 1
            next
        if blob.polarity > 0:
            positive += 1

    if positive > ((num_tweets - null)/2):
        return True


def get_historical(quote):
    url = 'https://app.quotemedia.com/quotetools/getHistoryDownload.csv?&webmasterId=501&startDay=02&startMonth=02&startYear=2002&endDay=02&endMonth=12&endYear=2017&isRanged=false&symbol=' + quote
    r = requests.get(url, stream=True)

    if r.status_code == 200:
        with open(FILE_NAME, 'wb') as f:
            for chunk in r:
                f.write(chunk)

        return True
    else:
        print('Could not load csv with financial data: ' + url)
        sys.exit()


def stock_prediction():

    # Collect data points from csv
    dataset = []

    with open(FILE_NAME) as f:
        for n, line in enumerate(f):
            if n != 0:
                dataset.append(float(line.split(',')[1]))

    dataset = np.array(dataset)

    # Create dataset matrix (X=t and Y=t+1)
    def create_dataset(dataset):
        dataX = [dataset[n+1] for n in range(len(dataset)-2)]
        return np.array(dataX), dataset[2:]

    trainX, trainY = create_dataset(dataset)

    # Create and fit Multilinear Perceptron model
    model = Sequential()
    model.add(Dense(8, input_dim=1, activation='relu'))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(trainX, trainY, batch_size=2, epochs=500, verbose=0)

    # Our prediction for tomorrow
    prediction = model.predict(np.array([dataset[0]]))
    result = 'The price of ' + stock_quote + ' will move from %s to %s' % (dataset[0], prediction[0][0])

    return result


# Ask user for a stock quote
stock_quote = input('Enter a stock quote from NASDAQ (e.j: AAPL, FB, GOOGL): ').upper()

# Check if the stock sentiment is positve
if not stock_sentiment(stock_quote, num_tweets=500):
    print('This stock has bad sentiment, please re-run the script')
    #sys.exit()

# Check if we got te historical data
if not get_historical(stock_quote):
    print('Google returned a 404, please re-run the script and')
    print('enter a valid stock quote from NASDAQ')
    sys.exit()

# We have our file so we create the neural net and get the prediction
print(stock_prediction())

# We are done so we delete the csv file
os.remove(FILE_NAME)
