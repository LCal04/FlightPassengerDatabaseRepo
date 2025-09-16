# FlightPassengerDatabaseRepo

This project generates an Excel based database for analysing "Flight Passenger Traffic" across American airports. It includes information about airports, airlines, flight routes, passenger volumes, seat occupancy rates, and weekly flight frequency. It's purporse is to serve data analysis and dashboard creation (in PowerBI) with a focus on aviation & transportation patterns.

---

# Project Structure

This dataser includes five main tables, wach with 50 rows of randomly generated data:

|     Table Name     |                 Description                             |
|--------------------|---------------------------------------------------------|
| *Airports*         | Airport codes, names, cities and country                |
| *Airlines*         | Airline codes and names                                 |
| *Routes*           | Flight routes with origin and destination airport codes |
| *PassengerTraffic* | Monthly arrival/departure passenger counts per airport, |
|                    | average seat load factor %                              |
| *WeeklyFlights*    | Weekly flight frequency per route and airline           |

Tables are saved inside an Excel workbook:
'FlightPassengerDatabase_50Rows.xlsx'

---

# Technology/libraries Used:
- Python 3
- Pycharm
- PowerBI
- Excel
- 'pandas'
- 'faker'
- 'xlsxwriter'

---

# Use Cases

- Building a PowerBI dashboard and report
- Performing data analysis and visualisation
- Creating a portfolio project in transportation/aviation analytics
- Simulating trends and metrics for airports and airlines

--- 

# How to run the code

*1) Clone the Repository
'''bash
git clone https://github.com/LCal04/FlightPassengerDatabaseRepo/blob/main/sjsi.py
cd flight-traffic-database

*2) Install Dependencies
pip install pandas faker xlsxwriter

*3) Run the Script
python sjsi.py

*4) Output (Script produce)
'FlightPassengerDatabase_50Rows.xlsx'
Created inside the same folder as 'sjsi.py'

# Sample Preview
PassengerTraffic Table (example):
| AirportCode | Year | Month | PassengersArriving | PassengersDeparting | AvgSeatLoadFactor (%) |
-------------------------------------------------------------------------------------------------
|    JFK      | 2025 |   1   |      1,230,000     |      1,210,000      |          82.5         |
|    LAX      | 2025 |   3   |      1,800,000     |      1,750,000      |          84.2         |

# Notes
- All data in the tables are RANDOMLY GENERATED
- Data is intended for educational and portfolio purposes ONLY
- Dataset can be expanded by increasing rows, year range, or adding additional attributes such as delay data or   aircraft types, etc.

# License
This project is open-source and available to access under the MIT License.

  
