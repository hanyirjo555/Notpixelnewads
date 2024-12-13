import subprocess
import time
import webbrowser
from colorama import Fore, Back, Style, init

def print_banner():
    banner = """
░▀▀█░█▀█░▀█▀░█▀█
░▄▀░░█▀█░░█░░█░█
░▀▀▀░▀░▀░▀▀▀░▀░▀
╔══════════════════════════════════╗
║                                  ║
║  ZAIN ARAIN                      ║
║  AUTO SCRIPT MASTER              ║
║                                  ║
║  JOIN TELEGRAM CHANNEL NOW!      ║
║  https://t.me/AirdropScript6              ║
║  @AirdropScript6 - OFFICIAL      ║
║  CHANNEL                         ║
║                                  ║
║  FAST - RELIABLE - SECURE        ║
║  SCRIPTS EXPERT                  ║
║                                  ║
╚══════════════════════════════════╝
"""
    print(Fore.MAGENTA+ banner)
    print(Fore.YELLOW + 'CREATED BY : Zain Arain: ⨭ ' + Fore.GREEN + 'https://t.me/AirdropScript6')
    print(Fore.WHITE + 'JOIN OUR TELEGRAM CHANNEL ➤ ' + Fore.GREEN + 'https://t.me/AirdropScript6')
    print(Fore.RED + 'LEARN HACKING HERE ➤ ' + Fore.GREEN + 'https://www.youtube.com/@ZainArain279/videos')
    print(Fore.RED + 'DOWNLOAD MORE HACKS ➤ ' + Fore.GREEN + 'https://github.com/@ZainArain279')
    print(Fore.WHITE + 'BUY NODEPAY REFERAL HERE ➤ : ⨭ ' + Fore.GREEN + 'https://t.me/AirdropScript6')
    print(Fore.YELLOW + '⚡it was Paid but i gifted Free so please subscribe my channels ⚡ ')
    print(Fore.GREEN + '                  [𝍖𝍖𝍖 NOTPIXEL ADS WATCHER 𝍖𝍖𝍖]                  ')

# Initialize colorama
init(autoreset=True)

# Function to simulate a glowing effect for text
def glowing_text(text, color=Fore.CYAN, delay=0.1, iterations=5):
    for _ in range(iterations):
        print(f"{color}{text}", end="\r")  # Print text and overwrite it
        time.sleep(delay)
        print(" " * len(text), end="\r")  # Clear text
        time.sleep(delay)

# Function to run adduser.py script
def run_mainn():
    glowing_text("Running adduser.py script...", Fore.GREEN)
    try:
        subprocess.run(['python', 'adduser.py'], check=True)
        glowing_text("adduser.py script executed successfully.", Fore.GREEN)
    except subprocess.CalledProcessError:
        glowing_text("Error executing adduser.py", Fore.RED)

# Function to run start-mining-px.py script
def run_zain():
    glowing_text("Running start-mining-px.py script...", Fore.GREEN)
    try:
        subprocess.run(['python', 'start-mining-px.py'], check=True)
        glowing_text("start-mining-px.py script executed successfully.", Fore.GREEN)
    except subprocess.CalledProcessError:
        glowing_text("Error executing start-mining-px.py", Fore.RED)

# Function to open Telegram and YouTube channels
def open_channels():
    print(Fore.GREEN + "\nAttempting to open Telegram and YouTube channels...")
    # Open Telegram channel
    telegram_url = "https://t.me/AirdropScript6"
    youtube_url = "https://www.youtube.com/@ZainArain279/videos"
    
    try:
        # Attempt to open the URLs
        print(Fore.YELLOW + f"Opening Telegram: {telegram_url}")
        webbrowser.open(telegram_url)
        time.sleep(1)  # Short delay before opening the second link
        print(Fore.YELLOW + f"Opening YouTube: {youtube_url}")
        webbrowser.open(youtube_url)
    except Exception as e:
        print(Fore.RED + f"Failed to open channels: {e}")

# Main function to display the menu
def main():
    # First, open Telegram and YouTube channels
    open_channels()

    # After opening channels, show the main process
    while True:
        # Displaying the menu options with emojis
        print(Fore.GREEN + "💻 Please select an option:")
        print(Fore.YELLOW + "1: 🖥️ Run adduser.py")
        print(Fore.YELLOW + "2: 🖥️ Run start-mining-px.py")
        print(Fore.YELLOW + "3: Exit ❌")

        # Get user input with a cyberpunk theme
        choice = input(Fore.CYAN + "Enter your choice : ")

        if choice == '1':
            run_mainn()  # Run adduser.py
        elif choice == '2':
            run_zain()   # Run start-mining-px.py
        elif choice == '3':
            glowing_text("Exiting program... 🛑", Fore.RED)
            print(Back.BLACK + Fore.RED + "Exiting program. 🛑\n")
            break  # Exit the loop and end the program
        else:
            glowing_text("Invalid choice. Please try again. ❗", Fore.RED)

# Run the main function
if __name__ == "__main__":
    print_banner()  # Call the print_banner function to display the banner
    main()