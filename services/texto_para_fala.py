import azure.cognitiveservices.speech as speechsdk
import os

# Credenciais da API
SUBSCRIPTION, REGION = os.environ.get('SPEECH_KEY'), os.environ.get('SPEECH_REGION')


class TextoParaFala():
    def __init__(self):
        self.speech_config = speechsdk.SpeechConfig(subscription=SUBSCRIPTION, region=REGION)
        self.speech_config.speech_synthesis_language = 'pt-BR'
        self.speech_config.speech_synthesis_voice_name = 'pt-BR-AntonioNeural'
        self.audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
        self.speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=self.speech_config, audio_config=self.audio_config)
    
    
    def falar(self, texto: str) -> None:
        
        speech_synthesis_result = self.speech_synthesizer.speak_text_async(texto).get()

        if speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_synthesis_result.cancellation_details
            raise Exception("Sintetização de fala cancelada: {}".format(cancellation_details.reason))