## Omidyar Extractive Industry Fiscal Governance
### Project 1: Contract Anomaly Detection and Metadata Enhancement
### Project Summary:
 
#### Organizations like the Natural Resource Governance Institute must read 100+ page legal contracts in full in order to find any clauses which may be unfair. This is a time-consuming manual process. Additionally, the term unfair is highly subjective and many are hesitant to use the term in public, however, having a measurement of non-standard is very helpful.  
 
#### We want to use extractive industry contracts to build an anomaly detection model which alerts when an incoming contract is different from a standard contract so that the organizations who are reviewing contracts for governance purposes can prioritize their work by weeding out standard contracts and/or standard contract sections.

Process:

    1. Ingest corpus of contracts
    2. Label with language, country and contract type (mineral, oil, natural gas)
    3. Have SMEs label any contracts they know are anomalous or unfair as a hold-out set for testing
    4. Build model (potentially Isolation Forest or fine-tune a distance metric)
    5. Test against known anomalies
    6. Enrich contract metadata
        a. Topic modeling
        b. Subject tags
        c. Named entities
        d. User log data time series, locations
        e. Boolean search terms (confidentiality, exemption)
        f. Contract tone (Bloomberg research on harshness)
        g. Contracts with redactions - From Rob Pitman: “It would be great to put together a definitive list of all the contracts in resourcecontracts.org that have redactions and analyse what terms companies (or their law firms) plan to keep out of the public realm.”
