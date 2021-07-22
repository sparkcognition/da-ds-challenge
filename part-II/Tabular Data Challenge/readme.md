# DeepArmor Data Science Coding Challenge

## Part II - Tabular Data Challenge

Our client, a local football team, is developing their offensive and defensive strategies
for the coming season. They would like to use "AI" to help determine when "going for it" on 4th down makes
sense, and to determine when their opponent is likely to attempt a 4th-down conversion so they can make
the appropriate real-time substitutions. To keep their opponents off balance, they'd like to change the
previous year's strategy for deciding these things, and they're assuming their opponents will do the same.

We have play-by-play data from last year's database (train.csv) and some test data (test.csv). The team's 
analytics staff has taken care of all the work that requires domain knowledge. They have evaluated each 
play/situation record and for each one that may be a candidate for a fourth-down conversion they have 
set the "is_candidate" value for the record to 'True'. 

Design a model that can be used to predict whether a situation is a good 4th down conversion
candidate or not. The model's inference time should be reliably short since it will be used in real time.

Provide the following:
   1. The source code you used to build the model. You can use any language you like
   2. A csv containing the predictions of the test data
   3. A description of your model and an explanation why you chose this model over other models
   4. An explanation of how you handled unbalanced data
   5. An explanation of how you considered the inference time for the model
