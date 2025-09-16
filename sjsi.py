import pandas as pd
import random
from faker import Faker

fake = Faker()

#Constants
airport_codes = ['JFK', 'LAX', 'ORD', 'ATL', 'DFW', 'DEN', 'SFO', 'SEA', 'MIA', 'PHX']
airline_codes = ['AA', 'DL', 'UA', 'SW', 'JB', 'NK', 'AS', 'F9', 'B6', 'WN']

#Create Airports table
airports = []
for code in airport_codes:
    airports.append({
        "AirportCode": code,
        "AirportName": fake.company() + "International",
        "City": fake.city(),
        "Country": "USA"
    })

while len(airports) < 50:
    code = fake.unique.lexify(text = '???').upper()
    airports.append({
        "AirportCode": code,
        "AirportName": fake.company() + "International",
        "City": fake.city(),
        "Country": "USA"
    })

#Create Airlines table
airlines = []
for code in airline_codes:
    airlines.append({
        "AirlineCode": code,
        "AirlineName": fake.company()
    })

while len(airlines) < 50:
    code = fake.unique.lexify(text = '???').upper()
    airlines.append({
        "AirlineCode": code,
        "AirlineName": fake.company()
    })

#Create Routes table
routes = []
for i in range(50):
    origin, dest = random.sample(airport_codes, 2)
    routes.append({
        "RouteID": f"R{i+1}",
        "OriginAirport" : origin,
        "DestinationAirport" : dest,
    })

#passenger traffic table
passenger_traffic = []
for i in range(50):
    airport = random.choice(airport_codes)
    passenger_traffic.append({
        "AirportCode": airport,
        "Year": 2025,
        "Month": random.randint(1, 12),
        "PassengersArriving": random.randint(50000, 15000000),
        "PassengersDeparting" : random.randint(50000, 15000000),
        "AvgSeatLoadFactor": round(random.uniform(65.0, 90.0), 1)
    })

#WeeklyFlights table
weekly_flights = []
for i in range(50):
    route_id = f"R{random.randint(1, 50)}"
    airline = random.choice(airline_codes)
    weekly_flights.append({
        "RouteID": route_id,
        "AirlineCode": airline,
        "WeekNumber": random.randint(1, 52),
        "Year": 2025,
        "NumFlights": random.randint(10, 150),
    })

#convert to dataFrame
df_airports = pd.DataFrame(airports[:50])
df_airlines = pd.DataFrame(airlines[:50])
df_routes = pd.DataFrame(routes)
df_passenger_traffic = pd.DataFrame(passenger_traffic)
df_weekly_flights = pd.DataFrame(weekly_flights)

#save to excel sheet
with pd.ExcelWriter("FlightPassengerDatabase_50Rows.xlsx", engine='xlsxwriter') as writer:
    df_airports.to_excel(writer, sheet_name='Airports', index=False)
    df_airlines.to_excel(writer, sheet_name='Airlines', index=False)
    df_routes.to_excel(writer, sheet_name='Routes', index=False)
    df_passenger_traffic.to_excel(writer, sheet_name='PassengerTraffic', index=False)
    df_weekly_flights.to_excel(writer, sheet_name='WeeklyFlights', index=False)

print("Excel file 'FlightPassengerDatabase_50Rows.xlsx' created successfully. ")