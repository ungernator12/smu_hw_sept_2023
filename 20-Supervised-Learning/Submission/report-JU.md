# Module 12 Report Template

## Overview of the Analysis

In this section, describe the analysis you completed for the machine learning models used in this Challenge. This might include:

* Explain the purpose of the analysis.
* Explain what financial information the data was on, and what you needed to predict.
* Provide basic information about the variables you were trying to predict (e.g., `value_counts`).
* Describe the stages of the machine learning process you went through as part of this analysis.
* Briefly touch on any methods you used (e.g., `LogisticRegression`, or any resampling method).

This analysis is being performed to determine credit worthiness of borrowers for a peer-to peer lending service. This data covers the credit history of potential borrowers, including their loan size, interest rate, income, debt/income ratio, number of accounts held, and total debt. This dataset exhibits a roughly 97% successful loan payoff rate. Methods of analysis include: logistic regression, svc, knn, decision tree, random forest, ADABOOST, and GradientBoost.

## Results

Using bulleted lists, describe the balanced accuracy scores and the precision and recall scores of all machine learning models.

* Machine Learning Model 1:
  * Description of Model 1 Accuracy, Precision, and Recall scores.
* no signs of overfitting
* false psitive slightly high (15%)
* false negative also high (9%)

* could maybe do better, lots of red flags
* violate assumptions of linear models- need PCA/Scaler


* Machine Learning Model 2:
  * Description of Model 2 Accuracy, Precision, and Recall scores.
* no overfitting
* LOVE the reduction in false negatives
* but did increase false positive

* Machine Learning Model 3:
  * Description of Model 2 Accuracy, Precision, and Recall scores.
* no overfitting
* ALSO reduces false negatives
* but does have a chunk of false positives
* Easier to explain, and less computationally heavy vs the SVC, so this is now my model to beat

* Machine Learning Model 4:
  * Description of Model 2 Accuracy, Precision, and Recall scores.
* There's signs of overfitting
* all metrics are worse than KNN :(

* Machine Learning Model 5:
  * Description of Model 2 Accuracy, Precision, and Recall scores.
* A bit of overfitting (we're better on the train than the test)
* Recall is WORSE than the KNN

* Machine Learning Model 6:
  * Description of Model 2 Accuracy, Precision, and Recall scores.
* no signs of overfitting
* about the same performance as ADA

## Summary

Summarize the results of the machine learning models, and include a recommendation on the model to use, if any. For example:
* Which one seems to perform best? How do you know it performs best?
* Does performance depend on the problem we are trying to solve? (For example, is it more important to predict the `1`'s, or predict the `0`'s? )

If you do not recommend any of the models, please justify your reasoning.

* So in summary, either AdaBoost, GradientBoost, or Knn is good

* Knn is most explainable
* Ada/Gradient is probably the most adaptable 
