# Machine Learning Data separation into training & test data
# for ML algo evaluation:
#
#     1) Train & Test Sets Split (Randomly 33% of data is selected)

#     2) k-fold Cross validation (divide the data into k folds, we hide 1 part and use rest k-1 folds as training data.
#                                   do this recursively, that is k times accuracy is calculated, in the end we will have
#                                   an array of k size array of accuracies. Every row gets a chance to become training
#                                   as well as testing data. Its most reliable and widely used technique. If i/p is big data
#                                   result is printed very late. k times more time will be taken.)

#     3) leave one out cross validation (special version of k-fold. except one row use the entire rem data as training
#                                           and test this for that row, repeat this for every row. It's all the more slow
#                                           but reliable)

#     4) Repeated random train test split (repeat the train test model. It may select the previously selected or
#                                              a row may never be selected. Ans will fluctuate)

# this is used to Divide the data into training and test data
