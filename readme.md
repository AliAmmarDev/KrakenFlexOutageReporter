#  KrakenFlex Outage Reporter

  

###  The following program reports outages on the KrakenFlex platform

  
  

##  Dependencies

  

Python **v3.8**

  

##  Setup

  

Setup repository

```bash

git clone https://github.com/AliAmmarDev/KrakenFlexOutageReporter.git
cd KrakenFlexOutageReporter

```

  
  

Create a virtual environment

```bash

python3 -m venv .venv

```

  

Activate virtual environment

```bash

source .venv/bin/activate

```

  

Install packages

```bash

python -m pip install -U pip wheel

pip install -r outage_reporter/requirements.txt

```

  

##  Execution

  

```bash

python ./main.py

```

  

##  Tests

  

Run the following command to execute unit tests

```bash

pytest ./outage_reporter/*

```