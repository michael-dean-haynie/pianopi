#!/usr/bin/env python3

import websocket
import rel
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import mido
import os
import threading
from dotenv import load_dotenv
import queue

""" GLOBAL VARIABLES """

midi_ports = {}
midi_ports_lock = threading.Lock()

midi_msg_queue = queue.Queue()

""" MIDI FUNCTIONS """


def listen_to_midi_port(midi_port):
    # with mido.open_input(port_name) as midi_port:
    with midi_port:
        for message in midi_port:
            midi_msg_queue.put(message)
            print(message, flush=True)


def list_midi_input_names():
    midi_ports_lock.acquire()
    print("Listing MIDI Inputs:", flush=True)
    input_names = mido.get_input_names()
    for index, name in enumerate(input_names, 1):
        print(f"{index}: {name}", flush=True)

        if name in midi_ports:
            print(f"MIDI port '{name}' already exists in midi_ports", flush=True)
            midi_port = midi_ports[name]
            print(f"MIDI port '{name}' is closed: {midi_port.closed}", flush=True)
            if midi_port.closed:
                print(f"Opening new MIDI port for '{name}'", flush=True)
                midi_ports[name] = mido.open_input(name)
                threading.Thread(target=listen_to_midi_port, args=[midi_port]).start()
        else:
            print(f"MIDI port '{name}' does not already exists in midi_ports", flush=True)
            print(f"Opening new MIDI port for '{name}'", flush=True)
            midi_port = mido.open_input(name)
            midi_ports[name] = midi_port
            threading.Thread(target=listen_to_midi_port, args=[midi_port]).start()

    dead_port_names = [name for name in midi_ports.keys() if name not in input_names]
    for port_name in dead_port_names:
        print(f"Existing MIDI '{port_name}' seems to have gone missing ...", flush=True)
        midi_ports[port_name].close()
        midi_ports.pop(port_name, None)

    midi_ports_lock.release()


""" WATCH DOG EVENT HANDLERS"""


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory:
            return
        print(f'File {event.src_path} has been modified.', flush=True)
        list_midi_input_names()


""" WEB SOCKET EVENT HANDLERS """


def on_message(ws, message):
    print(message)


def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("### closed ###")


def on_open(ws):
    print("Opened connection")
    threading.Thread(target=queue_consumer, args=[midi_msg_queue, ws]).run()


""" QUEUE CONSUMER """


def queue_consumer(q, web_soc):
    while True:
        item = q.get()
        web_soc.send(f"{item}")
        q.task_done()


if __name__ == "__main__":
    # testing
    # list_midi_input_names()

    # load environment variables
    env_file_path = "/etc/pianopi/.env"
    load_dotenv(dotenv_path=env_file_path)

    web_socket_url = os.getenv("WEB_SOCKET_URL")
    usb_event_file = os.getenv("USB_EVENT_FILE")

    print(f"WEB_SOCKET_URL is configured as '{web_socket_url}'", flush=True)
    print(f"USB_EVENT_FILE is configured as '{usb_event_file}'", flush=True)

    # watchdog for detecting midi devices
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, usb_event_file, recursive=True)
    observer.start()  # non-blocking

    # do initial midi port search/initialization
    list_midi_input_names()

    # Start up websocket app
    websocket.enableTrace(True)
    web_socket = websocket.WebSocketApp(web_socket_url,
                                        on_open=on_open,
                                        on_message=on_message,
                                        on_error=on_error,
                                        on_close=on_close)

    web_socket.run_forever(dispatcher=rel,
                           reconnect=5)  # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()  # blocking
