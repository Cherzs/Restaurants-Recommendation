# Machine Learning Project Report - Muhammad Zhafran Ghaly

## Project Category
The category I chose for this project is a Restaurant recommendation system in Bangalore, India on the Zomato website.

## Background
The rapid growth of technology in data collection has led to a new era of data-driven world. Data is used to create more efficient systems and that's where recommendation systems come in.

A recommendation system is a type of information filtering system as it improves the quality of search results and provides elements that are more relevant to the search items or those related to the user's search history.

This is an active information filtering system that personalizes information given to users based on their interests, information relevance, etc. Recommendation systems are widely used to recommend movies, items, restaurants, places to visit, items to buy, etc. Using content-based filtering methods that use item features to recommend other items similar to what users like, based on their previous actions or explicit feedback.

## Business Understanding
### Problem Statements
From the background description outlined above, the following problems can be formulated:
- How does the restaurant recommendation system work?
- What method is used?

### Goals

Objectives:
- Provide recommendations that use item features to recommend other items similar to what users like, based on their previous actions or explicit feedback.
- The method used is content user-based filtering which uses item features to recommend other items similar to what users like, based on their previous actions or explicit feedback.

### Solution statements
- Examine the dataset such as removing columns we don't need to use and delete them. Then eliminate items that have similar names.

