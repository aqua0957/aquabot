from random import choice, randint
def get_response(user_input: str) -> str:
	lowered: str = user_input.lower()
	if lowered == '':
		return '...did you say something?'
	elif 'hello' in lowered or 'hi' in lowered:
		return 'Hello there!'
	elif 'spartan hackers' in lowered:
		return 'Yes, it is a very good club.'
	elif 'roll dice' in lowered:
		return f'You rolled: {randint(1,6)}'
	else:
		return choice(['Uhhh….', 'What are you talking about?', 'I don\'t get it', 'I give up trying to understand.'])
