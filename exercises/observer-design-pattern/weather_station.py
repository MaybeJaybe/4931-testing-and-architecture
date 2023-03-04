"""
Final Implementation of WeatherData.  Complete all the TODOs
"""

class Subject:
    # Both of the following two methods take an
    # observer as an argument; that is, the observer
    # to be registered or removed.
    def registerObserver(observer):
        pass
    def removeObserver(observer):
        pass

    # This method is called to notify all observers
    # when the Subject's state (measurements) has changed.
    def notifyObservers():
        pass

# The observer class is implemented by all observers,
# so they all have to implemented the update() method. Here
# we're following Mary and Sue's lead and
# passing the measurements to the observers.
class Observer:
    def update(self, temp, humidity, pressure):
        pass

# WeatherData now implements the subject interface.
class WeatherData(Subject):

    def __init__(self):
        self.observers = []
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0


    def registerObserver(self, observer):
        # When an observer registers, we just
        # add it to the end of the list.
        self.observers.append(observer)

    def removeObserver(self, observer):
        # When an observer wants to un-register,
        # we just take it off the list.
        self.observers.remove(observer)

    def notifyObservers(self):
        # We notify the observers when we get updated measurements
        # from the Weather Station.
        for ob in self.observers:
            ob.update(self.temperature, self.humidity, self.pressure)

    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure

        self.measurementsChanged()

    # other WeatherData methods here.

class CurrentConditionsDisplay(Observer):

    def __init__(self, weatherData):
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

        self.weatherData = weatherData # save the ref in an attribute.
        weatherData.registerObserver(self) # register the observer
                                           # so it gets data updates.
    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        print("Current Conditions:")
        # this looks awful i'm fixing it you can't stop me its already done
        print(f"{self.temperature} degrees F, with {self.humidity}% humidity and an air pressure of {self.pressure}.")

# TODO: implement StatisticsDisplay class and ForecastDisplay class.

# TODO: Create two objects from StatisticsDisplay class and
    # ForecastDisplay class. Also register them to the concerete instance
    # of the Subject class so the they get the measurements' updates. -?

class StatisticsDisplay(Observer):
    # The StatisticsDisplay class should keep track of the min/average/max
    # measurements and display them. (self, temperature, humidity, pressure)
    def __init__(self, weatherData):
        self.temp_stats = []
        self.humid_stats = []
        self.pressure_stats = []
        self.weatherData = weatherData

        weatherData.registerObserver(self)

    def update(self, temperature, humidity, pressure):
        self.temp_stats.append(temperature)
        self.humid_stats.append(humidity)
        self.pressure_stats.append(pressure)

        self.display()

    def display(self):
        print("\nMinimum Temperature:", min(self.temp_stats))
        print("Average Temperature:", sum(self.temp_stats)/len(self.temp_stats))
        print("Maximum Temperature:", max(self.temp_stats))

        print("\nMinimum Humidity:", min(self.temp_stats))
        print("Average Humidity:", sum(self.temp_stats)/len(self.temp_stats))
        print("Maximum Humidity:", max(self.temp_stats))

        print("\nMinimum Pressure:", min(self.temp_stats))
        print("Average Pressure:", sum(self.temp_stats)/len(self.temp_stats))
        print("Maximum Pressure:", max(self.temp_stats))


class ForecastDisplay():
    # The ForecastDisplay class shows the weather forcast based on the current
    # temperature, humidity and pressure. Use the following formulas :
    # forecast_temp = temperature + 0.11 * humidity + 0.2 * pressure
    # is forecast_temp correct? it makes a super long number. oh well
    # forecast_humidity = humidity - 0.9 * humidity
    # forecast_pressure = pressure + 0.1 * temperature - 0.21 * pressure
    
    def __init__(self, weatherData):
        self.forecast_temp = 0
        self.forecast_humidity = 0
        self.forecast_pressure = 0
        self.weatherData = weatherData

        weatherData.registerObserver(self)

    def update(self, temperature, humidity, pressure):
        self.forecast_temp = temperature + 0.11 * humidity + 0.2 * pressure
        self.forecast_humidity = humidity - 0.9 * humidity
        self.forecast_pressure = pressure + 0.1 * temperature - 0.21 * pressure
        
        self.display()

    def display(self):
        print("Current Forecast:")
        print(f"{self.forecast_temp} degrees F, with {self.forecast_humidity}% humidity and an air pressure of {self.forecast_pressure}.")


class WeatherStation:
    def main(self):
        weather_data = WeatherData()
        current_display = CurrentConditionsDisplay(weather_data)
        statistics_display = StatisticsDisplay(weather_data)
        forecast_display = ForecastDisplay(weather_data)

        weather_data.setMeasurements(80, 65,30.4)
        weather_data.setMeasurements(82, 70,29.2)
        weather_data.setMeasurements(78, 90,29.2)

        # un-register the observer
        weather_data.removeObserver(current_display)
        weather_data.setMeasurements(120, 100,1000)


if __name__ == "__main__":
    w = WeatherStation()
    w.main()
