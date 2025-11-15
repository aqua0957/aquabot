from random import choice, randint
import openai
import os

def get_response(user_input: str) -> str:
	lowered: str = user_input.lower()

	client = openai.OpenAI(
		api_key=os.environ.get("GROQ_API_KEY"),
		base_url="https://api.groq.com/openai/v1"
	)

	response = client.responses.create(
		model="llama-3.3-70b-versatile",
		input=lowered
	)

	return response.output_text


