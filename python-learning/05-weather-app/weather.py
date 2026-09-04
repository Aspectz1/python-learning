import python_weather
import asyncio

city = input("What city?: ")
choice = input("What do you want to check? (Temperature, Humidity, Wind Speed, All): ")

async def get_weather():
    async with python_weather.Client() as client:
        weather = await client.get(city)

        if choice == "Temperature":
            print(f"It is {weather.temperature} Celsius")
        elif choice == "Humidity":
            print(f"The current humidity is {weather.humidity}%")
        elif choice == "Wind Speed":
            print(f"The current wind speed is {weather.wind_speed}km/h")
        elif choice == "All":
            print(f"It is {weather.temperature} Celsius")
            print(f"The current humidity is {weather.humidity}%")
            print(f"The current wind speed is {weather.wind_speed}km/h")
        else:
            print("Invalid choice.")

asyncio.run(get_weather())
