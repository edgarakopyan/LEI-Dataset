# LEI-Dataset
The code transforms LEI Dataset of Commercial legal entities and their relations (originally in XML format) into csv files. 

Level 1 Includes data on individual company level. Level 2 indicates relationships between companies. 

The data is taken from gleif.com and includes both Level 1 and Level 2 data and Exceptions. The file downloaded are the following (files are too big to be uploaded here but available upon request): 

1) 20201013-gleif-concatenated-file-lei2.xml

2) 20201013-gleif-concatenated-file-repex.xml

3) 20201013-gleif-concatenated-file-rr.xml

# Features 

The data includes following features: 

Level 1: LEI, Legal Name, Other Name, Legal Address First line, Legal Address Additional line, Legal Address City, Legal Address Region, Legal Address Country, Legal Address Postcode, Headquarters First line, Headquarters Additional line, Headquarters City, Headquarters Region, Headquarters Country, Other Address First line, Other Address Additional line, Other Address City, Other Address Region, Other Address Country, Other Address Postcode, Registration Status, Initial Registration Date, Registration Authority ID, Registration Authority Entity ID, Registration Authority, Legal Jurisdiction, Legal Form Code, Other Legal Form, Entity Status, Last Update, Next Renewal Date, Managing LOU, Validation Sources, Validation Authority ID. 

Level 2: Start Node ID, Start Node ID Type,	End Node ID, End Node ID Type, Relationship Type, Relationship Period, Start Date, Relationship Period End Date, Period Type, Relationship Period Start Date 2, Period type 2, Relationship Status, Relationship Qualifier Dimension, Qualifier Category, Relationship Quantifier Measurement Method, Quantifier Amount, Quantifier Units, Initial Registration Date, Last Update Date, Registration Status, Next Renewal Date, Managing LOU, Validation Sources, Validation Documents, Validation Reference. 
