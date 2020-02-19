# LT2212 V20 Assignment 1

### Part 1
I decided to split the text into words just by spaces. I didn't lemmatize them, since we are not allowed to use nltk for this assignment, and any manual approaches to this seem excessively laborious and not very promising. However, I excluded all punctuation and all numbers, in order to get only actual words. This is not perfect, for example I get a high number of "s", probably from contractions with removed apostrophes, but it still yields more useful results than leaving those in the data. 
My function assumes that the first two arguments are the full paths to the directories, in case they are not already in the same directory.

### Part 4
In the plot before tf-idf, the top words were mostly content-free (except for #9, oil) and relatively evenly distributed between the two classes. Crude generally has higher numbers, which might be because it's the bigger corpus of the two. After tf-idf the plot changes drastically. While a few of the function words from the last plot still appear (e.g. "the"), there are also content words which appear almost exclusively in one of the classes. For example, "tonnes", "mil", and "wheat" appear overwhelmingly frequently in the grain class, while "oil" and "opec" appear mostly in the crude class. I was a bit surprised to see that some of the function words did not get eliminated, but it seems that e.g. "the", "in", or "that" are so frequent, that they still have a high count after the tf-idf normalization. 

### Part Bonus
I chose to create a classifier using SVM, since they are known to work well with high-dimensional data such as language. For the purpose of this assignment it seemed the easiest to write a function that takes a dataframe as input and then trains and evaluates the model. It returns the accuracy score (as asked for in the assignment) and additionally prints precision, recall, and a confusion matrix, to get more detailed information about the performance. 
Comparing the results with and without tf-idf, the model without performs very slightly worse than the model with tf-idf. However, the difference is minimal since the basic model already has a very high performance, so there is not a lot of room for improvement. This result confirms my expectation that the model works better with tf-idf, as this should take less general (function) and more class-specific (content) words into regard. I did expect a bigger difference though. 

