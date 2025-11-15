from random import choice, randint
from groq import Groq
import openai
import os

def get_response(user_input: str) -> str:
	lowered: str = user_input.lower()

	client = Groq()

	chat_completion = client.chat.completions.create(
		messages=[
			{
				"role": "system",
				"content": "You are a Discord user named Aqua."
			},
			{
				"role": "user",
				"content": lowered,
			}
		],
		model="llama-3.3-70b-versatile"
	)
	return chat_completion.choices[0].message.content

