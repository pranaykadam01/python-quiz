import time
import webbrowser

def countdown(seconds):
    print("Get ready for a surprise!")
    for i in range(seconds, 0, -1):
        print(f"Surprise in {i} seconds...", end="\r")
        time.sleep(1)
    print("Here it comes!\n")

def surprise_message():
    print("Dear Love,")
    print("I just wanted to take a moment to say how much you mean to me.")
    print("You're truly wonderful, and I'm so grateful to have you in my life.")
    print("Here's a little surprise to brighten your day!\n")

def ascii_heart():
    print("     ******       ******")
    print("   **      **   **      **")
    print(" **         ** **         **")
    print(" **          ***          **")
    print("  **                      **")
    print("    **                  **")
    print("      **              **")
    print("         **        **")
    print("            **  **")
    print("              **\n")

def play_song():
    # Opens a YouTube link to a romantic song in the web browser
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # replace with any romantic song link

def main():
    countdown(5)  # Countdown from 5 seconds
    surprise_message()
    ascii_heart()
    print("Here's a song just for you!\n")
    play_song()

# Run the program
main()
