import time
import json
import sqlite3
import threading

locker = threading.Lock()


class DataBase:
    def __init__(self, db_file_path: str):
        self.connection = sqlite3.connect(db_file_path)
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()


    ''' Service '''
    def get_messages_id(self, chat_id: int):
        with locker:
            with self.connection:
                return self.cursor.execute("SELECT * FROM `messages_need_to_be_deleted` WHERE `chat_id` = ?", (chat_id, )).fetchall()

    def add_message_id(self, chat_id: int, message_id: int):
        with locker:
            with self.connection:
                return self.cursor.execute("REPLACE INTO `messages_need_to_be_deleted` ('chat_id', `message_id`) VALUES (?, ?)", (chat_id, message_id))

    def remove_message_id(self, _id: int):
        with locker:
            with self.connection:
                return self.cursor.execute("DELETE FROM `messages_need_to_be_deleted` WHERE `id` = ?", (_id, ))


    ''' Cache '''
    def save_cache(self, user_id: int, key: int, data: list):
        with locker:
            with self.connection:
                result = json.dumps(data)
                return self.cursor.execute("REPLACE INTO `cache` (`user_id`, `key`, `last_update`, `data`) VALUES (?, ?, ?, ?)", (user_id, key, int(time.time()), result))

    def load_cache(self, user_id: int, key: int):
        with locker:
            with self.connection:
                return self.cursor.execute("SELECT `last_update`, `data` FROM `cache` WHERE `user_id` = ? AND `key` = ?", (user_id, key)).fetchone()
    


    ''' PlayList '''
    def get_all_tracks(self, chat_id: int):
        with locker:
            with self.connection:
                return self.cursor.execute("SELECT `id`, `track_info` FROM `playlist` WHERE `chat_id` = ?", (chat_id, )).fetchall()

    def get_track_by_id(self, track_id: int):
        with locker:
            with self.connection:
                return self.cursor.execute("SELECT `track_info` FROM `playlist` WHERE `id` = ?", (track_id, )).fetchone()

    def user_has_tack_in_playlist(self, chat_id: int):
        pass
        # with self.connection:
        #     result = self.cursor.execute("SELECT * FROM `playlist` WHERE `chat_id` = ?", (user_id, )).fetchall()
        #     return bool(len(result)) 

    
    def add_track(self, chat_id: int, track_info: str):
        with locker:
            with self.connection:
                return self.cursor.execute("REPLACE INTO `playlist` (`chat_id`, `track_info`) VALUES (?, ?)", (chat_id, track_info))

    def remove_track(self, _id: int):
        with locker:
            with self.connection:
                return self.cursor.execute("DELETE FROM `playlist` WHERE `id` = ?", (_id, ))