## Data Understanding
The dataset used in this project is the Zomato Bangalore Dataset from [Kaggle](https://www.kaggle.com/datasets/absin7/zomato-bangalore-dataset) which has a size of 89 mb and has 17 columns and 51716 rows.
Here is information about the variables from the dataset:
- url: Restaurant address from zomato website.
- address: Restaurant address.
- name: Name of the restaurant
- online_order: Information whether restaurant can be ordered online or not
- book_table: Information whether restaurant can book tables or not
- rate: Value of restaurant given by customers
- votes: Number of customers who voted for the restaurant
- phone: Restaurant phone number
- location: location in Bangalore
- rest_type: Type of restaurant
- dish_liked: Preferred dishes
- cuisines: Types of cuisine made
- approx_cost(for two people): Estimated cost for 2 people
- reviews_list: List of reviews
- menu item: Menu Items
- listed_in(type): Type of restaurant service such as self-service or served
- listed_in(city): Location of existing restaurant branches

## Exploratory Data Analysis
Drop columns that are not used in this dataset, namely 'url', 'dish_liked', 'phone', 'address', 'rest_type', 'type', 'menu_item', 'votes'. The remaining columns after being dropped are 10 columns and 23043 rows. Then the columns used are only 'cuisines', 'Rating Value' which is changed from the 'rates' column and 'cost'. While the rows used are only 23043 out of 51716.

Then handle missing values in the dataset by deleting them using drop until none are left.
- Visualization of the most popular restaurant locations.
Restaurants with high ratings are rated by users who have visited them.

![lok](https://user-images.githubusercontent.com/76243151/195944993-893ab362-280b-4de9-9906-ed695003dcc0.png)

Figure 1. Location Visualization

In Figure 1, we can see that Koramangala 5th Block is the most popular and crowded restaurant location.

## Data Preparation
### Deleting Columns
At this stage, I deleted columns that we do not use as I did in the dataset, namely 'url', 'dish_liked', 'phone', 'address', 'rest_type', 'type', 'menu_item', and 'votes'. By dropping columns that we feel are unnecessary.
### Calculating Average Rating
Calculate the average rating using _mean_ and normalize the data using MinMaxScaler.
### Sample
In the sample data we use, it is 50% of the data using frac(0.5) which means using half of the total data.
### Handling Missing Values
At this stage, I have 37700 missing values, but by dropping the missing data, I can continue modeling without problems.
The method I use is to delete missing data using drop,

df.isnull().sum()
df.dropna(how='any', inplace=True)

## Modeling

### Content Based Filtering
Content-based filtering uses item features to recommend other items similar to what users like, based on their previous actions or explicit feedback.
### TF-IDF
Create a tf-idf matrix. There I use Cosine Similarity to detect plagiarism words from 'reviews_list'.

Create a list to place the top restaurants and then find the index of the entered restaurant. Find restaurants with the same cosine value from the large number. Extract the top 40 restaurant indices with similar cosine values. Then create a new dataset to display similar restaurants and create the top 40 similar restaurants with some of their columns. After that, drop restaurants with the same name and sort only the top 10 based on the highest ranking.

At this stage, I create a new variable to narrow down what I will display, such as 'cuisines', 'Rating Value', and 'cost'. From there, we can use the restaurant name keyword to find the top 40 restaurant recommendations that have relevant values such as ratings and costs given by users. And there I narrow it down again to only display the top 10 restaurants with the 'Rating Value' and 'cost' or cost categories.
- The advantage is that it does not require the process of forming a neighborhood.
- The disadvantage of user-based filtering is that when testing is done with error measurement using normalized mean absolute error (NMAE), the result obtained is quite high NMAE.

### Modeling Results
The results of recommendations for several restaurants similar to the restaurant 'Jalsa':

In Table 1, it recommends restaurants that have similarities like the restaurant Jalsa.

|index|cuisines|Rating Value|cost|
|---|---|---|---|
|The Black Pearl|North Indian, European, Mediterranean|4.78|1.4|
|Communiti|Continental, BBQ, Salad|4.67|1.5|
|Hammered|North Indian, Thai, Japanese, Continental, Cafe|4.65|1.3|
|The Pallet|Continental, Mediterranean, Italian, North Indian, Finger Food, Asian, Momos|4.48|1.6|
|The Globe Grub|Continental, North Indian, Asian, Italian|4.48|1.3|
|Jalsa Gold|North Indian, Mughlai, Italian|4.48|1.3|
|Brooks And Bonds Brewery|Continental, Mediterranean, North Indian, Chinese, Finger Food|4.45|1.6|
|Delhi Highway|North Indian|4.41|1.2|
|Deja Vu Resto Bar|North Indian, Italian|4.35|900.0|
|The Fisherman'S Wharf|Seafood, Goan, North Indian, Continental, Asian|4.3|1.4|

Table 1. Recommendation Results from "Jalsa"

## Evaluation
I took another sample to ensure that the recommendation system works well, namely Grand Village.

Here are the results from the Grand Village Restaurant:

In Table 2, it can be seen that the recommendations from restaurants similar to Grand Village.

|index|cuisines|Rating Value|cost|
|---|---|---|---|
|Village - The Soul Of India|North Indian, Lucknowi, Gujarati, Maharashtrian, South Indian, Bengali|3.85|1.1|
|Shanthi Sagar|South Indian, North Indian, Chinese|3.72|400.0|
|Shanthi Sagar|South Indian, North Indian, Chinese, Juices|3.72|250.0|
|Cinnamon|North Indian, Chinese, Biryani|3.71|550.0|
|Madeena Hotel|North Indian, Mughlai, Biryani|3.71|400.0|
|Red Chilliez|North Indian, South Indian, Chinese, Seafood|3.26|550.0|
|Red Chilliez|North Indian, Chinese, Seafood, Mangalorean|3.26|650.0|
|Konaseema Grand|North Indian, Mughlai, Andhra, Biryani|2.87|1.0|
|Melange - Hotel Ekaa|North Indian, Chinese, Continental, Mangalorean|2.81|900.0|
|Kabab Treat|North Indian, Chinese|2.29|500.0|

Table 2. Recommendation Results from "Grand Village"

The formula for Content-Based Filtering:

P = (# of our recommendations that are relevant) / (# of items we recommended)

For p = 1, because relevant recommendations divided by the items we recommended
which for relevant recommendations = 10, recommended items = 10.

So, 10/10 = 1

With the formula above, we can recommend very well.

References:
- Google Developers, https://developers.google.com/machine-learning/recommendation/content-based/basics#:~:text=Content%2Dbased%20filtering%20uses%20item,previous%20actions%20or%20explicit%20feedback.
- Recommendation System-Content Based, Binus University (17 Nov 2020) https://mti.binus.ac.id/2020/11/17/sistem-rekomendasi-content-based/
