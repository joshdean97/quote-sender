import boto3
import random
import os
from dotenv import load_dotenv
import json

load_dotenv()

sns = boto3.client("sns", region_name="us-east-1")

TOPIC_ARN = os.getenv("SNS_TOPIC_ARN")


try:
    with open("quotes.json", "r", encoding="utf-8") as file:
        QUOTES = json.load(file)
except FileNotFoundError:
    print("Error: quotes.json file not found.")
    QUOTES = []


def send_daily_quote():
    quote = random.choice(QUOTES)

    response = sns.publish(
        TopicArn=TOPIC_ARN,
        Message=f'"{quote['Quote']}" - {quote['Author']}',
        Subject="✨Your Daily Quote",
    )
    print(f"Sent Quote: {quote}")
    print(f"SNS response: {response}")


quote = random.choice(QUOTES)

if __name__ == "__main__":
    send_daily_quote()
# print(f'"{quote["Quote"]}" — {quote["Author"]}')
