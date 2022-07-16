import requests
from requests import HTTPError
from loader import vk_session


def get_audio_content(track_info=''):
    try:
        result = vk_session.method("audio.getById", {"audios": "{0}".format(track_info)})
    except:
        return

    url = result[0]["url"]
    try:
        response = requests.get(url=url)
        response.raise_for_status()
    except HTTPError as ex:
        return
    except Exception as ex:
        return

    if response.status_code != 200:
        return

    return response.content
