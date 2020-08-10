#!/usr/bin/env python
# coding: utf-8

# In[1]:print ("hello")


import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
x=pd.read_csv('Downloads/ml-latest-small/tags.csv')

movietags={}
for index,i in x.iterrows():
    temp=i['movieId']
    if temp in movietags and i['tag'] not in movietags[temp]:
        movietags[temp].append(i['tag'])
    else:
        movietags[temp]=[i['tag']]


gnrs_dict={}
mvs=pd.read_csv('Downloads/ml-latest-small/movies.csv')
mvs['genres']
for index,i in mvs.iterrows():
    gnrs_dict[i['movieId']]=i['genres']


for i in gnrs_dict:
    gnrs_dict[i]=gnrs_dict[i].split('|')

titles={}
ttls=[]
for index,i in mvs.iterrows():
    ttls.append(i['title'])
    titles[i['movieId']]=i['title']


for i in gnrs_dict:
    if i in movietags:
        gnrs_dict[i]+=movietags[i]


a=list(gnrs_dict.values())
b=[]
for i in a:
    temp=""
    for j in i:
        temp+=j
        temp+=','
    b.append(temp)


mvs['keywords']=b

count=CountVectorizer()
count_matrix=count.fit_transform(mvs['keywords'])


similarity=cosine_similarity(count_matrix,count_matrix)


'''def myreccomender(title,similarity=similarity):
    for i in range(0,len(ttls)):
        if ttls[i]==title:
            pointer=i
            break
    #similar_movies=similarity[pointer]
    #similar_movies.sort(reverse=True)
    #similar_movies=similar_movies[:11]
    score_series=pd.Series(similarity[pointer]).sort_values(ascending=False)
    top10=list(score_series.iloc[1:50].index)
    final=[]
    for i in top10:
        final.append(ttls[i])
    return final'''
a=pd.read_csv('Downloads/ml-latest-small/links.csv')
b=pd.read_csv('Downloads/ml-latest-small/movies.csv')
links=[]
for index,i in a.iterrows():
    links.append('http://www.imdb.com/title/tt0'+str(int(i['imdbId']))+'/')
links
def myreccomender(title,similarity=similarity):
    for i in range(0,len(ttls)):
        if ttls[i]==title:
            pointer=i
            break
    #similar_movies=similarity[pointer]
    #similar_movies.sort(reverse=True)
    #similar_movies=similar_movies[:11]
    score_series=pd.Series(similarity[pointer]).sort_values(ascending=False)
    top10=list(score_series.iloc[0:50].index)
    final_dict=[]
    #final=[]
    for i in top10:
        final=[]
        final.append(i)
        final.append(ttls[i])
        final.append(links[i])
        if i in gnrs_dict:
            final.append(gnrs_dict[i])
        final_dict.append(final)
        
    return final_dict
#print(myreccomender('Two if by Sea (1996)'))



###################################################################

#import pandas as pd
from flask import Flask, jsonify, request
#import pickle
from flask_cors import CORS
import json
# load model
#model = pickle.load(open('model.pkl','rb'))

# app
app = Flask(__name__)
CORS(app)
# routes
@app.route('/', methods=['POST','GET'])

def predict():
    #print ()
    print (request.method)
    if request.method=='POST':
        data = request.get_json(force=True)
        f=open('demofile3.txt',"w")
        f.write(str(data))
        f.close()
        return jsonify(data)

    # convert data into dataframe
    else:
        f=open('demofile3.txt','r')
        data=f.read()
        f.close()
        data_df=str(data)
    # predictions
        #inpt=prev
    #f = open("demofile3.txt", "r")
    #inpt='Heat (1995)'
    #print (inpt)
    #data_df=str(inpt)
        result = myreccomender(data_df)

    # send back to browser
        output = result

    # return data
    #print (output)
        return jsonify(output)



if __name__ == '__main__':
    app.run(port = 5000, debug=True)



