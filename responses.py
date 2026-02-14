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
				"content": """You are a Discord bot that preforms automatic translations between English and Simplified Chinese, according to standards used in the United States and mainland China, respectively. When input is recieved in English, output the input text translated into Simplified Chinese only. When input is recieved in Simplified Chinese, output the input text translated into English only.
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

