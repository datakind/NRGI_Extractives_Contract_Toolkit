![alt text](NRGI_logo.jpg)
# Omidyar Extractive Industry Fiscal Governance
## Project 1: Contract Anomaly Detection and Metadata Enhancement
### Project Summary
 
#### Those working on extractive industry governance aim to help local communities benefit from their countries’ endowments of oil, gas and minerals. One of the ways they do this is by assessing 100+ page extractives industry legal contracts for things like fiscal governance and environmental reparations, but this is a time-consuming, manual and subjective process, usually performed by legal experts. Automatic generation of metadata and annotations would allow those reviewing the contracts (including those without legal training) to quickly find relevant contracts and clauses within those contracts in order to focus on what is different about one contract compared to a standard contract and make their assessment based on a higher-level analysis of metadata as opposed to an extensive word-for-word comparative review.
 
#### We will leverage publicly available extractive industry contracts to extract data using natural language processing techniques and then train a suite of machine learning models to assist legal reviewers, journalists, regulators and community activists.

### Notebook Summary

### 1a. Extract Contracts

 - Extracts contract text using urls to pdf documents contained in contract metadata file downloaded from http://www.resourcecontracts.org/contracts
 - Appends contract text to original contract metadata file and pickles dataframe for analysis

### 1b. Extract Contract Backlog

 - From scraped text from Colombian oil contract website, found pdf links and output list of links to pdf files
 - Takes the list of pdf links and downloads files to directory

### 1c. Extract Contract Annotations 

 - Downloads annotation excel files

### 2. OCR Contract Backlog

 - From a directory of PDFs, performs OCR
 - Outputs results of OCR to txt files in same directory

### 3a. Munge Contract Annotations

 - Reads in contract text
 - Strips HTML from text
 - Outputs cleaned text appended to original dataframe

### 3b. Munge and Clean Raw Contract Text

 - Reads in contract text
 - Parses by paragraph
 - Strips HTML from text
 - Outputs text by paragraph

### 4a. Multiclass Classifier Grid Search
 
 - Search for optimal parameters for our classifier and clause types
 - In this case the model was tuned for high recall so as to minimize false negatives

### 4b. Multiclass Classifier
 
 - Performs classification of selected clause types


### 5. Featurize and Predict Unannotated Corpus

 - Cleans and featurizes raw text
 - Predicts clause types based on pickled model from 4b
 - Outputs prediction results to csv file

### 6b. Annotation Tag Classifer

 - Performs Binary classification of contract clause types

### 7. Rolling Hash Function

  - Hash-based partitition function for segmenting documents prior to clustering

 ### 8. Anomaly Detection

  - Reads in contract text and metadata dataframe
  - Runs anomaly detection and alerts on:
  	- Anomalous / non-standard contract sections
  	- Missing standard sections which should be present
  - Output results appended to original dataframe
