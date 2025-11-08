from flask import Flask, Response
import json
app = Flask(__name__)

@app.route('/prime_number/<number>')
def check(number):
    num = int(number)
    
    if num <=1:
            return f"The number {number} is not a prime number"
    for n in range(2,num):
        
        
             
        if num%n ==0:
            return f"The number  {number} is not a prime number"
            
    else:
            return f"The number {number} is a prime number"
        
@app.errorhandler(404)
def page_not_found(error_code):
    response = {
        "message":"Invalid endpoint",
        "status":404
    }
    res_json = json.dumps(response)
    res_html = Response(response=res_json,status=404,mimetype="application/json")
    return res_html
if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)