# cs5293sp22-project2
# Author Nasri Binsaleh
#### See COLLABORATORS.txt for related links

# How to install, directions on how to use the code, and some example of how to run.

## First, installation, simply clone the github ripository to your machine.
This github repository can be cloned using the following command:-  
    ```git clone "git repository link"```
    
    
## Activating pipenv in the project directory


## Prerequisites
    [packages]
    spacy = "*"
    nltk = "*"
    pytest = "*"

    [requires]
    python_version = "3.10"
You should be able to install above packages using pipenv install 'package'
  e.g. pipenv install pandas
The rest of the requirements will be import by the program. Also, make sure to create and use the environment with python 3.10


## Directories
    cs5293sp22-project2
        ├── COLLABORATORS
        ├── LICENSE
        ├── Pipfile
        ├── Pipfile.lock
        ├── README.md
        ├── docs
        │   └── yummly.json
        ├── project2.py
        ├── setup.cfg
        ├── setup.py
        └── tests
The program to run is ```project2.py``` in the main directory cs5293sp22-project2
## How to run
You can call `project2.py` in the commandline to run the program by using the following command as an example:- 

    pipenv run python project2.py --N 5 --ingredient paprika --ingredient banana  --ingredient "rice krispies" 

Among the arguments, --N takes in an integer that indicates the amount of the closest cuisine ID to be showed, and --ingredient can take multiple items which are the ingredients that the user would want to input for the prediction. 

# Functions in this program

## predict_cuisine(input_ingredients, ingredient_train, ingredient_test, cuisine_train, cuisine_test)
this function takes the following parameters: input_ingredients, ingredient_train, ingredient_test, cuisine_train, and cuisine_test. The names of the parameters are straight forward.

Then the function models the clasifier model using scikit-learn package. In this case, SVM model was used as it produces higher confidence score. 

Once the SVM classifier is modelled, the test data was used to find the prediction accuracy to be used as our confidence score for the prediciton.

Then on the ingredient list that was input, the cuisine was predicted using SVM classifier. Then the items being returned from this function are the predicted cuisine, the confidence score, and a dictionary of the new cuisine that was generated from the input ingredients. This dictionary of input ingredients is then used for comparing with other cuisines for similarity. 

## closest_cuisines(N, train_df, train_features, input_ingredients, cuisine_pred)


## Main Function


### Getting yummly.json

### Split dataset to train and test data

# Assumptions & Bugs
## Assumptions
#### Train and Test split 
- Train and Test data were split into 70% and 30% respectively, with the assumption that 70% of data is enough to predict with high accuracy.

#### Testing with the holdout testing set is enough
- with this assumption, I did not need to evaluate the model with cross validation. 

## Bugs

#### Random Forest
- when the number of trees in the forest is higher than 10, the virtual machine cannot handle the modeling.
- 
#### Data size in finding similarities with cosine similarity
- The data size for finding similarity is limited to about 5,000 elements. More than that would cause the virtual machine to die.  

# Test
### 
    ├── glob_test.py
    ├── project1
    │   └── common_names.txt
    ├── spacy_test.py
    ├── test_address.py
    ├── test_concepts.py
    ├── test_dates.py
    ├── test_email.py
    ├── test_genders.py
    ├── test_names.py
    └── test_phones.py
As can be seen from the trees above, several test was done to check if a particular component is working. 
  
### glob_test.py
This test was done to check if glob can actually locate the file with the given extention. In this case, I simply want glob to look for common.names.txt in projext1 folder. 



# Outputs
The outputs are written into a specified folder on the same level as project1/
The output file will have the same name as the input with .redacted appended as an extention.
`"./"+output_path + fileName + ".redacted"`
