import requests
import time
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

delay = int(config['DISCORD']['delay'])
channel_id = int(config['DISCORD']['channel_id'])
user_agent = str(config['CHROME']['Useragent'])
auth = str(config['CHROME']['Authorization'])
picture = str(config['FILE']['picture'])
message = str(open('sale.txt', 'r', encoding='utf-8').read())

def get_data():
    headers = {
        'User-agent': user_agent,
        'Authorization': auth
    }

    json_data = {
    'content': message
    }
    
    pic = open(f"source/{picture}", 'rb')
    files = {
        "file" : (f"source/{picture}", pic)
    }

    response = requests.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", files=files, headers=headers, data=json_data)
    if response.json()['code'] == 20016:
        print('Waiting for delay')
        time.sleep(response.json())
    pic.close()
    
    return response.json()

def main():
    while True:
        print(get_data())
        time.sleep(delay)

if __name__ == "__main__":
    main()
