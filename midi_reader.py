#!/usr/bin/env python3

import mido
import websocket

def list_midi_input_ports():
    print("Available MIDI input ports:")
    for port, _ in enumerate(mido.get_input_names(), 1):
        print(f"{port}: {mido.get_input_names()[port-1]}")

def on_message(wsapp, message):
    print(message)

def main():
    # Connect to websocket
    ws = websocket.WebSocket()
    ws.connect("wss://inalltwelvekeys.com")
    ws.send("Hello, from python")

    # List available MIDI input ports
    list_midi_input_ports()

    # Prompt the user to select a MIDI input port
    selected_port_index = int(input("Enter the number of the MIDI input port you want to use: ")) - 1
    input_ports = mido.get_input_names()

    try:
        # Open the selected MIDI input port
        with mido.open_input(input_ports[selected_port_index]) as midi_in:
            print(f"Connected to {input_ports[selected_port_index]}...")

            # Start receiving and printing MIDI events
            for message in midi_in:
                print(f"Received: {message}")
                ws.send(f"Received: {message}")

    except KeyboardInterrupt:
        print("\nExiting...")
    except OSError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
