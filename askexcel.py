import openai
import csv

# Set up your OpenAI API key
openai.api_key = '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'
 # Replace with your actual API key
from langchain_experimental.agents.agent_toolkits import create_csv_agent

from langchain.llms import OpenAI
from dotenv import load_dotenv
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# Allow requests from 'http://localhost:3000'
CORS(app)
OPENAI_API_KEY= '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'

app.config['MAX_CONTENT_LENGTH'] = 0.2 * 1024 * 1024  # 200kb
# Create a directory for storing uploaded files within the app context
UPLOAD_FOLDER = os.path.join(app.root_path, 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route('/chat_csv', methods=['POST'])
def chat_csv():
    
    print(request.form.get('query'))
    load_dotenv()
    query = request.form.get('query')
    print(query)
    csv_file = request.files.get('csv_file')
    if csv_file is None:
        return jsonify({"error": "No CSV file provided"}), 400
 
  # Get the original file name
    original_filename = csv_file.filename

    # Create a path for saving the uploaded file
    file_path = os.path.join(UPLOAD_FOLDER, original_filename)

    # Save the uploaded file with the original name
    csv_file.save(file_path)


    agent = create_csv_agent(
        OpenAI(temperature=0, max_tokens=500), file_path, verbose=True)

    prompt = query #"Which product line had the lowest average price"

    if prompt is None or prompt == "":
        return jsonify({"error": "No user question provided"}), 400
    
    response = agent.run(prompt)
    
    # You can format the response as needed, e.g., convert to JSON
    response_json = {"answer": response}
    
    return jsonify(response_json), 200

if __name__ == "__main__":
    app.run(debug=True)

