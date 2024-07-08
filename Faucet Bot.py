import requests
import time
import random

with open("output.txt", "w") as output_file:
    with open("discord.txt", "r") as file:
        lines = file.readlines()
    random_indices = list(range(len(lines)))
    random.shuffle(random_indices)
    for index in random_indices:
        line = lines[index]
        address, token = line.strip().split('\t')
        print(f"Processing address: {address}")
        for _ in range(random.choice([2, 3, 4])):
            payload = {
                "type": 2,
                "application_id": "1070744101433135174",
                "guild_id": "933959587462254612",
                "channel_id": "1070780355931541514",
                "session_id": "557706839551b6bb2be71e265e80ceea",
                "data": {
                    "version": "1070924903060099153",
                    "id": "1070924903060099152",
                    "guild_id": "933959587462254612",
                    "name": "faucet",
                    "type": 1,
                    "options": [
                        {
                            "type": 3,
                            "name": "address",
                            "value": f"{address}"
                        }
                    ]
                }
            }
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f"{token}",
            }
            try:
                response = requests.post("https://discord.com/api/v9/interactions", json=payload, headers=headers)

                if response.status_code == 200:
                    result = 'The interaction was successfully handled.'
                else:
                    result = f'Wystąpił błąd: {response.status_code} - {response.text}'
            except requests.exceptions.RequestException as e:
                result = f'HTTP query error occurred: {e}'
            print(result)
            output_file.write(f"{address}: {result}\n")
            time.sleep(random.choice([1.8, 1.7, 1.6, 1.9, 2.1]))
        time.sleep(2)
