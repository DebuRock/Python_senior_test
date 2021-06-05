# Python Senior Test

## Prerequisite
For running this project you need to check and do the bellow prerequisite steps:

* Make sure that mongodb cloud or localhost development server is running follow this link to install mongodb
https://docs.mongodb.com/manual/installation/. 
  
* mongodb service should be running on port 27017
  
* Restore data using mongodump archive. run the bellow commands
    ```commandline
    cd dumps
    mongorestore --archive="test_mongo_dump_archive" 
    ```
  for running the above command make sure that you have mongorestore tool installed, you can use the link here 
  https://docs.mongodb.com/database-tools/installation/installation/#installing-the-database-tools
  
* Make sure you have python3 and pip installed

## Setting up Development Environment And Running the application
Once your database is up and running then you should follow the bellow steps to prepare the development environment

* Create and activate a python virtual environment
  ```commandline
  python3 -m venv python-test-venv
  source python-test-venv/bin/activate
  ```
  
* Install python module dependencies
  ```commandline
  pip install -r requirements.txt
  ```
  
* Start the flask app
  ```commandline
  cd test_02
  python app.py  
  ```
  
* Check that application is running browsing the url http://localhost:5000/

* Run the testsuite file
  ```commandline
  python -m pytest  
  ```
