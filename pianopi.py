#!/usr/bin/env python3

import mido
import websocket
from dotenv import load_dotenv
import os
import rel

def list_midi_input_ports():
    print("Available MIDI input ports:", flush=True)
    for port, _ in enumerate(mido.get_input_names(), 1):
        print(f"{port}: {mido.get_input_names()[port-1]}", flush=True)

def on_message(ws, message):
    print(message, flush=True)

def on_error(ws, error):
    print(error, flush=True)

def on_close(ws, close_status_code, close_msg):
    print("### closed ###", flush=True)

def on_open(ws):
    print("Opened connection", flush=True)
    # List available MIDI input ports
    list_midi_input_ports()

def main():
    print("running the script... with all the flushes", flush=True)

    # Load environment variables
    env_file_path = "/etc/pianopi/.env"
    load_dotenv(dotenv_path=env_file_path)
    web_socket_url = os.getenv("WEB_SOCKET_URL")
    print(f"WEB_SOCKET_URL is configured as '{web_socket_url}'", flush=True)

    # Connect to websocket
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(web_socket_url,
                              on_open=on_open,
                              on_message=on_message,
                              on_error=on_error,
                              on_close=on_close)
    ws.run_forever(dispatcher=rel, reconnect=5)  # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()
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
#             print(f"Connected to {input_ports[selected_port_index]}...", flush=True)
#
#             # Start receiving and printing MIDI events
#             for message in midi_in:
#                 print(f"Received: {message}", flush=True)
#                 ws.send(f"Received: {message}")
#
#     except KeyboardInterrupt:
#         print("\nExiting...", flush=True)
#     except OSError as e:
#         print(f"Error: {e}", flush=True)

if __name__ == "__main__":
    main()
