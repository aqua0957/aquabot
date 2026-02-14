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
				"content": """You are a Discord bot that preforms automatic translations from English into Simplified Chinese, according to standards used in mainland China. When input is recieved, output the input text translated into Simplified Chinese only.
"""
			},
			{
				"role": "user",
				"content": input,
			}
		],
		model="openai/gpt-oss-120b"
	)
	return chat_completion.choices[0].message.content

