# Movie Recommendation System using Apriori Algorithm

This project is a movie recommendation system developed in Python, utilizing the Apriori algorithm to generate association rules for recommending movies based on user preferences.

## Project Description

The recommendation system takes movie rating data and applies the Apriori algorithm to find frequent itemsets and generate association rules. These rules help in recommending movies to users based on the movies they've watched. The project was created as an assignment to practice data preprocessing, matrix manipulation, and association rule mining.

## Features

- **Data Preprocessing**: Filters the dataset to include only the top movies for specific genres.
- **User-Movie Matrix**: Generates a matrix indicating movies watched (True) or not watched (False) by each user.
- **Frequent Itemsets**: Uses the FP-Growth or Apriori algorithm to identify frequent combinations of movies watched by users.
- **Association Rules**: Extracts rules that suggest which movies are likely to be watched together, based on the frequent itemsets.

## Usage
- **Data Preprocessing**: First, preprocess the data to filter and select popular movies.
- **Matrix Construction**: Run matrix.py to construct the user-movie matrix.
- **Frequent Itemset Mining**: Execute apriori.py to identify frequent movie combinations.
- **Generate Rules**: Use main.py to combine all components, extract association rules, and output recommendations.

## Requirements

- Python 3.x
- Required libraries 
  - pandas
  - mlxtend (for the Apriori and FP-Growth algorithms)
  - numpy
 
 ## Results
The resulting association rules suggest movie pairs or sets that users often watch together, forming the basis for recommendations.
Rules are evaluated by support (frequency of itemsets in data), 
confidence (likelihood of watching a movie given that another is watched), and lift (strength of association).

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/melikYalcinkaya/Movie_Suggestions

 ## Contributing
Feel free to fork the project and submit pull requests if you would like to contribute. 
Any contributions that improve functionality, efficiency, or readability are welcome!

