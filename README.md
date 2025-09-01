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

Mac/Linux:
```zsh
python3 -3.11 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install --upgrade -r requirements.txt
```

## Running the Custom Traffic System

### Start the Traffic Producer (Terminal 1)

Windows:
```shell
.venv\Scripts\activate
py -m producers.custom_producer_webb
```

Mac/Linux:
```zsh
source .venv/bin/activate
python3 -m producers.custom_producer_webb
```

### Start the Traffic Consumer (Terminal 2)

Windows:
```shell
.venv\Scripts\activate
py -m consumers.custom_consumer_webb
```

Mac/Linux:
```zsh
source .venv/bin/activate
python3 -m consumers.custom_consumer_webb
```

## What It Does

- **Producer**: Generates realistic Kansas City traffic updates for highways like I-35, I-70, and I-435
- **Consumer**: Monitors traffic conditions and alerts on incidents, heavy traffic, and long travel times

## Stop Processes

Press `Ctrl+C` in each terminal to stop the processes.

## License

MIT License - See [LICENSE](LICENSE.txt) file.