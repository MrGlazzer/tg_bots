from loader import vk_session


def from_profile(vk_id: int, offset: int, count: int) -> list:
    try:
        result = vk_session.method("audio.get", {"user_id": vk_id, "offset": offset, "count": count})
        return result["items"]
    except:
        pass
