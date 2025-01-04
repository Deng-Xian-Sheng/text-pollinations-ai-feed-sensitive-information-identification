from sseclient import SSEClient

def get_text_feed():
    url = 'https://text.pollinations.ai/feed'
    es = SSEClient(url)
    for event in es:
        if event.data:
            import json
data = json.loads(event.data)
print(json.dumps(data, indent=4, ensure_ascii=False))

if __name__ == '__main__':
    get_text_feed()
