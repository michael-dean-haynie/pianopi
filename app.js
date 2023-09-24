/////////////////////// keep process running
(function wait () {
    setTimeout(wait, 1000);
})();
/////////////////////////////// end keep process running

const { WebMidi } = require("webmidi")

console.log('Hello from Pianopi!')

const { WebMidi: webmidi } = require('webmidi');

webmidi.enable((err) => {
    if (err) {
        console.error('WebMidi could not be enabled:', err);
    } else {
        console.log('WebMidi enabled!');

        // Register a listener for the "connected" event after enabling
        webmidi.addListener('connected', (e) => {
            console.log('MIDI device connected:', e);
        });

        // List available MIDI inputs
        console.log('Available inputs:');
        webmidi.inputs.forEach((input) => {
            console.log(input.name);
        });
        if (!webmidi.inputs.length) {
            console.log("No inputs found.")
        }
    }
});
