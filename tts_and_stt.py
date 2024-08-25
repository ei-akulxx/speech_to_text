import speech_recognition as sr
from googletrans import Translator
from langdetect import detect, DetectorFactory

# Ensure consistent language detection results
DetectorFactory.seed = 0

# Initialize Translator
translator = Translator()

# Function to translate text
def translate_text(text, src_language='hi', dest_language='en'):
    try:
        translated = translator.translate(text, src=src_language, dest=dest_language)
        return translated.text
    except Exception as e:
        print(f"Translation error: {e}")
        return text

# Function for Speech-to-Text and Conditional Translation
def speech_to_text_and_translate():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Please speak...")
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            print("Recognized speech: " + text)

            # Detect language of the recognized text
            detected_language = detect(text)
            print(f"Detected language: {detected_language}")

            # Translate text if it's in Hindi
            if detected_language == 'hi':
                translated_text = translate_text(text, src_language='hi', dest_language='en')
                print("Translated text in English: " + translated_text)
                return translated_text
            else:
                # For better accuracy, check if detected language is close to Hindi
                if detected_language in ['en', 'hi']:
                    return text
                else:
                    # Attempt to translate to English if not recognized correctly
                    translated_text = translate_text(text, src_language='auto', dest_language='en')
                    print("Translated text in English: " + translated_text)
                    return translated_text

        except sr.UnknownValueError:
            print("Could not understand the audio")
            return None
        except sr.RequestError as e:
            print(f"Error with the request: {e}")
            return None
        except Exception as e:
            print(f"Error in processing: {e}")
            return None

# Example usage
def main():
    final_output = speech_to_text_and_translate()
    if final_output:
        print(f"Final output: {final_output}")

if __name__ == "__main__":
    main()
