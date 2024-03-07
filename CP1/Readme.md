# IT492_RecSys
This is the official repository for Team:T7 Gnosis for the submission of Course Projects in Recommender Systems(IT492))

## Team Members:
## 202311021 - Bhavan Bhatt
## 202311022 - Pratham Patel
## 202311026 - Nishit Munjani
## 202311069 - Viraj Prajapati

The dataset has 14.5k rows and the images given in the dataset are a bit less but however sufficient enough. Firstly we have done exploratory data analysis of different features. With the help of libraries such as matplotlib we have plotted various graphs. After doing this we decided that Multimodal Recommender System will be appropriate for this problem statement but just to be sure we have used text text-based model as well. In the multimodal system for image-based features we have gone with 2 models VGG-16 and DenseNet121. In these 2 models for text based features we have used TFIDF and Label encoding respectively. 

As this was a fashion dataset we have user ratings but we decided to not do user profiling as no other data was given. That is the main reason we were limited to item's features. Also as we are unaware about the the ground truth we have not included evaluation measures in this project. Choosing the ground truth by ourselves can lead to biased results as well and there was are chances of the ground truth to be subjective. For the above mentioned reasons the scope of this project on this dataset is limited to generating recommendations.

However when comparing the final results almost top 5 results were similar in text based as well as Multimodal Systems after 5th recommendation there are some variance some models we also see some novelty which may or may not be close to the ground truth.
