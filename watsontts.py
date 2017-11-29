# coding=utf-8
from kalliope.core.TTS.TTSModule import TTSModule, FailToLoadSoundFile
import logging
import json
from os.path import join, dirname
from watson_developer_cloud import TextToSpeechV1

logging.basicConfig()
logger = logging.getLogger("kalliope")

text_to_speech = TextToSpeechV1(
    username='',
    password='')

class Watsontts(TTSModule):
    def __init__(self, **kwargs):
        super(Watsontts, self).__init__(**kwargs)

    def say(self, words):
        """
        :param words: The sentence to say
        """

        self.generate_and_play(words, self._generate_audio_file)

    def _generate_audio_file(self):
        """
        Generic method used as a Callback in TTSModule
            - must provided the audio file and write it on the disk

        .. raises:: FailToLoadSoundFile
        """

        with open(join(dirname(__file__), self.file_path),
                  'wb') as audio_file:
            audio_file.write(
                text_to_speech.synthesize(
                    self.words, 
                    accept='audio/wav',
                    voice="fr-FR_ReneeVoice"
                )
            )
