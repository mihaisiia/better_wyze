# better_wyze - enhanced automation capabilities for Wyze devices
## Table of Contents
* [Introduction](#introduction)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)

## Features
* Turn on and off lights


## Setup

Set up an API key as described in [Creating an API Key by Wyze Support](https://support.wyze.com/hc/en-us/articles/16129834216731)  
Set the following environment variables:
* `BETTER_WYZE_ROOT`
* `WYZE_EMAIL`
* `WYZE_PASSWORD`
* `WYZE_API_KEY_ID`
* `WYZE_API_KEY`

Create a virtual environment with `python -m venv .venv`  
Activate the virtual environment with `source .venv/bin/activate` (unix) or `.venv\Scripts\Activate` (Windows)  
Install the dependencies with `pip install -r requirements.txt`

## Usage

```
cd src
python serve.py
```

### Planned
#### Fan Control
* Define weekdays to operate, similar to Wyze behaviors.
* Define time range to operate within (i.e. May 10th to September 30th), then sleep until next year.
* Fine control over cycling patterns (i.e. "in time frame 5am-9am, run )

## Introduction
Currently, the Wyze app offers little in the way of creating custom fan-only schedules and is limited to cycling the fan X amount of minutes for every hour of the day. On warmer days, homeowners without air conditioning may want to run their furnace fans in the mornings/evenings only, yet have no way to automate this behavior.

While others have found success using Home Assistant running on Raspberry Pi, they are [limited to Raspberry Pi 3 or above](https://www.home-assistant.io/installation/raspberrypi/).

better_wyze aims to give homeowners the control they want, all while being lightweight enough to run on boards such as Raspberry Pi Zero W.

## Acknowledgements
Thank you to [@chkoda](https://github.com/Chkoda) for his inspiration, guidance, and contributions throughout the project.

## Contact
Created by [@mihaisiia](https://www.github.com/mihaisiia), feel free to reach out to me on GitHub with questions or suggestions.
