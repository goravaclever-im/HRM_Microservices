class Notification:

    def __init__(
        self,
        user_id,
        title,
        message,
        category,
        is_read
    ):

        self.user_id = user_id
        self.title = title
        self.message = message
        self.category = category
        self.is_read = is_read


class NotificationPreference:

    def __init__(
        self,
        user_id,
        enable_sound,
        enable_toast,
        disabled_categories
    ):

        self.user_id = user_id
        self.enable_sound = enable_sound
        self.enable_toast = enable_toast
        self.disabled_categories = disabled_categories