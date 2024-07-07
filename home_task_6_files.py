from datetime import datetime, timedelta
from home_task_4_functions import final_text

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

class LoadFromFile:
    def __init__(self, path_to_file):
        self.path_to_file = path_to_file

    def write(self,file):
        with open(self.path_to_file, 'r') as input_file:
            content_from_file = input_file.read()
        with open(file, 'a') as f:
            f.write(content_from_file)


class SaveMessage:
    def __init__(self):
        self.file = "news_feed.txt"

    def get_user_input(self):
        while True:
            choice = input("Enter 1 for News, 2 for Advertisement, 3 for Weather Forecast, 4 for load from file, 0 for exit: \n")
            message = None
            if choice == '1':
                content = input("Enter the content: ")
                city = input("Enter the city: ")
                message = News(content, city)
                message.write(self.file)
                print("Message has been written to the file.")
                break
            elif choice == '2':
                content = input("Enter the content: ")
                expiry_days = int(input("Enter the number of days the advertisement is valid: "))
                message = Advertisement(content, expiry_days)
                message.write(self.file)
                print("Message has been written to the file.")
                break
            elif choice == '3':
                content = input("Enter the content: ")
                temperature_celsius = float(input("Enter the temperature in Celsius: "))
                message = WeatherForecast(content, temperature_celsius)
                message.write(self.file)
                print("Message has been written to the file.")
                break
            elif choice == '4':
                path_to_file = input("Enter the path to file: ")
                with open(path_to_file, 'r') as input_file:
                    content_from_file = input_file.read()
                lines = content_from_file.split('\n\n')
                for i in lines:
                    feed = i.split('\n')
                    feed_type = final_text(feed[0])
                    feed_content = final_text(feed[1])
                    feed_param = final_text(feed[2])
                    if feed_type == 'Weather forecast':
                        message = WeatherForecast(feed_content, float(feed_param))
                    elif feed_type == 'News':
                        message = News(feed_content, feed_param)
                    elif feed_type == 'Advertisement':
                        message = Advertisement(feed_content, int(feed_param))
                    message.write(self.file)
                    print(feed_type, "message from file have been written to the file.")
                break
            elif choice == '0':
                break
            else:
                print("Invalid input. Please enter 1, 2, 3, 4 or 0.")


# Main execution
jobrunner = SaveMessage()
jobrunner.get_user_input()
