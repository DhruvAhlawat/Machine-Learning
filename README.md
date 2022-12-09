# Machine-Learning
A collection of my machine learning implementations


# How to use the library MyRegressionModel
Currently 2 modes of logistic regression are implemented, normalized and unnormalized.
Normalized just converts each feature to a comparable range by subtracting mean and dividing by standard deviation for each feature.
to use the normalized version, set the variable Normalized to True so future testcases also get modified correctly.

To start the training process, create an object of the class and then call the function Unnormalized or Normalized RegressionTrain, and pass the parameters as given.
alpha corresponds to the training step during gradient descent, and regularization Factor is the factor used for regularizing the terms to prevent overfitting.

to predict using the model, use the predict function.

an example usage is provided for the kaggle's titanic competition dataset
