#!/usr/bin/env python3

import mido

def list_midi_devices():
    print("Available MIDI devices:")
    for device in mido.get_input_names():
        print(device)

def main():
    # List available MIDI devices
    list_midi_devices()

    # Prompt the user to select a MIDI device
    selected_device = input("Enter the name of the MIDI device you want to use: ")

    try:
        # Open the selected MIDI input port
        with mido.open_input(selected_device) as midi_in:
            print(f"Connected to {selected_device}...")

            # Start receiving and printing MIDI messages
            for message in midi_in:
                print(f"Received: {message}")

    except KeyboardInterrupt:
        print("\nExiting...")
    except OSError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
