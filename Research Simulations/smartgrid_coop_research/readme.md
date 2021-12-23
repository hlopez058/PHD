# Smart Grid Cooperative Research

## Description:
Simulate cooperative gaming strategies for prosumers inside of a Smart Grid. 

- Focus on south florida datasets
- System Model of prosumers, and consumers
- Bring in wind, or solar datasets to model prosumer output

Randomized around a mean for the 


The focus of my thesis is to analyze how pricing functions affect the coalition formation of prosumers and the benefits obtained due to coalitions. The results are studied by calculating Shapley value. The behavior of the 'g' function that is used in NRG-X-Change mechanisim is tested in the first section of chapter 5. Here , we considered four different scenarious, in each scenario, we consider 5 cases where each case is a network of 5 prosumers. As the 'g' function is the price function for paying prosumers, in each case, every peosumer is considered to have a varied production value and constant consumption. Each case has a 5 prosuers, and for each group of prosumeres we calculate the shapley value. The results obtained from different cases are compared and the case with highest shapley value gains maximum prodift. the results are plotted by comparing the total energy offered and total shapley value of all 5 prosumers in each case for every scenario. In order to test the effect of coalition, we first considered some hypothetical values for different pricing functions such as a concave , linear and convex and studed the shaple value witha nd without coalitions. We also took into account , the real-time data obtaind from Pecan Street Inc. where the houses selected had solar panels installed. For each of the selcted houses , the average production and consumption values generated during fall, spring and winter were consedered. At the end the Shapley value with and without forming coalitions wer examined during each season by considering linear and convex functions. 

from the four scenarious tested to scenarious tested to study the behavio of 'g' function , we have concluded that when the total energy poduction is less than the total energy consumption the shapley value is negative. when the production exceeds the consumption the shapley value is observed to be positive. when the total energy production exceeds more than twice that of the total consumption, the shapley value obtained is positive but negligible. hencewe conclude that the 'g' is maximized when production is twice as great as consumption.



# Prosumer Data 



## Measuring area of a Residential Roof

**These are estimations, and in general the square footage of the roof would be 10-20 percent more the square footage of the home.**

Roofing Calculator:

https://www.calculator.net/roofing-calculator.html?acarea=2000&acareaunit=feet&roofpitch=6&angle=25&eaves=1&eavesunit=feet&price=&priceunit=feet&ctype=pitch&tp=ar&x=71&y=10


Florida building code:
For roof slopes from two units vertical in 12 units horizontal (17-percent slope) up to four units vertical in 12 units horizontal (33-percent slope), double underlayment application is required in accordance with Section 1507.2.

    Accordng to Roofing calculator the lower and upper bounds in the section 1506.2 change a base area home thats 2000sqft's roof from a 2300sqft roof to a 2600 sqft roof. when dealing with a 3000sqft base area it changes from 3300 to 3800sqft.
    


What is the standard roof pitch for a house?
The most commonly used roof pitches fall in a range between 4/12 and 9/12. Pitches lower than 4/12 have a slight angle, and they are defined as low-slope roofs. Pitches of less than 2/12 are considered flat roofs, even though they may be very slightly angled.
[https://www.hunker.com/13401081/what-is-the-standard-roof-pitch#:~:text=The%20most%20commonly%20used%20roof,may%20be%20very%20slightly%20angled.]

What is the most common roof pitch?
Conventional slope roofs, with a pitch between 4/12 and 9/12, are the most common in residential work. Roofs with a pitch exceeding 9/12 (37 degrees) are termed steep slope roofs. In commercial work, low-slope roofs (with a pitch between 2/12 and 4/12) are most common.Mar 26, 2020 [https://santacruzarchitect.wordpress.com/2020/03/26/what-is-the-optimal-roof-pitch/]


## NREL PVWatts
The solar resource data takes in an address of a home and finds the nearest solar resource data site nearby. It then provides the lat/long and the distance to that solar resource. 
1. Address to Lat/Long ,get resource square 
2. System info; for solar setup
    - DC System Size (kW)
    - Module Type
    - Array Type
    - System Losses (%)
    - Tilt (deg)
    - azimuth (deg)
    - DC to AZ size ratio
    - Inverter Effciency
    - Groun Coverage Ratio
3. Solar Radiation, AC Energy , Value ; Annually

https://pvwatts.nrel.gov/pvwatts.php

Web Service:
https://developer.nrel.gov/docs/solar/pvwatts/v5/

Looks like the API is broken and can be queried with a demo
key that was in the tutorial. 
- I can use this to pull the monthly ac capacity of each home in the area, i would need the lat/long of each home.

https://developer.nrel.gov/api/pvwatts/v6.json?api_key=DEMO_KEY&lat=26.89&lon=-80.1&system_capacity=4&azimuth=180&tilt=40&array_type=1&module_type=1&losses=10

Address
- the api can take the address parameter that should convert it to a lattitiude and bring back the nearest value. That means each call can then be driven by an scraped address 

API Key Signup
Your API key for hector.lopez@nexteraenergy.com is:

Q4Iod2KFzaR9iekOzKWCL3rYyYivSB9lXMTMGmwN
You can start using this key to make web service requests. Simply pass your key in the URL when making a web request. Here's an example:

https://developer.nrel.gov/api/alt-fuel-stations/v1.json?fuel_type=E85,ELEC&state=CA&limit=2&api_key=Q4Iod2KFzaR9iekOzKWCL3rYyYivSB9lXMTMGmwN


### Zillow Addresses
Zillow has a dataabse of homes for sale, and with a map of each home . I could use this to validate residential data. Each home in an area is then refresehd on each change of the map

 Searching for jus thomes under 3k sqft in south flroida resulted in 80-100k listings. That means that the maximum amount of roof top solar would be 80-100k homes from 1200sqft to 3000 sqft according to zillow data as of 3/2021

 ### Geographic territories
The number of homes for sale in an area would result in the number of residential customers with the propencity to purchase solar , if they all purchased solar how would that impact the grid?

### Quesitons
1. Could a geographical map of solar customers be created that would provide group coverage for particular segments of the state? 
2. can the segments with coverage get funded by FPL to provide virtual power plant solar production? 
3. are there enough of these residential homes with the capacity to generate energy storage? 
4. if energy storage and solar could be installed what would be the impact to the grid and the benefit to FPL as a utility? could it replace a solar farm construction? could the money from a solar farm construction be offered to a conglomerate of prosumers to be dispatched as a regulatory asset? 
5. 