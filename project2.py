# required packages
import argparse
import urllib.request  # for downloading from url
import os              # for OS operations
import json            # for dealing with json files
import pandas as pd    # for dataframe
import numpy as np     # for array
from sklearn.model_selection import train_test_split         # for spliting dataset
from sklearn.feature_extraction.text import CountVectorizer  # for vectorizer to extract features
from sklearn.ensemble import RandomForestClassifier          # for Random Forest model
from sklearn.svm import LinearSVC                            # for SVM model
from sklearn.model_selection import cross_val_score          # for cross validation
from sklearn.metrics.pairwise import cosine_similarity       # for comparing the cuisines using cosine similarity


def predict_cuisine(input_ingredients, ingredient_train, ingredient_test, cuisine_train, cuisine_test):
    # modeling
    # extract features                                           
    cv = CountVectorizer(binary = False, ngram_range=(1,3))
    train_features = cv.fit_transform(ingredient_train)
    test_features = cv.transform(ingredient_test)
    
    # random forest classifier model
    #rf = RandomForestClassifier(n_estimators=64).fit(train_features, cuisine_train)
    
    # support vector machines 
    svm = LinearSVC(penalty = 'l2', C =1, random_state = 42, max_iter = 10000)
    svm.fit(train_features, cuisine_train)
    
    # test the model
    #test_score = rf.score(test_features, cuisine_test)    # this gets 0.705019693287522
    confidence = svm.score(test_features, cuisine_test)  # this gets 0.7628425375010475
    
    # predicting
    ingredients = []
    ingredients.append(' '.join(input_ingredients))
    input_features = cv.transform(ingredients)
    
    # predict the  cuisine
    cuisine_pred = svm.predict(input_features)
    #cuisine_pred = rf.predict(input_features)
  
    # data for the input ingredients
    input_cuisine = {'ID' : 'arbitary', 'cuisine' : cuisine_pred[0], 'ingredients' : ingredients[0]}

    return(cuisine_pred, input_cuisine, confidence)
    
def closest_cuisines(N, train_df, train_features, input_ingredients, cuisine_pred):
    # compute the cosine similarity
    similarities = cosine_similarity(train_features)
    similarities_df = pd.DataFrame(similarities)

    # look for the input data index
    ID_list = train_df['ID'].values
    input_index = np.where(ID_list == 'arbitary')[0][0]

    # similar_food list stores the cosine similarities among all cuisines to the input ingredients
    similar_food = similarities_df.iloc[input_index].values

    # store the top N similar cuisine in the following list
    similar_food_indexes = np.argsort(-similar_food)[1:N+1]
    
    # now store them in a dictionary to be passed into the final result
    closest_food_list = []
    for i in similar_food_indexes:
        tmpDict = {}
        tmpDict['id'] = str(ID_list[i])
        tmpDict['score'] = float(round(similarities_df[i][len(train_df)-1],2))
        closest_food_list.append(tmpDict)
    return closest_food_list



def main(N, input_ingredients):
    # get current working directory
    cwd = os.getcwd()
    # download yummly.json
    urllib.request.urlretrieve("https://oudatalab.com/cs5293sp22/projects/yummly.json", cwd + "/docs/yummly.json")

    # read open yummly.json file
    f = open(cwd + "/docs/yummly.json", "rb")
    data = json.load(f)

    # parse yummly into a dataframe
    ID = []           # a list to hold IDs
    cuisine = []      # a list to hold cuisine labels
    ingredients = []  # a list to hold ingredients
    for obj in data:
        ID.append(obj['id'])
        cuisine.append(obj['cuisine'])
        ingredients.append(' '.join(obj['ingredients']))
    # create dataframe using pandas
    foods = {'ID' : ID, 'cuisine' : cuisine, 'ingredients' : ingredients}
    df = pd.DataFrame(foods)
    f.close() # Closing file


    # split data into train and test dataset (train/test = 0.7/0.3)
    ingredient_train, ingredient_test, cuisine_train, cuisine_test, ID_train, ID_test = train_test_split(np.array(df['ingredients']), np.array(df['cuisine']), np.array(df['ID']), test_size = 0.30, random_state = 42)


    # predict the cuisine
    cuisine_pred, input_cuisine, confidence = predict_cuisine(input_ingredients, ingredient_train, ingredient_test, cuisine_train, cuisine_test)


    # compute the similarities
    train_data = {'ID' : ID_train[:5000], 'cuisine' : cuisine_train[:5000], 'ingredients' : ingredient_train[:5000]} # need to size the data down to 5,000, otherwise the virtual machine will not have enough ram
    train_df = pd.DataFrame(train_data)
    train_df = train_df.append(input_cuisine, ignore_index = True) # add the input data as well

    cv = CountVectorizer(binary = False, ngram_range=(1,3))
    train_features = cv.fit_transform(train_df['ingredients'])
    closest_food_list = closest_cuisines(N, train_df, train_features, input_ingredients, cuisine_pred) # a list containing the closest cuisines


    # output
    results = {}      # a dictionary containg the results
    results['cuisine'] = str(cuisine_pred[0])
    results['score'] = float(round(confidence,2))
    results['closest'] = closest_food_list
    # make them into json format
    results_json = json.dumps(results, indent = 4)
    
    # final output
    print(results_json)

    # return some elements for test
    return(cuisine_pred, closest_food_list)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--N", type = int, action = "store", help = "number of closest cuisines" , required = True)
    parser.add_argument("--ingredient", type = str, action = "append", help = "ingredient flags" , required = True)

    args = parser.parse_args()

    # transfer input variables
    N = int(args.N)
    input_ingredients = args.ingredient
    # call main function to run the program
    main(N, input_ingredients)
