from sklearn.linear_model import LogisticRegression
import argparse
import os
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from azureml.core.run import Run
from sklearn.metrics import precision_score

run = Run.get_context()

data = pd.read_csv('data.csv')

# TODO: Split data into train and test sets.

x= data.drop('Bankrupt?', axis=1)
y= data['Bankrupt?']

x_train, x_test, y_train, y_test= train_test_split(x,y, test_size= 0.2, random_state= 10)


def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--C', type=float, default=1.0, help="Inverse of regularization strength. Smaller values cause stronger regularization")
    parser.add_argument('--max_iter', type=int, default=100, help="Maximum number of iterations to converge")

    args = parser.parse_args()

    run.log("Regularization Strength:", np.float(args.C))
    run.log("Max iterations:", np.int(args.max_iter))

    model = LogisticRegression(C=args.C, max_iter=args.max_iter).fit(x_train, y_train)
    
    joblib.dump(value=model, filename= './outputs/model.joblib')

    precision = precision_score(y_test, model.predict(x_test), average='weighted')
    run.log("Precision", np.float(precision))

if __name__ == '__main__':
    main()