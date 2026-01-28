import firebase_admin
from firebase_admin import credentials, firestore
import json
import os


# Firebase settings
KEY_PATH = "firebase-key.json"
PROJECT_ID = "dvc-news-37dcd"


def init_firebase():

    if not firebase_admin._apps:

        cred = credentials.Certificate(KEY_PATH)

        firebase_admin.initialize_app(cred, {
            "projectId": PROJECT_ID
        })


def upload_to_firestore():

    init_firebase()

    file_path = "data/news.json"

    if not os.path.exists(file_path):
        raise FileNotFoundError("data/news.json not found. Run fetch first.")

    # Load JSON
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    db = firestore.client()

    # Collection name
    collection_ref = db.collection("news_data")

    # Document ID = timestamp
    doc_id = data["fetched_at"].replace(":", "-")

    collection_ref.document(doc_id).set(data)

    print(f"Uploaded to Firestore: news_data/{doc_id}")


if __name__ == "__main__":
    upload_to_firestore()
