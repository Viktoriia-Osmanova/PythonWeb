from models import Quote, Author
from mongoengine import connect, disconnect
import json


connect()

def search_quotes(command):
    parts = command.split(':')
    if len(parts) != 2:
        return "Невірний формат команди. Спробуйте ще раз."

    action, value = parts[0].strip(), parts[1].strip()

    if action == "name":
        # Пошук цитат за ім'ям автора
        author = Author.objects(fullname__icontains=value).first()
        if author:
            quotes = Quote.objects(author=author)
            return format_quotes(quotes)
        else:
            return "Автор не знайдений."

    elif action == "tag":
    
        quotes = Quote.objects(tags__icontains=value)
        return format_quotes(quotes)

    elif action == "tags":
        
        tags = value.split(',')
        quotes = Quote.objects(tags__in=tags)
        return format_quotes(quotes)

    elif action == "exit":
       
        disconnect()
        exit()

    else:
        return "Невідома команда. Спробуйте ще раз."

def format_quotes(quotes):
    result = []
    for quote in quotes:
        result.append({
            "quote": quote.quote,
            "tags": quote.tags,
            "author": quote.author.fullname
        })
    return json.dumps(result, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    while True:
        command = input("Введіть команду: ")
        result = search_quotes(command)
        print(result)
