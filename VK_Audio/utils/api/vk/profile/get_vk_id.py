from urllib.parse import urlparse
from loader import vk_session


def is_vk_url(url='') -> bool:
    result = urlparse(url)
    return result.netloc == "vk.com"


def get_vk_id(url='') -> int:
    if not is_vk_url(url):
        return 0

    path = urlparse(url).path
    s_name = str(path)
    s_name = s_name.replace('/', '')

    try:
        result = vk_session.method('utils.resolveScreenName', {'screen_name': s_name})
    except:
        return 0
    return result["object_id"]
