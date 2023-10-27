from telethon.sync import TelegramClient
import json

api_id = 'xxxxx' #conf info
api_hash = 'xxxxx' #conf info
phone_number = '+xxxxx'#conf info
session_name = 'xxxxx'#conf info
group_username = 'xxxxx'#conf info

def get_gender(first_name):
    if first_name and first_name[-1].lower() == 'a':
        return 'female'
    else:
        return 'male'

def get_group_members():
    with TelegramClient(session_name, api_id, api_hash) as client:
        group_entity = client.get_entity(group_username)
        participants = client.get_participants(group_entity)

        members_info = {}

        for participant in participants:
            username = participant.username
            name = participant.first_name
            last_name = participant.last_name
            gender = get_gender(name)
            members_info[username] = {
                "name": name,
                "last_name": last_name,
                "gender": gender
            }

        return members_info

def filter_and_write_to_files(members_info):
    male_file = open("male.txt", "w", encoding="utf-8")
    female_file = open("female.txt", "w", encoding="utf-8")

    for username, info in members_info.items():
        gender = info.get("gender", "unknown")
        if username:
            if gender == "male":
                male_file.write(username + "\n")
            elif gender == "female":
                female_file.write(username + "\n")

    male_file.close()
    female_file.close()


if __name__ == "__main__":
    members_info = get_group_members()
    with open("members_info.json", "w", encoding="utf-8") as json_file:
        json.dump(members_info, json_file, ensure_ascii=False, indent=2)

    filter_and_write_to_files(members_info)
