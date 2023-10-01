# Exploring Metropolitan Statistical Areas and Employment
## Data and Programming for Public Policy II - Python

## 1. Downloading data
The first challenge researchers often face is the availability of desired data; it might exist but at the wrong frequency or level of geographic analysis, it might not cover desired time spans or geographies, or it might not exist at all. This can be surprisingly common, and it is dangerous to begin work on a project under the assumption data will be available.

Once you establish that your data exists, the second issue becomes retrieving it, some of which was covered last quarter when we went over automated data retrieval and web scraping. The first step in this assignment is to interface through your web browser with two sites to retrieve US data at the county and MSA (Metropolitan Statistical Area) level. Note that sites like these can be great sources of data for your final project, so take a minute to browse the data available for inspiration. For full credit you should follow these steps exactly.

To begin, go to the following Bureau of Economic Analysis (BEA) website: https://www.bea.gov/itable/regional-gdp-and-personal-income. Click on:
  * "Interactive Data Tables" (orange bar)
  * "Personal income and employment by county and metropolitan area"
  * "CAEMP25 Total full-time and part-time employment by industry"
  * Select by NAICS code
  * Select "County"
  * Select "All counties in the U.S."
  * In the "Statistic" window, select "Total employment (number of jobs)", "Manufacturing", and "Military" (hold ctrl to select multiple items)
  * Select the years 2005, 2006, and 2007
  * Click "Download" and select "CSV". The resulting file will be named Table.csv
 
Second, go to this Bureau of Labor and Statistics (BLS) website: https://www.bls.gov/lau/metrossa.htm. At the bottom under "Downloadable Data Files" select the ZIP version of Table 1. The extracted file is named ssamatab.xlsx by default (you can extract it manually, though it is not hard to do with Python).

And finally, go to the Missouri Census Data Center Geographic Correspondence Engine (MABLE Geocorr) at: https://mcdc.missouri.edu/applications/geocorr2018.html. 
  * In the top window select all US states by holding shift and clicking at the bottom
  * In the left window select "County"
  * In the right window select "Core Based Statistical Area (CBSA)"
  * Leave all other selections at their defaults and click "Run request"
  * Save the CSV document generated at the bottom of the next page, that begins with "geocorr2018_"
  
## 2. Preparing the county-level BEA data
The file Table.csv shows annual county employment levels for three years, split by total jobs, manufacturing jobs, and military jobs. Explore the file, then load it in as a dataframe, cleaning it up and reshaping it to long (tidy) format. Recall that in this format, each row should be uniquely identified by a place and a time. The end result should have five columns (county, year, manufacturing, military, total) and 9,354 rows.

## 3. Preparing the MSA-level BLS data
The file ssamatab.xlsx has the monthly statistics on the levels of the labor force, employment, and unemployment, along with the unemployment rate, for all MSAs in the US, from 1990 to 2023. As before, explore the file, then load it in as a dataframe and perform any necessary cleaning. The final result should have only four columns (area, year, month, unemployment rate), and 159,588 rows.

## 4. Preparing the county-MSA crosswalk
Our goal is to connect the unemployment rate data from the BLS file to the industry-level data from the BEA file, but we have a (fairly common) problem: these datasets are currently mis-matched by the level of geographic resolution. We cannot directly merge counties into MSAs with our current tools! The solution is called a "crosswalk" - a third dataset that does nothing but connect the matching key in each of the other datasets. Fortunately, MSAs are made up of entire counties, so we can easily find the connecting data we need using MABLE Geocorr. Load the crosswalk (the file named begginning with geocorr2018_) into a third dataframe, dropping all counties that aren't part of an MSA (denoted by 99999 in the cbsaname10 column). The final dataframe should have only two columns (the counties and the MSAs) and 1,788 rows.

## 5. Merging
Using these three dataframes, combine them into one long "tidy" dataframe where each row is unique by MSA-year. Attempting this will highlight another mismatch - the BEA data is annual and the BLS data is monthly. There are many ways to "solve" this, or it may even be desired (for example, the annual value could be used as a fixed effect in a monthly frequency pannel), but for now simply aggregate the montly data to annual using the mean value in a given place. When you aggregate from county to MSA level, you should use the sum (because those values are in levels, not rates). Make sure you explore your merges - normally you would need to work on fixing any unmatched areas. It is common for any larger string merges to not match up quite right (for an example, look at the Boston MSA). For this assignment, at least show that you know how to investgiate those, but you are not required to fix them. Keep only rows with complete data.

## 6. Basic exploration
We will continue to use this data in the next assignment, so we will have more opportunities to go deeper into it.  For now:
  * Divide each MSA up into one of four quartiles based on the military share of total employment in 2005
  * Answer the question, "Did MSAs with a higher proportion of military employment in 2005 see a greater or lesser change in the unemployment rate compared to MSAs with a lower proportion of military employment?" 
	* Specifically, what is the mean change in the unemployment rate between 2005 and 2006 for each quartile?  Your answer should be printing a Pandas Series that shows the four quartiles, next to the four mean unemployment rate changes.
  * Repeat that question for the manufacturing share of total employment in 2005.
  
Remember everything we've talked about regarding writing good code, using functions, and generalizing where possible.  To read more about what an MSA is, see [this link](https://www.census.gov/programs-surveys/metro-micro/about.html) to the US Census Bureau.  Aside from this readme file, your final repo that you submit on Gradescope should contain:
  * One file named homework1.py with your code.  Please use this exact name as it makes our internal processing easier.  Also include your name as it appears on Canvas in a comment at the top.
  * The three datasets you download: Table.csv, ssamatab.xlsx, and geocorr2018_xxxx.csv
