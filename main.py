import json
from dotenv import load_dotenv
import os
import telebot
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import random
import gspread


def connect_mongo(uri):
    client = MongoClient(uri, server_api=ServerApi('1'))
    return client['telegram'], client


def get_random_document(collection):
    result = collection.find()
    data = list(result)
    return random.choice(data)


def set_message(document):
    if document['book']:
        return f"\n\n🔖\n\n{document['title']}\n\n" \
               f"{document['advice']}\n\n" \
               f"📖 Kitap: {document['book']}\n" \
               f"✏️ Yazar: {document['author']}\n" \
               f"📚 Yayınevi: {document['publisher']}\n\n👋\n\n"
    else:
        return f"\n\n📌\n\n{document['title']}\n\n" \
               f"{document['advice']}\n\n👋\n\n"


def send_message_to_gibi(bot_token, chat_id, message):
    bot = telebot.TeleBot(bot_token)
    bot.send_message(chat_id, message)
    bot.stop_bot()


def get_data_from_sheet(credentials_json, sheet_url):

    credentials_dict = json.loads(credentials_json)
    gc = gspread.service_account_from_dict(credentials_dict)
    sh = gc.open_by_url(sheet_url)
    worksheet = sh.sheet1
    return worksheet.get_all_values()


def add_data_to_database(collection, data):
    for row in data[1:]:
        column_3 = row[2]
        column_4 = row[3]
        column_6 = row[5]
        column_7 = row[6]
        column_8 = row[7]
        existing_document = collection.find_one({
            'title': column_3,
            'advice': column_4,
            'book': column_6,
            'author': column_7,
            'publisher': column_8
        })
        if not existing_document:
            new_document = {
                'title': column_3,
                'advice': column_4,
                'book': column_6,
                'author': column_7,
                'publisher': column_8
            }
            collection.insert_one(new_document)


def main():
    load_dotenv()
    sheet_url = os.getenv('SHEET_URL')
    bot_token = os.getenv('BOT_TOKEN')
    chat_id = os.getenv('CHAT_ID')
    uri = os.getenv('URI')
    credentials_json = os.getenv('CREDENTIALS')
    data = get_data_from_sheet(credentials_json, sheet_url)
    db, client = connect_mongo(uri)
    collection = db['advices']
    add_data_to_database(collection, data)
    collection = db['advices']
    random_document = get_random_document(collection)
    message = set_message(random_document)
    send_message_to_gibi(bot_token, chat_id, message)
    client.close()


if __name__ == '__main__':
    main()
