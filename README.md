![alt text](https://pbs.twimg.com/profile_images/458395751433789440/tB_OOPH7_400x400.png)
# Omidyar Extractive Industry Fiscal Governance
## Project 1: Contract Anomaly Detection and Metadata Enhancement
### Project Summary
 
#### Organizations like the Natural Resource Governance Institute must read 100+ page legal contracts in full in order to find any clauses which may be unfair. This is a time-consuming manual process. Additionally, the term unfair is highly subjective and many are hesitant to use the term in public, however, having a measurement of non-standard is very helpful.  
 
#### We want to use extractive industry contracts to build an anomaly detection model which alerts when an incoming contract is different from a standard contract so that the organizations who are reviewing contracts for governance purposes can prioritize their work by weeding out standard contracts and/or standard contract sections.

### Notebook Summary

### 1. Extract Contracts

 - Extracts contract text using urls to pdf documents contained in contract metadata file downloaded from http://www.resourcecontracts.org/contracts
 - Appends contract text to original contract metadata file and pickles dataframe for analysis

### 2. Get Contracts Backlog

 - From scraped text from Colombian oil contract website, found pdf links and output list of links to pdf files
 - Takes the list of pdf links and downloads files to directory

### 3. OCR Contracts

 - From a directory of PDFs, performs OCR
 - Outputs results of OCR to txt files in same directory

### 4. Clean Contract Text

 - Reads in contract text
 - Strips HTML from text
 - Cleans text for NLP prep (remove unicode, special characters, stopwords, etc.)
 - Outputs cleaned text appended to original dataframe

### 5. Exploratory Data Analysis (Optional)

 - Reads in contract text and original metadata
 - Computes basic stats on text and original metadata
 - Does language detection
 - Does topic modeling on text
 - Creates descriptive charts and graphs

### 6. Metadata Creation

 - Reads in contract text and original metadata dataframe
 - Computes various metadata fields including 
 	- Auto-generated original metadata fields
 	- Subject tags
 	- Named entities
 	- Presence of boolean search terms (confidentiality, exemption, stabilization clause, redactions)
 	- Basic stats on text
  - Outputs results appended to original dataframe

### 7. Rolling Hash Function

  - Function to segment documents prior to clustering

 ### 8. Anomaly Detection

  - Reads in contract text and metadata dataframe
  - Runs anomaly detection and alerts on:
  	- Anomalous / non-standard contract sections
  	- Missing standard sections which should be present
  - Output results appended to original dataframe
