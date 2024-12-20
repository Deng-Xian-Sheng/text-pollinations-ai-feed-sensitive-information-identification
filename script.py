from sseclient import SSEClient

def get_text_feed():
    url = 'https://text.pollinations.ai/feed'
    es = SSEClient(url)
    for event in es:
        if event.data:
            print(event.data)

if __name__ == '__main__':
    get_text_feed()
