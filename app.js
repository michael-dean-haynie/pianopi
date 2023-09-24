/////////////////////// keep process running
(function wait () {
    setTimeout(wait, 1000);
})();
/////////////////////////////// end keep process running

const { WebMidi } = require("webmidi")

console.log('Hello from Pianopi!')

// WebMidi
//     .enable()
//     .then(onEnabled)
//     .catch(err => alert(err));
//
// function onEnabled() {
//     // Inputs
//     WebMidi.inputs.forEach(input => console.log(input.manufacturer, input.name));
//
//     // Outputs
//     WebMidi.outputs.forEach(output => console.log(output.manufacturer, output.name));
// }

WebMidi.addListener('midiaccessgranted', event => {
    console.log(event.type)
})
WebMidi.addListener('connected', event => {
    console.log(event.type)
})
WebMidi.addListener('enabled', event => {
    console.log(event.type)
})

WebMidi.enable();
