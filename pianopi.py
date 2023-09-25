#!/usr/bin/env python3

import mido
import websocket
from dotenv import load_dotenv
import os

def list_midi_input_ports():
    print("Available MIDI input ports:")
    for port, _ in enumerate(mido.get_input_names(), 1):
        print(f"{port}: {mido.get_input_names()[port-1]}")

def on_message(wsapp, message):
    print(message)

def main():
    print("running the script... but with more style this time")

    # Load environment variables
    env_file_path = "/etc/pianopi/.env"
    load_dotenv(dotenv_path=env_file_path)
    web_socket_url = os.getenv("WEB_SOCKET_URL")
    print(f"WEB_SOCKET_URL is configured as '{web_socket_url}'")

    # Connect to websocket
    wsapp = websocket.WebSocketApp(web_socket_url, on_message=on_message)
    wsapp.run_forever()
    wsapp.send("Hello, from python")
#
#     # List available MIDI input ports
#     list_midi_input_ports()
#
#     # Prompt the user to select a MIDI input port
#     selected_port_index = int(input("Enter the number of the MIDI input port you want to use: ")) - 1
#     input_ports = mido.get_input_names()
#
#     try:
#         # Open the selected MIDI input port
#         with mido.open_input(input_ports[selected_port_index]) as midi_in:
#             print(f"Connected to {input_ports[selected_port_index]}...")
#
#             # Start receiving and printing MIDI events
#             for message in midi_in:
#                 print(f"Received: {message}")
#                 wsapp.send(f"Received: {message}")
#
#     except KeyboardInterrupt:
#         print("\nExiting...")
#     except OSError as e:
#         print(f"Error: {e}")

if __name__ == "__main__":
    main()
