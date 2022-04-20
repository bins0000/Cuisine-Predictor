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

## How to run
In the repository outer most directory (cs5293sp22-project1/ where redactor.py is located), you can call `redactor.py` to run the program by using the following command:- 

    pipenv run python redactor.py --input '*.txt' \
                        --names --dates --phones --genders --address\
                        --concept 'kids' \
                        --output 'files/' \
                        --stats stderr
Among the arguments, --input and --concept can take more than one arguments. For example, you might pass in --concept food --concept school for concept. 

# The functions

## predict_cuisine(input_ingredients, ingredient_train, ingredient_test, cuisine_train, cuisine_test)
this function takes the following parameters: input_ingredients, ingredient_train, ingredient_test, cuisine_train, and cuisine_test. The names of the parameters are straight forward.

Then the function models the clasifier model using scikit-learn package. In this case, SVM model was used as it produces higher confidence score. 

## closest_cuisines(N, train_df, train_features, input_ingredients, cuisine_pred)


## Main Function


### Getting yummly.json

### Split dataset to train and test data

# Assumptions & Bugs
## Assumptions
#### Times are not redacted.
- I assumed that time is not the sensitive information worth redacting. It can also provide a little bit of context. 



## Bugs
#### Not all the names are redacted
- NLTK and SpaCy are not being so accurates with names. Also, names are not detected if they are enclosed within other special characters. e.g. "Name LastName". 
- Some short names are not being detected and some common names are being mislabeled into GPE or ORG. 


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
