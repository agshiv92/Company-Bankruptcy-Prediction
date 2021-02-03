# Bankruptcy Prediction for Company using Machine Learing
Bankruptcy is an event when a company can not pay its debt. Bankruptcy give freedom to the company from all its debt. Bankruptcy is important event as the debter has to take haircut for the amount they have given to copmany which is declaring bankruptcy. In general a company moving towards bankruptcy will get the debt at higher interest rate. Bankruptcy prediction can help Banks to finalize the interest rate, financial institution and general public for investement decision. 

## Project Set Up and Installation
Some part of this project required access of Azure Machine Learning portal. You may need to create the account to execute the code of this experiment. 

## Dataset

### Overview
The data were collected from the Taiwan Economic Journal for the years 1999 to 2009. Company bankruptcy was defined based on the business regulations of the Taiwan Stock Exchange. This dataset has 6219 example for training. The dataset of 95 different financial ratios as features. This dataset is avaialable at kaggel. 

### Task
This is a binary classification task where our target column is Bankrupt which may have the value 1 in case the company goes bankrupt 0 in case the company does not goes bankrupt.

### Access
The data has been downloaded from Kaggle then uploaded to Azure Machine Learning Studio's Datasets where it'll be used to train the models. Please clicke here to download the dataset from Kaggle

## Automated ML
In order to train and deploy best model using Azure Auto ML below steps are required:-
1. Login to Azure portal 
2. Create Azure Machine Learing portal
3. Creating the experiment 
4. Downloading the dataset 
5. Importing the dataset 
6. Creating Azure Auto ML and configuring it 
7. Creating new compute or using existing one
8. Sumitting the Azure Auto ML run 
9. Selecting the best model and deploying it to webservice
10. Consuming the best model using webservices

Below configuration is used for Auto ML 
1. Experiment Timeout 
2. Task
3. Primary Metric = Precision 
4. Compute target 
5. Target Variable 
6. Cross Validation 
7. Auto Featurization 
8. Early Stop

### Results

Best Model:- 
Precision of the Model:- 
Accuracy of the Model:- 

Ways to increase the a Precision:
a. Changing the experiment time out time
b. Enabling Deeplearning 
c. Increasing the cross validation

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Hyperparameter Tuning
*TODO*: What kind of model did you choose for this experiment and why? Give an overview of the types of parameters and their ranges used for the hyperparameter search


### Results
*TODO*: What are the results you got with your model? What were the parameters of the model? How could you have improved it?

*TODO* Remeber to provide screenshots of the `RunDetails` widget as well as a screenshot of the best model trained with it's parameters.

## Model Deployment
*TODO*: Give an overview of the deployed model and instructions on how to query the endpoint with a sample input.

## Screen Recording
*TODO* Provide a link to a screen recording of the project in action. Remember that the screencast should demonstrate:
- A working model
- Demo of the deployed  model
- Demo of a sample request sent to the endpoint and its response

## Standout Suggestions
*TODO (Optional):* This is where you can provide information about any standout suggestions that you have attempted.
