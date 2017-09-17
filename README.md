# CSV URL checker

Reads URLs from CSV column with header "URL", gets HTTP status code and writes status to new column in CSV.

This was initially written for a migration/cataloging cleanup project in which digital object URLs were being updated in catalog records-- verifying that the new URLs are working and identifying any issues before moving forward with updating them in the catalog. 

## Dependencies
*Python 2.7
*pandas
