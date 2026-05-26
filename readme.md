# AFTER EXPERIMENT - CONCLUSIONS
1) It is impossible to teach model to solve x^2 + y^2 with x and y out of training range directly by training it on many random x and y values.
   1.1) Instead, it should be taught the structure of exponentiation as an operation that applies universally to all numbers.
###   1.2) How to teach a model broader rule without hardcoding the structure of the rule or the rule itself?
2) If for x^2 + y^2 the broader domain is (anynumber)^2 and for (anynumber)^2 the broader domain is exponentiation in general, how far can we go with "broader" and do we end up with one or very few global domains that include every rule of how the world works?
   2.1) Can we teach a model to come up with looking for broader domain on it's own when its needed just like humans do?
     2.1.1) Can we loop the process so the model finds the "list of global domains and rules" (assuming it exists)
3) Learning rate should be adjusted according to amount of epochs, dataset size and it's range (e.g. If the dataset is large and the variety of data is small then smaller learning rate is better for big amount of epochs)
# BEFORE EXPERIMENT
## Problem:
AI models with too many parameters for the training data/pattern are being trained memorize all solutions instead of learning a hidden rule which makes them extremely weak on examples they have not seen yet.

## Rules
Model will be trained on rules of simple yet non linear mathematical operation (x^2 + y^2) to guess the solution.
Human will experiment with different learning rates, datasets and other variables in order to make model capable of solving operations that contain values far from the training range
