from sseclient import SSEClient

def get_text_feed():
    url = 'https://text.pollinations.ai/feed'
    es = SSEClient(url)
    for event in es:
        if event.data:
            import json
data = json.loads(event.data)
# 定义敏感信息关键词\nsensitive_keywords = ["敏感关键词1", "敏感关键词2", "邮箱", "身份证号"]  # 请根据需要替换\n\n# 检查是否含有敏感信息\ndef validate_id_number(id_number):\n    pattern = r'^\d{17}[\\dX]$'\n    return bool(re.match(pattern, id_number))\n\n# 检查中国手机号\ndef validate_china_phone_number(phone_number):\n    pattern = r'^1[3-9]\\d{9}$'\n    return bool(re.match(pattern, phone_number))\n\n# 检查信用卡号（包括美国等）\ndef validate_credit_card(card_number):\n    pattern = r'^(?:4[0-9]{12}(?:[0-9]{3})? | 5[1-5][0-9]{14} | 3[47][0-9]{13} | 3(?:0[0-5]|[68][0-9])[0-9]{11} | 6(?:011|5[0-9]{2})[0-9]{12} | 7[0-9]{15})$'\n    return bool(re.match(pattern, card_number))\n\n# 检查所有敏感信息\ndef contains_sensitive_info(data):\n    if validate_id_number(data.get('id_number', '')) or \\\n       validate_china_phone_number(data.get('phone_number', '')) or \\\n       validate_credit_card(data.get('credit_card_number', '')):\n        return True\n    return False\n\n# 在接收到数据之后进行检查\nif contains_sensitive_info(data['response']):\n    print("警告：检测到敏感信息！")\nelse:\n    print(json.dumps(data, indent=4, ensure_ascii=False))\n

if __name__ == '__main__':
    get_text_feed()
