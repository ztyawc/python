import requests

cookies = {
    'abtest': '20220715125057190_59',
    'unpl': 'JF8EAK5nNSttDUkBAElWHBNAS1xXW10LQkQBPDVVVl5fTgMGHwoSQhV7XlVdXhRKER9vYxRUXlNPVQ4bBSsiE0peUFxYD0MUC19XNVddaEpkBRwGHRsXSl9VW1gMSBcHamcHU1tYTlQ1KwITFiBLXFVcXg5KFQdrYgZTWWh7UQUaAx0bGEhfU25cOEonQgFnBFVaXEpdBlYCHBYWQlpVXFwNThMAb2MAVF9fTVQAGzIaIhM',
    'pt_pin': 'jd_wUgGKYgKKKDP',
    'pwdt_id': 'jd_wUgGKYgKKKDP',
    '__jdc': '122270672',
    '3AB9D23F7A4B3C9B': 'U56NU5GYF7JB47AELUHUYW3DTCEM4P2GO267BRJFJAKARF5MQAFW2X5VZR2BHHPHVXY2H6QMGBVSPAYN7CLIRG2AWA',
    'pt_key': 'app_openAAJi4oXFADCgcKX6h6uSBBJbTk1j97_Rx39dQ8Ce-dIi_kRCjvXvaKSz7Elan6uJw7XhXPBtfe0',
    'sid': 'f23d6057608d62369074c0fcab4ed44w',
    '__jda': '122270672.1657860671157937218595.1657860671.1658041701.1659012554.4',
    '__jdv': '122270672%7Ckong%7Ct_2025346929_%7Ctuiguang%7Cd3d4ce60a1024128b3bca3264f2598a4%7C1657860615429',
    'BATQW722QTLYVCRD': '{"tk":"jdd01CJILS5HLZF6TC4JGXJZRJNSMYMQFWDKUVYHYSPSFCUV4IHD6F4U43AWE32OJ44YITSDTSYOHQWOFVV2WZUDSXZZC3AFO426DIY62BBA01234567","t":1659012965746}',
    '_gia_s_local_fingerprint': '6c0452017f4cbb70b64b2c33aced322f',
    '_gia_s_e_joint': '{"eid":"U56NU5GYF7JB47AELUHUYW3DTCEM4P2GO267BRJFJAKARF5MQAFW2X5VZR2BHHPHVXY2H6QMGBVSPAYN7CLIRG2AWA","ma":"","im":"","os":"android","osv":"","ip":"183.200.191.229","apid":"jdapp","ia":"","uu":"","cv":"11.1.0","nt":"UNKNOW","at":"3"}',
    'wxa_level': '1',
    'shshshfpb': 'yDi-LzWeTDstk8lw87vsWRw',
    'joyytokem': 'babel_2XfoF4fZJt4yxh6NNwe9z6GPMVDSMDFGb2NIYTk5MQ==.d1lWcVF3XVp/UHJdUDY4cV4mAAd0BCIHH3dDVWRQal4deh93ER0=.f6838158',
    'cid': '8',
    'joyya': '1659013164.0.28.1gz59jd',
    'shshshfpv': 'JD012145b9e6MNlnUazl1659013160951053skZAjhky2sjHSVhPzuEYs8raIPNIPSycDV1tVOHQHDhLTO97MTj0TRscNz5KdGxEnACNdjfPybtxRp_9PA7EA0fz791s~xkjSzlCPBu8eVzymr1dfWMO9nGdVERaxDfPzsAD9HqIrBIk9F1-STU7b-c94dkmlC-PmlUBxtUkQCGmcklMZPLU8cw9H1Cc6ON75tp97kvId3gob3_nYsMSYjDVUPX1pKwVRwOwGO3irBZdEWkjKO6w',
    '__jdb': '122270672.9.1657860671157937218595|4.1659012554',
    'mba_sid': '460.30',
    'pre_session': 'WwxeHXfZr9Z8I1kifpc0VBgEeKIMy+9G|641',
    'pre_seq': '29',
    '__jd_ref_cls': 'Babel_dev_other_DDNC_Pot',
    'mba_muid': '16531225053981164197224.460.1659013318247',
}

