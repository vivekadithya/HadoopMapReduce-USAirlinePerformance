# HadoopMapReduce-USAirlinePerformance
A Hadoop Map Reduce application to report maximum departure delay for each originating airport, average arrival delay by flight number and minimum arrival delay for all origin-destination airport combinations.

Data: 
Visit http://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=236&DB_Short_Name=On-Time and download data selecting the following fields (Flight Date, Airline ID, Flight#, Origin Airport, Destination Airport, Departure Time, Departure Delay in Minutes, Arrival time, Arrival Delay in Minutes, Amount of Time in the Air, Distance in miles). 

A sample record is shown below:
2014-04-01, 19805, 1, JFK, LAX, 0854, -6.00, 1217, 2.00, 355.00, 2475.00

Enviroinment Used For Execution: Cloudera Hadoop Distribution on Virtual Machine

Execution:
Individual mappers and reducers were developed for each task. The	intermediate data from the mapper was sorted and sent as input to the reducer.

