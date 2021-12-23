# Step 2 Parse

## Description :
Parse the dataset and clean it 

- Remove empty fields
- Change timestamp to UTC/ISO
- Normalize the data from total FPL territory demand to average home demand


# Demand Curve Sample Data Methodology
---------------------------------------------------------
Data from FPL eia.gov tools 
FPL's service territory includes over 4.6 million customers
Sample data of 11/20/20 to 11/27/20 by hour of consumer demand
Using the real demand curves we can estimate consumer demand
by Household. In Florida, a survey (https://www.floridarealtymarketplace.com/blog/how-much-power-does-a-house-use.html:~:text=In%20Florida%2C%20the%20survey%20showed,windows%2C%20doors%2C%20and%20roofs.)
showed that the average home used 1,110 kWh (~14k kwh/yr) . 
This can be used to estimate 
(4.6M * 1110kWh/mo) / 730 = Total FPL Demand in kWh
6,000 MWh on average. The max of the data demand is 18k MWh 
with an average of 12000 MWh. By cutting the demand from the
sample data set in half we can safely assume that the 
remaining clients would be commercial and ancillary loads
with the reasoning that the average home would be 1000kWh
fields :
'Timestamp (Hour Ending)'
'Demand (MWh)'