headers = {
    'authority': 'api.m.jd.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'abtest=20220715125057190_59; unpl=JF8EAK5nNSttDUkBAElWHBNAS1xXW10LQkQBPDVVVl5fTgMGHwoSQhV7XlVdXhRKER9vYxRUXlNPVQ4bBSsiE0peUFxYD0MUC19XNVddaEpkBRwGHRsXSl9VW1gMSBcHamcHU1tYTlQ1KwITFiBLXFVcXg5KFQdrYgZTWWh7UQUaAx0bGEhfU25cOEonQgFnBFVaXEpdBlYCHBYWQlpVXFwNThMAb2MAVF9fTVQAGzIaIhM; pt_pin=jd_wUgGKYgKKKDP; pwdt_id=jd_wUgGKYgKKKDP; __jdc=122270672; 3AB9D23F7A4B3C9B=U56NU5GYF7JB47AELUHUYW3DTCEM4P2GO267BRJFJAKARF5MQAFW2X5VZR2BHHPHVXY2H6QMGBVSPAYN7CLIRG2AWA; pt_key=app_openAAJi4oXFADCgcKX6h6uSBBJbTk1j97_Rx39dQ8Ce-dIi_kRCjvXvaKSz7Elan6uJw7XhXPBtfe0; sid=f23d6057608d62369074c0fcab4ed44w; __jda=122270672.1657860671157937218595.1657860671.1658041701.1659012554.4; __jdv=122270672%7Ckong%7Ct_2025346929_%7Ctuiguang%7Cd3d4ce60a1024128b3bca3264f2598a4%7C1657860615429; BATQW722QTLYVCRD={"tk":"jdd01CJILS5HLZF6TC4JGXJZRJNSMYMQFWDKUVYHYSPSFCUV4IHD6F4U43AWE32OJ44YITSDTSYOHQWOFVV2WZUDSXZZC3AFO426DIY62BBA01234567","t":1659012965746}; _gia_s_local_fingerprint=6c0452017f4cbb70b64b2c33aced322f; _gia_s_e_joint={"eid":"U56NU5GYF7JB47AELUHUYW3DTCEM4P2GO267BRJFJAKARF5MQAFW2X5VZR2BHHPHVXY2H6QMGBVSPAYN7CLIRG2AWA","ma":"","im":"","os":"android","osv":"","ip":"183.200.191.229","apid":"jdapp","ia":"","uu":"","cv":"11.1.0","nt":"UNKNOW","at":"3"}; wxa_level=1; shshshfpb=yDi-LzWeTDstk8lw87vsWRw; joyytokem=babel_2XfoF4fZJt4yxh6NNwe9z6GPMVDSMDFGb2NIYTk5MQ==.d1lWcVF3XVp/UHJdUDY4cV4mAAd0BCIHH3dDVWRQal4deh93ER0=.f6838158; cid=8; joyya=1659013164.0.28.1gz59jd; shshshfpv=JD012145b9e6MNlnUazl1659013160951053skZAjhky2sjHSVhPzuEYs8raIPNIPSycDV1tVOHQHDhLTO97MTj0TRscNz5KdGxEnACNdjfPybtxRp_9PA7EA0fz791s~xkjSzlCPBu8eVzymr1dfWMO9nGdVERaxDfPzsAD9HqIrBIk9F1-STU7b-c94dkmlC-PmlUBxtUkQCGmcklMZPLU8cw9H1Cc6ON75tp97kvId3gob3_nYsMSYjDVUPX1pKwVRwOwGO3irBZdEWkjKO6w; __jdb=122270672.9.1657860671157937218595|4.1659012554; mba_sid=460.30; pre_session=WwxeHXfZr9Z8I1kifpc0VBgEeKIMy+9G|641; pre_seq=29; __jd_ref_cls=Babel_dev_other_DDNC_Pot; mba_muid=16531225053981164197224.460.1659013318247',
    'origin': 'https://carry.m.jd.com',
    'referer': 'https://carry.m.jd.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'jdapp;android;11.1.0;;;appBuild/98139;ef/1;ep/%7B%22hdid%22%3A%22JM9F1ywUPwflvMIpYPok0tt5k9kW4ArJEU3lfLhxBqw%3D%22%2C%22ts%22%3A1659013195219%2C%22ridx%22%3A-1%2C%22cipher%22%3A%7B%22sv%22%3A%22CJS%3D%22%2C%22ad%22%3A%22CJZwZJO4CQUnYWSzZNU0Zq%3D%3D%22%2C%22od%22%3A%22%22%2C%22ov%22%3A%22CzO%3D%22%2C%22ud%22%3A%22CJZwZJO4CQUnYWSzZNU0Zq%3D%3D%22%7D%2C%22ciphertype%22%3A5%2C%22version%22%3A%221.2.0%22%2C%22appname%22%3A%22com.jingdong.app.mall%22%7D;jdSupportDarkMode/0;Mozilla/5.0 (Linux; Android 12; M2012K11C Build/SQ1D.220205.004; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36',
    'x-requested-with': 'com.jingdong.app.mall',
}

response = requests.get('https://api.m.jd.com/client.action?functionId=waterGoodForFarm&body=%7B%22type%22%3A%22%22%2C%22version%22%3A17%2C%22channel%22%3A1%2C%22babelChannel%22%3A%22121%22%7D&appid=signed_wh5&area=6_309_311_32148&osVersion=12&screen=393*873&networkType=wifi&timestamp=1659013195652&d_brand=Redmi&d_model=M2012K11C&wqDefault=false&client=android&clientVersion=11.1.0&partner=google&build=98139&uuid=1363665613830356-1316263346534366&h5st=20220728210158264%3B5588190374281638%3B0c010%3Btk02w967c1b2d18n88d1oobliOV0IRinmFFkzRtJhYUAHk69JT0VTMh9GSryZll05QQb4w%2FHqFQaK1QtFF19k43UAqkI%3B3753c810327e7c14545c761935b901c98d2bb765d75f3a5bfa08e632515a92da%3B3.0%3B1659013318264', cookies=cookies, headers=headers)
print(response.json())