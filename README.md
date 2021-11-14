# API for name match

Project status: Completed

Project Objective: The purpose of this project was get the similarity score between two strings (names of two people, companies, etc) and then create an API using Flask so that it is readily available for anyone who want to get understand how similary two strings are.

Method used

1. Data Cleaning
2. Calculate similarity score using FuzzyWuzzy (Package to calculate the Levenshtein distance)
3. Create an API using Flask

Technology: Python

Project Description: Given two strings, this API calculates the similarity score between these two strings. The similarity score is calculated using Levenshtein distance and is a value between 0 to 100. Two strings having a value close to 100 tells us that the string are similar where as values close to 0 tell us that the string are dissimilar.

Files:
1. match_results_api: Code to create an API to calculate the similarity score between two strings
2. test_name_match_API: Code to test the API
