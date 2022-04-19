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


## closest_cuisines(N, train_df, train_features, input_ingredients, cuisine_pred)


## Main Function


### Getting yummly.json

### Split dataset to train and test data

# Assumptions & Bugs
## Assumptions
#### Times are not redacted.
- I assumed that time is not the sensitive information worth redacting. It can also provide a little bit of context. 

#### Phone number have too many forms
- I have assumed that my regular expression have the ability to detect most of the common phone number formats, but it might also unrecognize some unfamiliar patterns. 

#### SpaCy
- I have assumed that SpaCy will tokenize the words and label them accurately (but in reallity it is clearly not). 

#### Email Prefix
- I assumed that most of the email prefixes contain names. Therefore I generalized it and redact all the email prefixes. 

#### Names in Addresses
- It can be assumed that most of the street address would be someone's name, and that might cause a little bit of a confusion to the program. Thus, I decided to have the order of redaction to redact addresses first before names in the case that both categories are being redacted.

#### Dates in Phone Numbers
- It can also be assumed or observed that some patterns for date might be included in some of the phone numbers, therefore I order the redaction to have phone numbers redacted before dates in the case that both categories are being redacted. 

#### GLOB deals with input
 -  Since we are taking in an argument specifying which type(s) of files are being read. The program would only choose to read the specified file type and ignore the rest. Therefore I assumed that we do not need any 'input unable to read' handler. 

## Bugs
#### Not all the names are redacted
- NLTK and SpaCy are not being so accurates with names. Also, names are not detected if they are enclosed within other special characters. e.g. "Name LastName". 
- Some short names are not being detected and some common names are being mislabeled into GPE or ORG. 
- So, for the leftover names, I try to redact them with the nommon-names list. 
#### Some formats of phone number are not fully redacted.
#### "'s" and "\n" is categorized as PERSON
#### redacting dates accidentlly redacts some phone number
- So, phone number redaction will be done first. 
#### Dates that are not in the normal format are not redacted.
#### SpaCy also tokenize the string in a strange way where it separates every word at white space. 
- This then also stops SpaCy from recognizing the full pattern of dates.
#### The address regular expression catches some abbreviation of text like 15 min. or $100 million 
- Might be because this looks like an address. 
#### I had to create a new 'project1' folder in 'tests' folder to store common_names.txt
- without this, pytest could not find the common_names.txt file.


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

### spacy_test.py
This function test SpaCy to see if it is tokenizing just fine. I let SpaCy tokenize a text string and compared to the expected list of tokens/words. 

### test_address.py
This function test if the address redactor function can detect and redact the address from the text. A string with several forms of address were redacted and compared with the expected output.

### test_concepts.py
In this test, I tried to test to see of the concepts are being recognized and of the whole sentence is being redacted by the concept redactor fucntion. 

### test_dates.py
Dates of various forms were being tested to see if the regualar expression in date redactor function can detect dates in its different forms. 

### test_email.py
This function simply tested to see if the email prefixes are being redacted by the email prefix redactor function. (The part in front of @ sign)

### test_genders.py
This test tests gender redactor function so see if the function can lemmatize the words and catch gender specific terms using the flags list. 

### test_names.py
This function test if name redactor function can redact different names in a string.  

### test_phones.py
Several phone numbers with unique patterns are given to test if phone redactor function can catch the phone numbers in these various patterns. 

# Outputs
The outputs are written into a specified folder on the same level as project1/
The output file will have the same name as the input with .redacted appended as an extention.
`"./"+output_path + fileName + ".redacted"`
