#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-2021 Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from typing import Union

import pyrogram
from pyrogram import raw
from pyrogram.file_id import FileId, FileType, FileUniqueId, FileUniqueType, ThumbnailSource
from ..object import Object


class ChatPhoto(Object):
    """A chat photo.

    Parameters:
        file_id (``str``):
            Docs

        file_unique_id (``str``):
            Docs
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        file_id: str,
        file_unique_id: str,

    ):
        super().__init__(client)

        self.file_id = file_id
        self.file_unique_id = file_unique_id

    @staticmethod
    def _parse(
        client,
        chat_photo: Union["raw.types.UserProfilePhoto", "raw.types.ChatPhoto"],
        peer_id: int,
        peer_access_hash: int
    ):
        if not isinstance(chat_photo, (raw.types.UserProfilePhoto, raw.types.ChatPhoto)):
            return None

        return ChatPhoto(
            file_id=FileId(
                file_type=FileType.CHAT_PHOTO,
                dc_id=chat_photo.dc_id,
                media_id=chat_photo.photo_id,
                access_hash=0,
                thumbnail_source=ThumbnailSource.CHAT_PHOTO_BIG,
                chat_id=peer_id,
                chat_access_hash=peer_access_hash
            ).encode(),
            file_unique_id=FileUniqueId(
                file_unique_type=FileUniqueType.PHOTO,
                media_id=chat_photo.photo_id
            ).encode(),
            client=client
        )
