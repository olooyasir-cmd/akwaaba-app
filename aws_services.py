import boto3
import io

rekognition = boto3.client('rekognition', region_name='us-east-1')
polly       = boto3.client('polly', region_name='us-east-1')
translate   = boto3.client('translate', region_name='us-east-1')

def detect_labels(image_bytes):
    """Returns top labels for an image with confidence scores."""
    response = rekognition.detect_labels(
        Image={'Bytes': image_bytes},
        MaxLabels=10,
        MinConfidence=70
    )
    return [(l['Name'], l['Confidence']) for l in response['Labels']]

def text_to_audio(text, voice='Aria', language='en-US'):
    """Converts text to MP3 audio using Polly."""
    # Voice mapping — different voices for different languages
    voice_map = {
        'English': ('Aria', 'en-US'),
        'French':  ('Lea', 'fr-FR'),
        'Spanish': ('Lupe', 'es-US'),
        'Mandarin': ('Zhiyu', 'cmn-CN'),
    }
    voice, lang = voice_map.get(language, ('Aria', 'en-US'))
    response = polly.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId=voice,
        Engine='neural',
        LanguageCode=lang
    )
    return response['AudioStream'].read()

def translate_text(text, target_lang='en'):
    """Translates text to target language."""
    lang_codes = {
        'French': 'fr', 'Spanish': 'es',
        'Mandarin': 'zh', 'Twi': 'tw'
    }
    if target_lang == 'English':
        return text
    target = lang_codes.get(target_lang, 'en')
    response = translate.translate_text(
        Text=text,
        SourceLanguageCode='en',
        TargetLanguageCode=target
    )
    return response['TranslatedText']