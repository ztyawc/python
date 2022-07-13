import requests

cookies = {
    'PHPSESSID': '71rctjkqaiaiolrm7pf220danp',
    'wordpress_logged_in_420a9792b7082fc5c0fde63b2fa51820': 'ztyawc%7C1657876299%7COtlGhZMtgTBNGfbVsllDj2i4hkeeZucs2ueJNKMPXro%7Ce8687d62068482c332320ec2ec7b8d0493b241fc9249806240aa480819c75ced',
}

headers = {
    'authority': 'hualeshe.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'PHPSESSID=71rctjkqaiaiolrm7pf220danp; wordpress_logged_in_420a9792b7082fc5c0fde63b2fa51820=ztyawc%7C1657876299%7COtlGhZMtgTBNGfbVsllDj2i4hkeeZucs2ueJNKMPXro%7Ce8687d62068482c332320ec2ec7b8d0493b241fc9249806240aa480819c75ced',
    'referer': 'https://hualeshe.com/',
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
}

response = requests.get('https://hualeshe.com/user', cookies=cookies, headers=headers)
print(response.text)