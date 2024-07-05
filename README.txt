Pulled Data from NYC OpenData-Motor Vehicle Collisions - Crashes

https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95/about_data

Rows: 2.1M
Columns: 29
Each row is a: Motor Vehicle Collision


COLUMNS: CRASH DATE,CRASH TIME,BOROUGH,ZIP CODE,LATITUDE,LONGITUDE,LOCATION,ON STREET NAME,CROSS STREET NAME,OFF STREET NAME,NUMBER OF PERSONS INJURED,NUMBER OF PERSONS KILLED,NUMBER OF PEDESTRIANS INJURED,NUMBER OF PEDESTRIANS KILLED,NUMBER OF CYCLIST INJURED,NUMBER OF CYCLIST KILLED,NUMBER OF MOTORIST INJURED,NUMBER OF MOTORIST KILLED,CONTRIBUTING FACTOR VEHICLE 1,CONTRIBUTING FACTOR VEHICLE 2,CONTRIBUTING FACTOR VEHICLE 3,CONTRIBUTING FACTOR VEHICLE 4,CONTRIBUTING FACTOR VEHICLE 5,COLLISION_ID,VEHICLE TYPE CODE 1,VEHICLE TYPE CODE 2,VEHICLE TYPE CODE 3,VEHICLE TYPE CODE 4,VEHICLE TYPE CODE 5

Data Dictionary: https://data.cityofnewyork.us/api/views/h9gi-nx95/files/bd7ab0b2-d48c-48c4-a0a5-590d31a3e120?download=true&filename=MVCollisionsDataDictionary_20190813_ERD.xlsx

Cleaning Process: Used Python
Read CSV File-> Dropped columns 'ZIP CODE', 'LOCATION', 'CROSS STREET NAME',and 'OFF STREET NAME'->
Dropped Rows where field is empty in either columns 'BOROUGH', 'ON STREET NAME', or 'CONTRIBUTING FACTOR VEHICLE 1' ->
Remove rows where LATITUDE and LONGITUDE are 0 or empty ->
Renamed fields to consolidate Contributing Factors -> Extract the year from the date column and create a new column [NOT REQUIRED FOR TABLEAU]->

Saved cleaned file as 'CleanedMotorVehicleCollisions.csv'

Post Cleaning
Number of rows in the cleaned DataFrame:  1089578

Download CLEANING.py and run

Dashboard saved on Tableau Public:
https://public.tableau.com/app/profile/nelson.wong2558/viz/NYCMotorVehicleCollisions_17199821731750/Dashboard1?publish=yes