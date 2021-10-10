from command import *



print("         __       ___      .______     ____    ____  __       _______.")
print("        |  |     /   \     |   _  \    \   \  /   / |  |     /       |")
print("        |  |    /  ^  \    |  |_)  |    \   \/   /  |  |    |   (----`")
print("  .--.  |  |   /  /_\  \   |      /      \      /   |  |     \   \    ")
print("  |  `--'  |  /  _____  \  |  |\  \----.  \    /    |  | .----)   |   ")
print("   \______/  /__/     \__\ | _| `._____|   \__/     |__| |_______/    ")
print("                                                                      ")
print("            ***********************************************           ")
print("            **     Jarvis - Your's Friendly Assistant.   **           ")
print("            ***********************************************  \n       ")

welcome = pyttsx3.init()
myname = os.getlogin()
welcome.say("Hello "+ myname +" i am Jarvis . How can i help you")
print("Hello "+ myname +" i am Jarvis . How can i help you ? \n")
print("Type help and hit Enter to Find All Available Commands. \n")
welcome.runAndWait()



chat()
