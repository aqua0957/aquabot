from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response
import requests
import subprocess
from groq import Groq
import openai
import asyncio



load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents = intents)

def check_groq_credentials():
        """

        Check if Groq API credentials are valid by attempting to get an access token.

        Returns True if valid, False otherwise.

        """
        client = Groq(
            # This is the default and can be omitted
             api_key=os.environ.get("GROQ_API_KEY"),
        )

        # Check if credentials exist
        if not client:
            print("❌ Missing Groq credentials in .env file")
            return False

        # Test credentials by requesting a client credentials token
        models = client.models.list()
        try:
            response = models
            if len(response.model_dump_json()) != 0:
                print("✅ Groq credentials are valid")
                return True
            else:
                print(f"❌ Groq credentials invalid. Status: {response.status_code}")
                print(f"Response: {response.model_dump_json()}")
                return False
        except Exception as e:
            print(f"❌ Error checking Groq credentials: {e}")
            return False

def kill_processes_on_port(port):
    """Kill processes on Windows"""
    try:
        # Find processes using the port
        result = subprocess.run(['netstat', '-ano'],
                              capture_output=True, text=True, check=False)

        if result.returncode == 0:
            lines = result.stdout.split('\n')
            pids_to_kill = []

            for line in lines:
                if f':{port}' in line and 'LISTENING' in line:
                    parts = line.split()
                    if len(parts) >= 5:
                        pid = parts[-1]  # Last column is PID
                        if pid.isdigit():
                            pids_to_kill.append(pid)

            if pids_to_kill:
                print(f"Found processes on port {port}: {pids_to_kill}")
                for pid in pids_to_kill:
                    try:
                        subprocess.run(['taskkill', '/F', '/PID', pid],
                                     check=True, capture_output=True)
                        print(f"Killed process {pid} on port {port}")
                    except subprocess.CalledProcessError as e:
                        print(f"Failed to kill process {pid}: {e}")
            else:
                print(f"No processes found on port {port}")
        else:
            print(f"Failed to run netstat: {result.stderr}")
    except Exception as e:
        print(f"Error killing processes on port {port}: {e}")


async def send_message(message: Message, user_message: str) -> None:
	if not user_message:
		print('(Message was empty because intents were not enabled properly)')
		return
	if is_private := user_message[0] == '?':
		User_message = user_message[1:]
	try:
		response : str = get_response(user_message)
		await message.author.send(response) if is_private else await message.channel.send(response)
	except Exception as e:
		print(e)

@client.event
async def on_ready() -> None:
	print(f'{client.user} is now running!')

@client.event
async def on_message(message: Message) -> None:
	if message.author == client.user:
		return
	username: str = str(message.author)
	user_message: str = message.content
	channel: str = str(message.channel)
	print(f'[{channel}] {username}: "{user_message}"')
	await send_message(message, user_message)

def main() -> None:
     check_groq_credentials()
     kill_processes_on_port(8090)
     client.run(token=TOKEN)
if __name__ == '__main__':
	main()


