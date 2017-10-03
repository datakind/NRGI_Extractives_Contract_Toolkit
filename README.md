![alt text](https://pbs.twimg.com/profile_images/458395751433789440/tB_OOPH7_400x400.png)
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

### 2. OCR Contracts Backlog

 - From a directory of PDFs, performs OCR
 - Outputs results of OCR to txt files in same directory

### 3. Clean Text

 - Reads in contract text
 - Strips HTML from text
 - Cleans text for NLP prep (remove unicode, special characters, stopwords, etc.)
 - Outputs cleaned text appended to original dataframe

### 4. Contract EDA

 - Reads in contract text and original metadata from Notebook 2
 - Computes basic stats on text and original metadata
 - Does topic modeling on text
 - Creates explanatory charts and graphs

### 5. Metadata Creation


- Reads in contract text and original metadata dataframe
 - Computes various metadata fields including 
 	- Auto-generated original metadata fields
 	- Subject tags
 	- Named entities
 	- Presence of boolean search terms (confidentiality, exemption, stabilization clause, redactions)
 	- Basic stats on text
  - Outputs results appended to original dataframe
 
 ### 6a. Annoation Tag Classifier Grid Search
  
  - Performs grid search for binary classification of Stabilization and Royalties clauses

### 6b. Annotation Tag Classifer

 - Performs Binary classification of contract clause types

### 6c. Annotation Tag Multiclass Classifier 

 - Performs Multiclass Classifier for contract clause types

### 7. Rolling Hash Function

  - Hash-based partitition function for segmenting documents prior to clustering

 ### 8. Anomaly Detection

  - Reads in contract text and metadata dataframe
  - Runs anomaly detection and alerts on:
  	- Anomalous / non-standard contract sections
  	- Missing standard sections which should be present
  - Output results appended to original dataframe
