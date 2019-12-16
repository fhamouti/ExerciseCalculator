from flask import Flask
import json

#Init server
app = Flask(__name__)

def add(x,y):
    #Add function
    return x + y

def subtract(x,y):
    #Subtract function
    return x - y

def multiply(x,y):
    #Multiply function
    return x * y

def divide(x,y):
    #Divide function
    if y == 0:
        raise ValueError('Can not divide by 0')
   
    return x / y

@app.route('/', methods=['GET','POST'])
def calculator():
   
    value_1 = 2
    operator = 'x'
    value_2 = 2
    
    #Choose operation
    if(operator == '+'):
        result = add(value_1,value_2)
    elif(operator == '-'):
        result = subtract(value_1,value_2)
    elif(operator == '*'):
        result = multiply(value_1,value_2)
    elif(operator == '/'):
        result = divide(value_1,value_2)
    else:
        result = 'INVALID CHOICE'
   
    #Return result
    return result

if __name__ == '__main__':
    #Run server in port 5000
    app.run(debug=True, port=5000)
