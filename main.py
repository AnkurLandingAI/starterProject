# This is a sample Python script.
import requests

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


def run_inference():
    response = requests.get('https://api.github.com/events')
    print(response.json())
    print(f'running inference on Cloud')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run_inference()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
