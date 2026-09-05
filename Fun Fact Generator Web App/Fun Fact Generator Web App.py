"""
In this tutorial, we will create a Fun Fact Generator Web App in Python using the PyWebIO module.
This app fetches random fun facts from the Useless Facts API and displays them on a web interface.

PyWebIO is a Python library that allows you to build simple web applications or browser-based GUI
apps without writing HTML or JS. It provides:

Functions for input and output in the browser
Easy styling for text and buttons
Session handling for interactive applications
"""

"""
How the App Works
Fetch data: The app sends a GET request to the Useless Facts API.
Parse JSON: The response is parsed using the json module to extract the fact text.
Display fact: The fact is displayed on the web interface using PyWebIO's put_text and style.
Interactive button: A "Click me" button allows users to generate new facts without refreshing the page.
"""

import json
import requests
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
from pywebio import start_server


def get_fun_fact(_=None):
    clear()

    put_html(
        '<p align="left">'
        '<h2><img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png" width="7%"> Fun Fact Generator</h2>'
        '</p>'
    )

    url = "https://uselessfacts.jsph.pl/random?language=en"

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        useless_fact = data['text']
    except requests.exceptions.RequestException as e:
        useless_fact = f"Fact fetch nahi ho paaya. Error: {e}"
    except (json.JSONDecodeError, KeyError):
        useless_fact = "API se galat response mila, dobara try karo."

    style(put_text(useless_fact), 'color:blue; font-size: 30px')

    put_buttons(
        [dict(label='Click me', value='outline-success', color='outline-success')],
        onclick=get_fun_fact
    )


def main():
    get_fun_fact(None)   # page load hote hi pehla fact dikhega
    hold()


if __name__ == '__main__':
    start_server(main, port=8081, debug=True)