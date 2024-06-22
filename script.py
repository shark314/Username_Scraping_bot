import sys, os, asyncio, getopt, requests, json
from telethon.sync import TelegramClient
from dotenv import load_dotenv, find_dotenv

# Load the .env file
load_dotenv(find_dotenv())

# Get the values from the .env file
api_id = os.getenv('api_id')
api_hash = os.getenv('api_hash')
phone_number = os.getenv('phone_number')
print(api_id, api_hash, phone_number)

def getHelp():
	print("\nList of options:\n\n" +
		"-(t)oken of bot to control\n" +
		"--help to show this help message\n\n")
	sys.exit(0)

# Open the group_id.txt file
with open('group_id.txt', 'r') as file:
	# Read the contents of the file
	group_ids = file.read().splitlines()
	print(group_ids)

# Set the time range to get messages from
flag=0

async def get_group_messages():
	print('123123')
	# Create a Telegram client with the specified API ID, API hash and phone number
	print('---------session_name---------', api_id, api_hash)
	client = TelegramClient('session_name', api_id, api_hash)
	await client.connect()

	# Check if the user is already authorized, otherwise prompt the user to authorize the client
	if not await client.is_user_authorized():
		await client.send_code_request(phone_number)
		await client.sign_in(phone_number, input('Enter the code: '))
	
	participants = []
	messages = []
	participant_info = set()
	for group_id in group_ids:
		print(group_id)
		# Get the ID of the specified group
		group = await client.get_entity(int(group_id))
		participants = participants + await client.get_participants(group)
		# Get the messages in the group since 5 days ago
		messages = messages + await client.get_messages(int(group_id), None, offset_id=0)	
		for participant in participants:
			participant_info.add(
				(participant.id, participant.username, participant.first_name)
			)
		print('participant_info', list(participant_info), len(messages))
	with open('unique_participants.json', 'w') as f:
		json.dump(list(participant_info), f, indent=4)

	unique_authors = set()
	for message in messages:
		if message.sender and message.sender.username:
			author_info = (message.sender.username, message.sender.id, message.sender.first_name)
			unique_authors.add(author_info)
		else:
			print("message.sender.username is None")
	print("unique_authors=================>>>>>>>>>>>>>>>>>>>\n", unique_authors)
	with open('unique_message_authors.json', 'w') as f:
		json.dump(list(unique_authors), f, indent=4)
	for author in unique_authors:
	    print(f"Username: {author[0]}, User ID: {author[1]}, First Name: {author[2]}")

def run_async_jobs():
	asyncio.run(get_group_messages())

if __name__ == "__main__":	

	token = os.getenv('token')
	argv = sys.argv[1:]

	# try getting supported parameters and args from command line
	try:
		opts, args = getopt.getopt(argv, "t:",
			["token=", "help"])
	except:
		print("Error parsing options")
		getHelp()

	for opt, arg in opts:
		if opt in ['-t', '--token']:
			try:
				# connect to Telegram API with their getMe test method for checking API works
				testResponse = requests.get("https://api.telegram.org/bot%s/getMe" % (str(arg)))
				# set the token to be used if we get a 2xx response code back
				if testResponse.ok:
					token = str(arg)
				else:
					print("Error validating your token!")
					getHelp()
			except:
				print("Error trying to validate your token!")
				getHelp()
		if opt in ['--help']:
			getHelp()

	run_async_jobs()
	# schedule.run_pending()
	# time.sleep(1)

