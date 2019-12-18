# Calculator Exercise

This app simulates a calculator on a http server, where receives POST requests from a client, read from a CSV file.

## Files
* app.py : Server running on localhost on port 5000
* client.py : Read values and operations from *sample.csv* and send POST requests
* unittest_app.py : Unit testing of *app.py*
* sample.csv : Row of values and operations

## Prerequisites
Before execute the file, you need to install the requirements using
```
pip install -r requirements.txt
```
## Running
First step is to execute *app.py* file
```
python app.py
```
Then, the server will be listening and you will execute *client.py* to send POST requests 
```
python client.py
```
And it will give an output like 

![Output](/images/output.PNG)

And also a text file with all the logs.

## Test
You can also test *app.py* using the file unittest_app.py, that performs an unit testing to this file.

```
python unittest_app.py
```

![Output](/images/testing.PNG)
## Technologies
* Python 3.8.0
* Flask 1.1.1

by [@fhamouti](https://github.com/fhamouti)
