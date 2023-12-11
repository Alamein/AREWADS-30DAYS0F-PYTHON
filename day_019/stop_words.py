stop_words = ['i','me','my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up','down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]




def most_spoken_languages(file_n,v):
    '''
    Takes a filepath and an integer,n as arguments and returns the n most spoken languages in the world
    '''
    with open(file_n) as fl:
        list = json.loads(fl.read())
    # looping to get dict of languages
    languages = []
    for i in range(len(list)):
        languages.extend(list[i]['languages'])
    lang = {}
    for language in languages:
        lang[language] = lang.get(language,0) + 1
    # sorting the list of the tuples to get the most spoken languages
    sorted_lang = sorted(lang.items(), key= lambda x:x[1],reverse=True) # contains the languages arranged based on values
    result = [(item[1],item[0]) for item in sorted_lang]
    return result[:v]
most_spoken_languages('ountries_data.json',10)


def most_spoken_languages(file_n,v):
    '''
    Takes a filepath and an integer,n as arguments and returns the n most spoken languages in the world
    '''
    with open(file_n) as fl:
        list = json.loads(fl.read())
    # looping to get dict of languages
    languages = []
    for i in range(len(list)):
        languages.extend(list[i]['languages'])
    lang = {}
    for language in languages:
        lang[language] = lang.get(language,0) + 1
    # sorting the list of the tuples to get the most spoken languages
    sorted_lang = sorted(lang.items(), key= lambda x:x[1],reverse=True) # contains the languages arranged based on values
    result = [(item[1],item[0]) for item in sorted_lang]
    return result[:v]
most_spoken_languages('ountries_data.json',10)