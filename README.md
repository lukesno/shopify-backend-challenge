# Shopify's Backend Challenge for Summer 2022

Tech Stack: 

> Django  

Helpful Notes: 

* API implementation is found in `api/`   
* Website implemenetation is found in `inventory/`  
* Custom exceptions were created for API error handling (Found in `api/exceptions.py/`)  
* Serializers and forms were used to validate data  
* Read the comments for detailed descriptions!

## Getting Started

Prerequisites:   
> Python 3 (https://www.python.org/downloads/)  
  
Installation Steps (Mac):
1. Open terminal at desired location (Following steps are all executed on terminal)

2. Clone the repo: `git clone https://github.com/lukesno/shopify-backend-challenge`

3. Install/upgrade pip: `python3 -m pip install --user --upgrade pip`

4. Install virtualenv: `python3 -m pip install --user virtualenv`

5. Create a virtual environment (for dependency installation): `python3 -m venv env`

6. Activate the `env` environment that was created: `source env/bin/activate`

7. Install dependencies: `python3 -m pip install -r requirements.txt`

8. Start the app by running `python3 manage.py runserver`


Installation Steps (Windows):
1. Open command line at desired location (Following steps are all executed on terminal)

2. Clone the repo: `git clone https://github.com/lukesno/shopify-backend-challenge`

3. Install/upgrade pip: `python -m pip install --upgrade pip`

4. Install virtualenv: `pip install virtualenv`

5. Create a virtual environment (for dependency installation): `python -m venv env`

6. Activate the `env` environment that was created: `.\env\Scripts\activate`

7. Install dependencies: `pip install -r requirements.txt`

8. Start the app by running `python manage.py runserver`

