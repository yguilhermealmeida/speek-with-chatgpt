import os
import azure.cognitiveservices.speech as speechsdk


SUBSCRIPTION, REGION = os.environ.get('SPEECH_KEY'), os.environ.get('SPEECH_REGION')


class FalaParaTexto():
    def __init__(self) -> None:
        self.speech_config = speechsdk.SpeechConfig(subscription=SUBSCRIPTION, region=REGION)
        self.speech_config.speech_recognition_language="pt-BR"
        self.audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
        self.speech_recognizer = speechsdk.SpeechRecognizer(speech_config=self.speech_config, audio_config=self.audio_config)
        
    
    def ouvir(self) -> str:
        
        texto = ''
        
        print("Fale no microfone...")
        
        speech_recognition_result = self.speech_recognizer.recognize_once_async().get()

        if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
            print("Reconhecimento de fala: '{}'".format(speech_recognition_result.text))
            texto = speech_recognition_result.text
            
        elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
            raise Exception("Não foi possível relizaro reconhecimento de fala: {}".format(speech_recognition_result.no_match_details))
            
                        
        elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
            cancellation_details = speech_recognition_result.cancellation_details
            
            raise Exception("Reconhecimento de fala cancelado: {}".format(cancellation_details.reason))
            
        
        return texto    
            