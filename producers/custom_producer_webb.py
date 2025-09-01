"""
custom_producer_webb.py

Generate streaming Kansas City traffic condition updates.
Simulates real-time traffic monitoring data for KC area highways.
"""

#####################################
# Import Modules
#####################################

# Import packages from Python Standard Library
import os
import random
import time

# Import external packages (must be installed in .venv first)
from dotenv import load_dotenv

# Import functions from local modules
from utils.utils_logger import logger

#####################################
# Load Environment Variables
#####################################

# Load environment variables from .env
load_dotenv()

#####################################
# Define Getter Functions for .env Variables
#####################################

# Define a function to fetch the message interval from the environment
def get_message_interval() -> int:
    """
    Fetch message interval from environment or use a default value.

    It doesn't need any outside information, so the parentheses are empty.
    It returns an integer, so we specify that in the function signature.

    The colon at the end of the function signature is required.
    All statements inside the function must be consistently indented.

    Define a local variable to hold the value of the environment variable
    os.getenv() is a function that fetches the value of an environment variable
    os.getenv() always returns a string 
    We convert the return value to an integer using the built-in Python int() function
    To use handy functions like this, import the os module 
    from the Python Standard Library (see above).
    """
    return_value: str = os.getenv("MESSAGE_INTERVAL_SECONDS", 3)
    interval: int = int(return_value)
    logger.info(f"Messages will be sent every {interval} seconds.")
    return interval


#####################################
# Define global variables
#####################################

# Define lists for generating Kansas City traffic updates
KC_HIGHWAYS: list = ["I-35", "I-70", "I-435", "I-470", "US-71", "US-169", "K-10"]
TRAFFIC_CONDITIONS: list = ["heavy", "moderate", "light", "stop-and-go", "congested", "flowing"]
INCIDENTS: list = ["accident", "construction", "stalled vehicle", "road closure", "weather delay"]
DIRECTIONS: list = ["northbound", "southbound", "eastbound", "westbound"]
LOCATIONS: list = ["downtown", "near the Plaza", "at Grandview Triangle", "near KCI Airport", 
                  "at the Mixing Bowl", "near Union Station", "at State Line Road"]

#####################################
# Define a function to generate buzz messages
#####################################


def generate_messages():
    """
    Generate a stream of Kansas City traffic condition messages.
    
    This function uses a generator to yield traffic updates
    for Kansas City area highways and roads.
    """
    while True:
        highway = random.choice(KC_HIGHWAYS)
        direction = random.choice(DIRECTIONS)
        location = random.choice(LOCATIONS)
        
        # Generate different types of traffic messages
        message_type = random.choice(["condition", "incident", "travel_time"])
        
        if message_type == "condition":
            condition = random.choice(TRAFFIC_CONDITIONS)
            yield f"Traffic on {highway} {direction} is {condition} {location}"
            
        elif message_type == "incident":
            incident = random.choice(INCIDENTS)
            delay = random.randint(5, 45)
            yield f"ALERT: {incident.title()} on {highway} {direction} {location} - expect {delay} min delays"
            
        else:  # travel_time
            travel_time = random.randint(15, 90)
            yield f"Current travel time on {highway} {direction} {location}: {travel_time} minutes"


#####################################
# Define main() function to run this producer.
#####################################


def main() -> None:
    """
    Main entry point for this producer.

    It doesn't need any outside information, so the parentheses are empty.
    It doesn't return anything, so we say the return type is None.   
    The colon at the end of the function signature is required.
    All statements inside the function must be consistently indented. 
    This is a multiline docstring - a special type of comment 
    that explains what the function does.
    """

    logger.info("START Kansas City traffic producer...")
    logger.info("Hit CTRL c (or CMD c) to close.")
    
    # Call the function we defined above to get the message interval
    # Assign the return value to a variable called interval_secs
    interval_secs: int = get_message_interval()

    for message in generate_messages():
        logger.info(message)
        # Use the time module to pause execution for a specified number of seconds
        # The time.sleep() function takes a single argument: the number of seconds to pause
        time.sleep(interval_secs)

    logger.info("NOTE: See the `logs` folder to learn more.")
    logger.info("END producer.....")


#####################################
# Conditional Execution
#####################################

# If this file is the one being executed, call the main() function
if __name__ == "__main__":
    # Call the main function by writing its name followed by parentheses.
    main()
