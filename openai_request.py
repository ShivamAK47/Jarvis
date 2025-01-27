import openai
import user_config

# Set up the OpenAI client with the API key
openai.api_key = user_config.openai_key

def send_request(query):
    # Sending a chat completion request
    completion = openai.ChatCompletion.create(
        model="gpt-4",  # Replace with a valid model name
        messages=[
            {
                "role": "user",
                "content": query
            }
        ]
    )
    # Return the response content
    return completion.choices[0].message["content"]
