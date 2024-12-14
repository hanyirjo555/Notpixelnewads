import requests
import random
import time
from termcolor import colored

# Define the ASCII banner and tagline
ascii_banner = """
    ______      __        __  ______                 __
   / ____/___  / /_____  / /_/ ____/______  ______  / /_____
  / /_  / __ \/ //_/ _ \/ __/ /   / ___/ / / / __ \/ __/ __ \\
 / __/ / /_/ / ,< /  __/ /_/ /___/ /  / /_/ / /_/ / /_/ /_/ /
/_/    \____/_/|_|\___/\__/\____/_/   \__, / .___/\__/\____/
                                     /____/_/
"""

tagline = """
 +-+-+-+-+-+-+ +-+-+-+-+ +-+-+ +-+-+-+-+ +-+-+-+-+-+-+-+-+
 |A|n|y|o|n|e| |w|a|n|t| |d|o| |s|o|m|e| |d|o|n|a|t|i|o|n|
 +-+-+-+-+-+-+ +-+-+-+-+ +-+-+ +-+-+-+-+ +-+-+-+-+-+-+-+-+
"""

# Print the banner with colors
print(colored("=" * 70, "magenta"))
print(colored(ascii_banner, "cyan", attrs=["bold"]))
print(colored(tagline, "yellow", attrs=["bold"]))
print(colored("=" * 70, "magenta"))
print(colored("Telegram: https://t.me/foketcrypto", "green", attrs=["bold", "underline"]))
print(colored("YouTube: https://youtube.com/@foketcrypto", "red", attrs=["bold", "underline"]))
print(colored("=" * 70, "magenta"))

# Initialize a counter for successful 200 responses
success_count = 0

# Store multiple tg_id values
tg_ids = ["7302925429"]  # Default tg_id list

def generate_random_chat_instance():
    """Generate a random chat_instance as a large numeric string."""
    return str(random.randint(10**18, 10**19 - 1))

def fetch_ads(tg_id):
    """Fetch ads and handle the response for a specific tg_id."""
    global success_count
    url = 'https://api.adsgram.ai/adv'
    params = {
        'blockId': '4853',
        'tg_id': tg_id,
        'tg_platform': 'ios',
        'platform': 'Linux armv81',
        'language': 'en',
        'chat_type': 'sender',
        'chat_instance': generate_random_chat_instance(),
        'top_domain': 'app.notpx.app'
    }
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Origin': 'https://app.notpx.app',
        'Referer': 'https://app.notpx.app/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"'
    }

    # Send the initial request
    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        success_count += 1
        print(f"[tg_id: {tg_id}] Successful ads watch: {success_count}")
        try:
            # Parse the JSON response
            data = response.json()

            # Extract the 'reward' URL from the 'trackings' array
            trackings = data.get('banner', {}).get('trackings', [])
            reward_url = None
            for tracking in trackings:
                if tracking.get('name') == 'reward':
                    reward_url = tracking.get('value')
                    break

            if reward_url:
                # Make the follow-up request to the reward URL
                reward_response = requests.get(reward_url)
                print(f"[tg_id: {tg_id}] Reward claimed for ad.")
            else:
                print(f"[tg_id: {tg_id}] Reward URL not found in the response.")
        except ValueError:
            print(f"[tg_id: {tg_id}] Failed to parse JSON response.")
    else:
        print(f"[tg_id: {tg_id}] Initial request failed with status code {response.status_code}")
        print(response.text)

    # Notify when a milestone is reached
    if success_count % 20 == 0:
        print(f"Milestone reached: {success_count} successful responses.")

def add_tg_id():
    """Add a new tg_id to the list."""
    global tg_ids
    new_tg_id = input("Enter a new tg_id: ")
    if new_tg_id.isdigit():
        tg_ids.append(new_tg_id)
        print(f"tg_id {new_tg_id} added to the list.")
    else:
        print("Invalid tg_id. Please enter a numeric value.")

def list_tg_ids():
    """List all stored tg_ids."""
    global tg_ids
    print("Currently stored tg_ids:")
    for idx, tg_id in enumerate(tg_ids, start=1):
        print(f"{idx}. {tg_id}")

# Main menu
while True:
    print("\n1. Start fetching ads for all tg_ids")
    print("2. Add a new tg_id")
    print("3. List all tg_ids")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        print("Starting ad fetching for all tg_ids...")
        while True:
            for tg_id in tg_ids:
                fetch_ads(tg_id)
            print("Waiting for 25 seconds before the next cycle...")
            time.sleep(25)
    elif choice == "2":
        add_tg_id()
    elif choice == "3":
        list_tg_ids()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")