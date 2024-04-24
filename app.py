from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

price_api_key = "579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b"  


    
@app.route('/price', methods=['POST'])
def GetPrice():
 
    api_url = "https://api.data.gov.in/resource/9ef84268-d588-465a-a308-a864a43d0070"
    
    # Define the parameters for the API request
    params = {
		'api-key': price_api_key,
        'format': 'json',
        'limit': 1,
        'filters[state]': request.form['state'],
        'filters[district]': request.form['district'],
        'filters[market]': request.form['market'],
        'filters[commodity]': request.form['commodity']
    }

    try:
        response = requests.get(api_url,params=params)
        response_data = response.json()

        # Process the response data
       
        max_price = int(response_data["records"][0]["max_price"])
        max_price=max_price/100
        min_price = int(response_data["records"][0]["min_price"])
        min_price=min_price/100

        
        return jsonify({"max_price": max_price, "min_price": min_price}), 200
    except Exception as e:
        return str(e), 500  
