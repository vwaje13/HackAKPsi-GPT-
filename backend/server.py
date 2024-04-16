from flask import Flask, request, jsonify
from flask_cors import CORS
import csv
import openai

app = Flask(__name__)
# Enable CORS for all routes from the specific origin where your React app is hosted
CORS(app, resources={r"/process-csv": {"origins": "http://localhost:3000"}})

# Replace 'your-openai-api-key' with your actual OpenAI API key.
openai.api_key = 'key'

# Path to your CSV file
filename = 'roster.csv'

def create_chat_messages(content):
    messages = [{
        "role": "system",
        "content": "You are a helpful assistant."
    }, {
        "role": "user",
        "content": content
    }]
    return messages

def send_chat_to_openai(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    return response.choices[0].message['content']

@app.route('/process-csv', methods=['POST'])
def process_csv():
    data = request.json
    sample_query = data.get('query', '')
    if not sample_query:
        return jsonify({"error": "Empty query"}), 400
    
    previous_context = "This is what we talked about earlier.\n"
    
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                previous_context += str(row) + "\n\n\n"
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    new_query = previous_context + "\n" + sample_query
    new_messages = create_chat_messages(new_query)
    final_result = send_chat_to_openai(new_messages)
    
    return jsonify({"response": final_result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

