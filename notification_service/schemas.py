from pydantic import BaseModel


class NotificationSchema(BaseModel):

    user_id: int
    title: str
    message: str
    category: str
    is_read: str = "False"


class NotificationPreferenceSchema(BaseModel):

    user_id: int
    enable_sound: str
    enable_toast: str
    disabled_categories: str