from fastapi import APIRouter

from schemas import (
    NotificationSchema,
    NotificationPreferenceSchema
)
from database import notifications_db
router = APIRouter()


# GET NOTIFICATIONS

@router.get("/notifications")
def get_notifications():

    return notifications_db


# CREATE NOTIFICATION

@router.post("/notifications")
def create_notification(
    notification: NotificationSchema
):

    notifications_db.append(
        notification.dict()
    )

    return {
        "message": "Notification created successfully",
        "notification": notification
    }


# GET PREFERENCES

@router.get("/notifications/preferences")
def get_preferences():

    return preferences_db


# UPDATE PREFERENCES

@router.post("/notifications/preferences")
def update_preferences(
    preference: NotificationPreferenceSchema
):

    preferences_db.append(
        preference.dict()
    )

    return {
        "message": "Preferences updated successfully",
        "preferences": preference
    }