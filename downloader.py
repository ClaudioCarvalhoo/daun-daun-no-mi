import os
import json
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

with open("image_urls.json", "r") as f:
    data = json.load(f)

chapter_start = 1
chapter_end = 1103
for chapter in range(chapter_start, chapter_end + 1):
    print(f"Chapter {chapter}")

    directory = f"./out/{chapter}"
    if not os.path.exists(directory):
         os.makedirs(directory) 

    for i, page_url in enumerate(data[str(chapter)]):
        print(f"Page {i+1}")

        res = requests.get(page_url, headers=headers)
        with open(f"{directory}/{i+1}.png", 'wb') as f:
                f.write(res.content)

    print("==============")
