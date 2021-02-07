# Bankruptcy Prediction for Company using Machine Learing
Bankruptcy is an event when a company can not pay its debt. Bankruptcy give freedom to the company from all its debt. Bankruptcy is important event as the debter has to take haircut for the amount they have given to copmany which is declaring bankruptcy. In general a company moving towards bankruptcy will get the debt at higher interest rate. Bankruptcy prediction can help Banks to finalize the interest rate, financial institution and general public for investement decision. 

## Project Set Up and Installation
Some part of this project required access of Azure Machine Learning portal. You may need to create the account to execute the code of this experiment. 
## Overview of the Project 
![Image of Yaktocat](https://github.com/agshiv92/Company-Bankruptcy-Prediction/blob/main/Presentation1.jpg)

## Dataset

### Overview
The data were collected from the Taiwan Economic Journal for the years 1999 to 2009. Company bankruptcy was defined based on the business regulations of the Taiwan Stock Exchange. This dataset has 6219 example for training. The dataset of 95 different financial ratios as features. This dataset is avaialable at kaggel. 

### Task
This is a binary classification task where our target column is Bankrupt which may have the value 1 in case the company goes bankrupt 0 in case the company does not goes bankrupt.

### Access
The data has been downloaded from Kaggle then uploaded to Azure Machine Learning Studio's Datasets where it'll be used to train the models. Please clicke [here](https://www.kaggle.com/fedesoriano/company-bankruptcy-prediction "here") to download the dataset from Kaggle

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
1. Experiment Timeout = 30 mins (Due to limitation of project lab availablity)
2. Task = Classfication (As we are trying to predict only two classes whether the company will bankrupt or not) 
3. Primary Metric = Precision (Precision is more than accuracy for this problem as investing in a bankrupt comapny will cause more hurt in comparison to not investing in a good company)
4. Compute target = Created  
5. Target Variable = "Bankrupt" (1=Bankrupt, 0 not bankrupt)
6. Cross Validation =(4 cross validation is selected to get better result)
7. Auto Featurization = (Set True to enable auto featurization)
8. Early Stop = (Set True to ensure that the resources are not wasted for non performing models)

### Results

* Best Model:- Voting Ensemble
Precision of the Model:- 93.35 % 
Accuracy of the Model:- 78.87 % 
Voting Ensemble is an ensemble machine learning model that combines the predictions from multiple other models. It is a technique that may be used to improve model performance, ideally achieving better performance than any single model used in the ensemble, that involves summing the predictions made by classification models.

* Ways to increase the a Precision:
a. Changing the experiment time out time
b. Enabling Deeplearning 
c. Increasing the cross validation 

###AutoML Run Widget:
![Image of Yaktocat](https://github.com/agshiv92/Company-Bankruptcy-Prediction/blob/main/1.JPG)
![Image of Yaktocat](https://github.com/agshiv92/Company-Bankruptcy-Prediction/blob/main/2.JPG)
![Image of Yaktocat](https://github.com/agshiv92/Company-Bankruptcy-Prediction/blob/main/3.JPG)
![Image of Yaktocat](https://github.com/agshiv92/Company-Bankruptcy-Prediction/blob/main/4.JPG)
![Image of Yaktocat](https://github.com/agshiv92/Company-Bankruptcy-Prediction/blob/main/5.JPG)
![Image of Yaktocat](https://github.com/agshiv92/Company-Bankruptcy-Prediction/blob/main/6.JPG)
![Image of Yaktocat](https://github.com/agshiv92/Company-Bankruptcy-Prediction/blob/main/7.JPG)
![Image of Yaktocat](https://github.com/agshiv92/Company-Bankruptcy-Prediction/blob/main/8.JPG)
## Hyperparameter Tuning

We have created a train.py script with following steps. 
1. Importing the csv file containing the marketing campaigns data into our dataset.
2. Cleaning the dataset, which included droping NaN values.
3. Splitting our dataset into training set (80% of the data) & test set (20% of the data.)
4. Creating a Logistic Regression model using sci-kit learn.
5. Creating a directory to save the generated model into it.

Once this file is ready, we are using this file in Hyperparameter Tuning:-

* Primary Metric = Precision
* Parameter Sampling = Random Parameter Sampling (As the dataset is huge ramdom parameter sampling will save time)
* Early Termination Policy = Bandit Policy 


### Algorithm
Logistic Regression is a supervisied binary classification algorithm that predicts the probability of a target varaible, returning either 1 or 0 (yes or no).


### Results
The best value of the Precision was found to be: 92.65%  using the following hyperparemeter values:
![Image of Yaktocat](https://github.com/agshiv92/Company-Bankruptcy-Prediction/blob/main/13.JPG)

![Image of Yaktocat](https://github.com/agshiv92/Company-Bankruptcy-Prediction/blob/main/9.JPG)
![Image of Yaktocat](https://github.com/agshiv92/Company-Bankruptcy-Prediction/blob/main/10.JPG)
![Image of Yaktocat](https://github.com/agshiv92/Company-Bankruptcy-Prediction/blob/main/11.JPG)
![Image of Yaktocat](https://github.com/agshiv92/Company-Bankruptcy-Prediction/blob/main/12.JPG)

## Model Deployment
Voting Ensemble model is giving better precision than the logistic regression model tuned with Hyperdrive.The following steps have been performed to deploy the model and interact with it:
* Saving the best run model.
* Writing the scoring script.
* Creating an ACI deployment configuration with key-based authentication enabled.
* Configuring InferenceConfig using the environment & the scoring script created as an entry script.
* Deploying the model to an ACI webservice. The deployed model from Endpoints tab
![Image of Yaktocat](https://github.com/agshiv92/Company-Bankruptcy-Prediction/blob/main/15.JPG)
![Image of Yaktocat](https://github.com/agshiv92/Company-Bankruptcy-Prediction/blob/main/16.JPG)

In order to get the prediction from the deployed model, we are sending the data in json format. We are also using REST end point and primary key to get the prediction
![Image of Yaktocat](https://github.com/agshiv92/Company-Bankruptcy-Prediction/blob/main/17.JPG)
![Image of Yaktocat](https://github.com/agshiv92/Company-Bankruptcy-Prediction/blob/main/18.JPG)

## Screen Recording
[Screencast](https://youtu.be/Xnfkm2BUVZ0 "Screencast")
## Standout Suggestions

