import re 
from textblob import TextBlob 

def get_sentiment(text): 
        ''' 
        Utility function to classify sentiment of passed tweet 
        using textblob's sentiment method 
        '''
        # create TextBlob object of passed tweet text 
        analysis = TextBlob(text) 
        analysis.tags
        analysis.noun_phrases
        print(analysis)

        for sentence in analysis.sentences:
            print(sentence.sentiment.polarity)


        # set sentiment 
        if analysis.sentiment.polarity > 0: 
            return 'positive'
        elif analysis.sentiment.polarity == 0: 
            return 'neutral'
        else: 
            return 'negative'


if __name__ == "__main__":
    # for debug purposes
    print(get_sentiment(text))
