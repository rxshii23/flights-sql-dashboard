import mysql.connector


class DB:
    def __init__(self):
        # connect to the database
        try:
            self.conn = mysql.connector.connect(
                host='127.0.0.1',
                user='root',
                password='iRishi@23',
                auth_plugin='mysql_native_password',
                database='indigo'
            )
            self.mycursor = self.conn.cursor()
            print("connection successful")
        except:
            print('connection error')

    def fetch_city_names(self):

        city = []
        self.mycursor.execute("""
            SELECT DISTINCT(Destination) FROM flights.flightx UNION
            SELECT DISTINCT(Source) FROM flights.flightx 
            """)
        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])

        return city

    def fetch_all_flights(self, source, dest):
        self.mycursor.execute("""
            SELECT Airline,Route,Dep_Time,Duration,Price FROM flights.flightx
            WHERE Source = '{}' AND Destination = '{}'
        """.format(source, dest))

        data = self.mycursor.fetchall()
        return data

    def fetch_airline_freq(self):

        airline = []
        freq = []
        self.mycursor.execute("""
        SELECT Airline, COUNT(*) FROM flights.flightx
group by Airline 
        """)

        data = self.mycursor.fetchall()

        for item in data:
            airline.append(item[0])
            freq.append(item[1])

        return airline, freq

    def busy_airport(self):
        self.mycursor.execute("""
            SELECT Source, COUNT(*) FROM (SELECT Source FROM flights.flightx UNION ALL
                SELECT Destination FROM flights.flightx) t
            GROUP BY t.Source
            ORDER BY COUNT(*) DESC
        """)

        city = []
        freq = []
        data = self.mycursor.fetchall()

        for item in data:
            city.append(item[0])
            freq.append(item[1])

        return city, freq

    def flights_per_day(self):

        self.mycursor.execute("""
            SELECT Date_of_journey,COUNT(*) FROM flights.flightx
            GROUP BY Date_of_journey
            ORDER BY COUNT(*) DESC
        """)
        data = self.mycursor.fetchall()
        date = []
        freq = []
        for item in data:
            date.append(item[0])
            freq.append(item[1])

        return date, freq
