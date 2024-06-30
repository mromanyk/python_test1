from datetime import datetime, timedelta


class News:
    def __init__(self, content, city):
        self.content = content
        self.city = city
        self.date = datetime.now().strftime("%d/%m/%Y %H:%M")

    def write(self, file):
        with open(file, 'a') as f:
            f.write(f"News: " + "-" * 24 + "\n")
            f.write(f"{self.content}\n")
            f.write(f"{self.city}, {self.date}\n")
            f.write("\n" + "-" * 30 + "\n\n")


class Advertisement:
    def __init__(self, content, expiry_days):
        self.content = content
        self.expiry_date = (datetime.now() + timedelta(days=expiry_days)).strftime("%d/%m/%Y")
        self.remaining_days = expiry_days

    def write(self, file):
        with open(file, 'a') as f:
            f.write("Advertisement: " + "-" * 15 + "\n")
            f.write(f"{self.content}\n")
            f.write(f"Actual until: {self.expiry_date}, {self.remaining_days} days left\n")
            f.write("\n" + "-" * 30 + "\n\n")


class WeatherForecast:
    def __init__(self, content, temperature_celsius):
        self.content = content
        self.temperature_celsius = temperature_celsius
        self.temperature_fahrenheit = self.calculate_fahrenheit(temperature_celsius)

    def calculate_fahrenheit(self, celsius):
        return celsius * 9 / 5 + 32

    def write(self, file):
        with open(file, 'a') as f:
            f.write("Weather Forecast: " + "-" * 12 + "\n")
            f.write(f"{self.content}\n")
            f.write(f"Temperature: {self.temperature_celsius}°C / {self.temperature_fahrenheit}°F\n")
            f.write("\n" + "-" * 30 + "\n\n")


class SaveMessage:
    def __init__(self):
        self.file = "news_feed.txt"

    def get_user_input(self):
        while True:
            choice = input("Enter 1 for News, 2 for Advertisement, 3 for Weather Forecast: \n")
            if choice in ['1', '2', '3']:
                break
            else:
                print("Invalid input. Please enter 1, 2, or 3.")

        content = input("Enter the content: ")
        if choice == '1':
            city = input("Enter the city: ")
            message = News(content, city)
        elif choice == '2':
            expiry_days = int(input("Enter the number of days the advertisement is valid: "))
            message = Advertisement(content, expiry_days)
        elif choice == '3':
            temperature_celsius = float(input("Enter the temperature in Celsius: "))
            message = WeatherForecast(content, temperature_celsius)

        message.write(self.file)
        print("Message has been written to the file.")


# Main execution
jobrunner = SaveMessage()
jobrunner.get_user_input()
