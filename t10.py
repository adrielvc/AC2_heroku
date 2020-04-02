import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)
@app.route('/')

def primos():

 total = 99
    pr = 1
    c = 1
    num = 3

    primos = "2,"

    while pr < total:
        numprimo = 1
        for i in range(2, num):
            if num % i == 0:
                numprimo = 0
                break
        if (numprimo):
            primos = primos + str(num) + ","
            pr += 1
        num += 1

    return primos

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

