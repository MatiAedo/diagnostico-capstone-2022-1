
def most_retweeted(data):
    # Utilizando columna retweetCount
    #10 tweets
    out = data.sort_values(by ='retweetCount', axis = 0, ascending = False).head(10)
    return out