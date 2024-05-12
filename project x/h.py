import requests
import time

# Flask app URL
flask_url = 'http://192.168.1.7:5002/receive_user_number'  # Update with your Flask app's URL

def send_user_number():
    try:
        # Prompt the user to enter a number
        user_input = input("Enter a number: ")
        random_number = int(user_input)  # Convert user input to an integer
        
        # Prepare JSON data with the entered number
        data = {'random_number': random_number}

        # Send a POST request to the Flask app with the JSON data
        response = requests.post(flask_url, json=data)
        
        # Check if the request was successful
        if response.ok:
            print(f"Number {random_number} sent successfully to Flask app")
        else:
            print(f"Failed to send number to Flask app. Status code: {response.status_code}")

    except ValueError:
        print("Invalid input. Please enter a valid integer.")

    except requests.exceptions.RequestException as e:
        print(f"Error occurred while sending number: {e}")

if __name__ == '__main__':
    while True:
        send_user_number()
        # Introduce a delay (e.g., prompt every 5 seconds)
        time.sleep(1)
