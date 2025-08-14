from flask import Flask, render_template, request, jsonify, Response, stream_with_context
import ollama

app = Flask(__name__)
messages = [] 
model_name = 'llama3.2' 

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    messages.append({'role': 'user', 'content': user_message})

    # The generator function will yield chunks as they arrive
    def generate_stream():
        full_response_content = ""
        try:
            stream = ollama.chat(
                model=model_name,
                messages=messages,
                stream=True,  # Crucially, enable streaming
            )
            for chunk in stream:
                content = chunk['message']['content']
                if content:
                    full_response_content += content
                    yield content  # Yield the content chunk
        except Exception as e:
            yield f"Error: An unexpected error occurred: {e}"
        finally:
            messages.append({'role': 'assistant', 'content': full_response_content})

    # Return a streaming response
    return Response(stream_with_context(generate_stream()), mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True, port=5000)