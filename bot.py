

import requests

from  config import TOKEN

TG_BOT_URL = f'https://api.telegram.org/bot{TOKEN}'


def get_updates(offset: int | None, limit: int = 100):
    url = f'{TG_BOT_URL}/getUpdates'
    params = {
        'offset': offset,
        'limit': limit
    }
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        
        
        return response.json()['result']
    
    
def send_message(chat_id: int | str, text: str):
    url = f'{TG_BOT_URL}/sendMessage'
    params = {
        'chat_id': chat_id,
        'text': text
    }
    requests.get(url, params=params)
    
def send_photo(chat_id: int | str, photo: str):
    url = f'{TG_BOT_URL}/sendPhoto'
    params = {
        'chat_id': chat_id,
        'photo': photo
    }
    requests.get(url, params=params)

def send_video(chat_id: int | str, video: str):
    url = f'{TG_BOT_URL}/sendVideo'
    params = {
        'chat_id': chat_id,
        'video': video
    }
    requests.get(url, params=params)


def send_location(chat_id: int | str, latitude: float, longitude: float):
    url = f'{TG_BOT_URL}/sendLocation'
    params = {
        'chat_id': chat_id,
        'latitude': latitude,
        'longitude': longitude,
    }
    requests.get(url, params=params)


def send_dice_with_emoji(chat_id: int | str, emoji: str):
    url = f'{TG_BOT_URL}/sendDice'
    params = {
        'chat_id': chat_id,
        'emoji': emoji 
    }
    requests.get(url, params=params)

def send_stiker(chat_id: int | str, stiker: str):
    url = f'{TG_BOT_URL}/sendSticker'
    params = {
        'chat_id': chat_id,
        'stiker': stiker  
    }
    requests.get(url, params=params)

def send_audio(chat_id: int | str, audio: str):
    url = f'{TG_BOT_URL}/sendAudio'
    params = {
        'chat_id': chat_id,
        'audio': audio 
    }
    requests.get(url, params=params)

def send_voice(chat_id: int | str, voice: str):
    url = f'{TG_BOT_URL}/sendVoice'
    params = {
        'chat_id': chat_id,
        'voice' : voice
    }
    requests.get(url, params=params)

def send_document(chat_id: int | str, document: str):
    url = f'{TG_BOT_URL}/sendDocument'
    params = {
        'chat_id': chat_id,
        'document' : document
    }
    requests.get(url, params=params)
def send_contact(chat_id: int | str, phone_number: str, first_name:str, last_name:str):
    url = f'{TG_BOT_URL}/sendContact'
    params = {
        'chat_id': chat_id,
        'first_name': first_name,
        'last_name': last_name,
        'phone_number': phone_number
        
    }
    requests.get(url, params=params)

def main():
    offset = None
    limit = 100

    while True:
        for update in get_updates(offset, limit):
            chat_id = update['message']['chat']['id']

            if 'text' in update['message']:
                text = update['message']['text']
                if text == '/start':
        
                    text = 'salom, ECO botga xush kelibsiz!'

                send_message(chat_id, text)
            elif 'photo' in update['message']:
                photo = update['message']['photo'][-1]
                send_photo(chat_id, photo['file_id'])
            elif 'location' in update['message']:
                location = update['message']['location']
                send_location(chat_id, location['latitude'], location['longitude'])
            elif 'video' in update['message']:
                video = update['message']['video']
                send_video(chat_id, video['file_id'])
            elif 'contact' in update['message']:
                contact = update['message']['contact']
                phone_number = contact.get('phone_number')
                first_name = contact.get('first_name')
                last_name = contact.get('last_name', "")
                send_contact(chat_id, phone_number, first_name, last_name)
            elif 'dice' in update['message']:
                dice = update['message']['dice']
                emoji = dice['emoji']  
                send_dice_with_emoji(chat_id, emoji)
            elif 'stiker' in update['message']:
                stiker = update['message']
                stiker2= stiker['stiker']  
                send_stiker(chat_id, stiker2)
            elif 'audio' in update['message']:
                audio = update['message']['audio']
                file_id = audio['file_id']
                send_audio(chat_id, file_id)
            elif 'voice' in update['message']:
                voice= update['message']['voice']
                file_id = voice['file_id']
                send_voice(chat_id, file_id)
            elif 'document' in update['message']:
                document= update['message']['document']
                file_id = document['file_id']
                send_document(chat_id, file_id)
            
            offset = update['update_id'] + 1




main()
