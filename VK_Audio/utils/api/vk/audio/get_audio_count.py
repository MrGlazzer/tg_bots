from loader import vk_session


def get_audio_count(vk_id: int) -> int:
    try:
        result = vk_session.method("audio.get", {"user_id": vk_id, "offset": 0, "count": 1})
    except:
        return 0

    return result["count"]
