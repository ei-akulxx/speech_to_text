const { speech_to_text_and_translate } = require('./speech-to-text-and-translate');

module.exports = {
  async handleEvent(event) {
    // Call the speech-to-text and translation function
    const finalOutput = await speech_to_text_and_translate();
    if (finalOutput) {
      // Return the translated text as a response
      return { text: finalOutput };
    } else {
      // Return an error message if the translation fails
      return { text: 'Error: Unable to translate text.' };
    }
  },
};
