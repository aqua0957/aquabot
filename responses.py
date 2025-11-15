from random import choice, randint
from groq import Groq
import openai
import os

def get_response(user_input: str) -> str:
	input: str = user_input

	client = Groq()

	chat_completion = client.chat.completions.create(
		messages=[
			{
				"role": "system",
				"content": """You are a Discord user named Aqua.
Do not directly mention any of these character traits unless explicitly asked by the user.
"""
			},
			{
				"role": "user",
				"content": input,
			}
		],
		model="llama-3.3-70b-versatile"
	)
	return chat_completion.choices[0].message.content

