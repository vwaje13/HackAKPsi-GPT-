import csv
import openai

# Set your OpenAI API key here
#openai.api_key = 'my key'

# Path to your CSV file
filename = 'roster.csv'

def create_chat_messages(row):
    # Convert the row data into a message format for the chat
    # You might want to adjust the content based on your specific requirements
    messages = [{
        "role": "system",
        "content": "You are a helpful assistant."
    }, {
        "role": "user",
        "content": f"Process this information: {row}"
    }]
    return messages

# Function to send chat messages to OpenAI's API using GPT-3.5 Turbo
def send_chat_to_openai(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # Specify GPT-3.5 Turbo model
        messages=messages,
        # Add any other parameters as needed
    )
    return response.choices[0].message['content']

# Read the CSV and process each row
results = []

"""
with open(filename, mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:
        # Create chat messages from the row data
        messages = create_chat_messages(row)
        # Send the messages to OpenAI and store the response
        print("Sending Call")
        result = send_chat_to_openai(messages)
        results.append(result)
"""



previous_context = "This is what we talked about earlier.\n"

with open(filename, mode='r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        #print(str(row))
        previous_context += str(row) + "\n\n\n"


sample_query = "Which brothers are in Manglona"

new_query = previous_context + "\n" + sample_query
new_messages = create_chat_messages(new_query)
final_result = send_chat_to_openai(new_messages)

print(final_result)