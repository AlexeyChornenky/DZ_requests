import requests
import json

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {'Content-Type': 'application/json',
                'Authorization': f'OAuth {self.token}'}

    def upload(self, file_path):
        headers = self.get_headers()
        url = 'https://cloud-api.yandex.net/v1/disk/resources'
        res = requests.get(f'{url}/upload?path={path_to_file}&overwrite=True', headers=headers).json()
        with open(path_to_file, 'rb') as file:
            requests.put(res['href'], files={'file': file})


if __name__ == '__main__':
    path_to_file = r'\Users\Banan\Desktop\config_mikrotik_home.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)