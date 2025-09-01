# buzzline-01-webb

![Python 3.11](https://img.shields.io/badge/Python-3.11-blue?logo=python&logoColor=white)

This project demonstrates streaming data analytics using Kansas City traffic conditions. 
It includes a custom producer that generates realistic traffic updates and a consumer that monitors for critical conditions.

## Setup

1. Clone this repository
2. Create and activate virtual environment:

Windows:
```shell
py -3.11 -m venv .venv
.venv\Scripts\activate
py -m pip install --upgrade pip setuptools wheel
py -m pip install --upgrade -r requirements.txt
```

## Running the Custom Traffic System

### Start the Traffic Producer (Terminal 1)

Windows:
```shell
.venv\Scripts\activate
py -m producers.custom_producer_webb
```

### Start the Traffic Consumer (Terminal 2)

Windows:
```shell
.venv\Scripts\activate
py -m consumers.custom_consumer_webb
```

## What It Does

- **Producer**: Generates realistic Kansas City traffic updates for highways like I-35, I-70, and I-435
- **Consumer**: Monitors traffic conditions and alerts on incidents, heavy traffic, and long travel times

## Stop Processes

Press `Ctrl+C` in each terminal to stop the processes.


## License
This project is licensed under the MIT License as an example project. 
You are encouraged to fork, copy, explore, and modify the code as you like. 
See the [LICENSE](LICENSE.txt) file for more.