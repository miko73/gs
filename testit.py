from google.cloud import speech_v1 as speech

# set GOOGLE_APPLICATION_CREDENTIALS=C:\Users\micha\Projects\google_speech\speech-test-300122-d4f7f5f35fc7.json

def speech_to_text(config, audio):
    client = speech.SpeechClient()
    response = client.recognize(config=config, audio=audio)
    print_sentences(response)


def print_sentences(response):
    for result in response.results:
        best_alternative = result.alternatives[0]
        transcript = best_alternative.transcript
        confidence = best_alternative.confidence
        print("-" * 80)
        print(f"Transcript: {transcript}")
        print(f"Confidence: {confidence:.0%}")


config = dict(language_code="en-US")
audio = dict(uri="gs://cloud-samples-data/speech/brooklyn_bridge.flac")

config.update(dict(enable_automatic_punctuation=True))

speech_to_text(config, audio)
# print_sentences("Hi how are you there ?")