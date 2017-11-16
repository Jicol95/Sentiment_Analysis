import sys
import numpy

def initDic():
    with open('../Test_Files/nokia-pos.txt', 'r', encoding="ISO-8859-1") as x:
        posText = x.read()#.replace('\n', '')
        posText = posText.split('\n')

    with open('../Test_Files/nokia-neg.txt', 'r', encoding="ISO-8859-1") as y:
        negText = y.read()#.replace('\n', '')
        negText = negText.split('\n')
    #Each review ends with a " . " however, some parts end with a " . ", even if it isn't the end of the review."

    reviewData = {}

    #For using the data parts for an array do: posReviews = [], then, posReviews.append(reviewData['positiveReviews']), or even do a loop if needed.
    reviewData['positiveReviews'] = posText
    reviewData['negativeReviews'] = negText

    # for x in reviewData['positiveReviews']:
    #     print(x)
    # for x in reviewData['negativeReviews']:
    #     print(x)
    return reviewData

if __name__ == '__main__':
    initDic()
