import requests


# 1. Поиск тура при вводе в запрос номера departureCityId города вылета,
#  который есть в списке вкладки "Откуда", например: из Мурманска в Абхазию


def test_positive_search_tour1():
    url = "https://fstravel.com/searchtour/country/europe/"
    "russia?departureCityId=708868&arrivalCountryId=210357"
    "&minStartDate=2025-11-03&maxStartDate=2025-11-03&minNightsCount=7"
    "&maxNightsCount=7&adults=2&flightTypes=all"

    payload = {}
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;'
        'q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/'
        'signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'priority': 'u=0, i',
        'referer': 'https://fstravel.com/searchtour',
        'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8",'
        ' "Chromium";v="141"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)'
        ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
        '141.0.0.0 Mobile Safari/537.36',
        'Cookie': 'spid=1759945933331_3525d277eb1a4dc4e01874b9310c1ae2_i77mh1'
        'scah4h6wh5; __ddg1_=goFa24s6VCc0XIeMxkF7;'
        ' _ga=GA1.1.422080909.1759945935; adrcid=AUJVUtkKWnNkh1SgaTgVDjw;'
        'flocktory-uuid=6cce39d7-d616-4f25-866c-694873d07482-5;'
        ' _ymab_param=i2F1e-pEE4ul20Huet8XPoYx8WtIy1fymYEy4NbvnOhAfe7'
        'OOU_mldljzvEonEP6s0KqoRmoONG37Gja4pf6NPizIKU;'
        ' _ym_uid=175994593610628113; _ym_d=1759945936;'
        'tmr_lvid=572dc590a568b50263e90859e4f396bd;'
        ' tmr_lvidTS=1759945935881; popmechanic_sbjs_migrations=pop'
        'mechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7'
        'C%7C1471519752605%3D1; _ct=1700000000423386978;'
        '_ct_client_global_id=9dc8d198-a5c9-5510-80a4-d17167669ef9;'
        'rai=b8cc547af6e96ad7188b9890915536ca;'
        'advcake_track_id=b1281536-227f-47a7-3f9c-ae13a27d1f1d;'
        'advcake_session_id=a907d419-5daf-3fea-7608-4f69ecd'
        '86830; r2UserId=1759945946866477; uxs_uid=8d66b910-a'
        '46f-11f0-b95a-893caab4cf73; has_action=true;'
        'analytic_id=1759945946972488; mindboxDeviceUUID=0c'
        'e09a14-8a7c-4de6-a1cb-498b257cc557;'
        'directCrm-session=%7B%22deviceGuid%22%3A%220ce09'
        'a14-8a7c-4de6-a1cb-498b257cc557%22%7D; acs_3=%7'
        'B%22hash%22%3A%221aa3f9523ee6c2690cb34fc702d414'
        '3056487c0d%22%2C%22nst%22%3A1760970765084%2C%22'
        'sl%22%3A%7B%22224%22%3A1760884365084%2C%221228%2'
        '2%3A1760884365084%7D%7D; domain_sid=7RDOPdKftNZ'
        'l87aKOMk3h%3A1760884365541; token_type_fs=Bearer;'
        'access_token_fs=eyJhbGciOiJSUzI1NiIsImtpZCI6Ij'
        'U4MUNCNTNGRUE1RDg1MjI3QjA2MDU2MEMzMEYxRDkwNTl'
        'EQkNBMEEiLCJ4NXQiOiJXQnkxUC1wZGhTSjdCZ1Znd3c4'
        'ZGtGbmJ5Z28iLCJ0eXAiOiJhdCtqd3QifQ.eyJpc3MiOiJ'
        'odHRwczovL2F1dGgyLmZzdHJhdmVsLmNvbS8iLCJleHAiO'
        'jE3NjExNDM2MDcsImlhdCI6MTc2MDg4NDQwNywiYXVkIjo'
        'id2ViYXBpIiwic2NvcGUiOiJwcm9maWxlIGVtYWlsIHJvb'
        'GVzIG9mZmxpbmVfYWNjZXNzIHBob25lIHdlYmFwaSIsImp'
        '0aSI6IjhlMjY1YjQ1LTM1ZGEtNDUxZC1iNjdhLWNjNzNlM'
        'mRhZDcxMSIsInN1YiI6ImE3MWJkZDAzLTEwNWUtNDFiMy0'
        '5ZTcxLTZlNzJmMGZiZGVkYiIsInBob25lX251bWJlciI6I'
        'is3OTYwMjE0MzA5MiIsImVtYWlsIjoidjY3ODcwOTk1QGd'
        'tYWlsLmNvbSIsInJvbGUiOiJVc2VyIiwiYnV5ZXJJZCI6M'
        'jA0MTQ3Niwib2lfYXVfaWQiOiJlZTA0ZGVlMy03ZjhhLTQ'
        '3ZGMtYWY5My0zOGRlOThmMWYzODciLCJvaV9wcnN0IjoiY'
                            'jJjLnB1YmxpYy5jbGllbnQiLCJjbGllbnRfaWQiOiJiMm'
                            'MucHVibGljLmNsaWVudCIsIm9pX3Rrbl9pZCI6ImY0NTg'
                            '2ZjY1LWRiNWItNDY0Zi1hMTFlLTlkZTk1MGFmZTllYSJ9.'
                            'HQA3wVKMIxXDqGQQHUaPnREnFc8JyIizR4vrTcnSNZt66X'
                            'AX6rUf6_QRxbcZhAQOlqIjeEalLp1YxDLsVwmasdFpFaK'
                            'KqfF3R-fQ3OCt-PqKZ2HrzqnzrBogh_CYZ47kTKBMhZR'
                            'N-yN1-wR01J-SUWMMV5Z2aQ-7dVFqlo6JclpK4pmsx8O9g'
                            'iqU6V7mUpJ47u8V-N49Xc97Huzb4qCXkZsfHjcPiDbY0CZ'
                            'UYlFZK6T7b-SQg9fZrtLoMb0xn8EYxHh3M0z2C_4FG9Oio'
                            'rkovYUE9IrBe3lHAxwrIHDmNBGHS5BFD2Drtyr3wlOs7Ch'
                            'H-R9rDRKJeeVlOxfX4ZXLxg; PHPSESSID=4sn4umcse0u'
                            'k9fe58j60lmhb1a; adrdel=1760955002437;'
                            'spjs=1760957653533_3d50de78_0135012e_40b95c8'
                            '4684529b694db00fac7c6ba97_34uIDmbS4jcN2KlszbB'
                            'SulzbBgtIn/4TSla3elM9rTGYVSXY4Bx9ECdTsldvmvuep'
                            'tIg352J6Twm08N3T2S0jdDcDeFZBWB8MrvuUioCh/uGejh'
                            '8lKVwpJjLJL4Us1E43WgpjUTyYGap1CQ4ZS2N0enVZopX3'
                            'gsCm0enbhMd2KyRMKGlyPlZWFOygTXNGei/JlM8ZZ3ENHi'
                            'Ezfgx3FbzivI+X6OOhzcrfL2NXCFEgbCd3gv71uLiQxqOz'
                            'l9CPJzwiFS1+ZT4SCQqRsZ6Z1+/MxsHUJMfm2l7E9Kj2f4'
                            '5Y70k99QiOz7++sXNXCGoFOQ/9MjLtz7iVz3lnq9jSvDgB'
                            'YotvB2l0dAxjrrr70EH57JKDVGt5yn4cfmFlQihLo+zDeG'
                            'hvBRerjbBRRUlS2y8iDCgs/H7Hk/L0oJTZw8FBLlgXc3wz'
                            '6BwXBb7P4IaJ5Zbsz4Lv0cSY/WuKip/HZAJ5myJKPTDYmx'
                            'n+PfyDdX93ZErhoWu5s+4FFn0818Szs7up3QFp+7MPNzQh'
                            'JBVa04MvIDzP3PKtxJNlDjohT0kRW33q9qGDsZgDoj9Xak'
                            'WslZQeRnd6DG2RyPqmQj4cpjJRV3AcC/i3u4jCYAFWcE67'
                            'LYpJzDEnIh4LEWRgTVdSsqephJj5++7ey8k36jQy7bROQE/'
                            'DdKq12U7oN+MBT6FBfF4LBlepYHw1Q86rV2WA6Omb1rEiP'
                            'AMbdB5oiZ/4mmr5r/iYg/IvHyEcSVVAYlI7ihgYMl129BJL'
                            'YRfD3yEN7a4iX8++GqHRr8w/Y3xWDSkOJFcOn4Fk2G3DP9'
                            'q3nYB4bSEyRrdpIBQJCvXtzsDDv6imlYF2YG9TSELJNbZIB'
                            'v7v7dDIvb+qloONdGhRU0o6Ly0YCzSixeWO4NeXHLItUdqE'
                            'l5f4+uXN7s8e2uvRxrhR9VQi140EXOXbFd4zcQdz4ObRzRa'
                            'Ah5vMghVp3lDnO+wi1QgV48baj8C0qb2SxnamCXz4HWdmEm'
                            '8Ed798ngWxTqGXilxzJVgmVf7/qVtReOxD1wq+UfKYiYFWb'
                            'l0RQDRvhzKBjtjSzhkLCGgKLbLGoe/olXY57s9kHTxdTHZb'
                            'H38Cp3OCjJmlsL7ILPR3LYXM4P+JPKrHmaYDt3/0F/S8l7H'
                            'ah3owcG0MChMfGlhgMPVArlp9eTBuo6qY+UrSxyq8AWp2gY'
                            '+YpLO9yS3d7/kFEB4rN0JPovKjoRQoPSdGOS/dlAt+1sDS6'
                            'sT//7SHIMC/9ecDPFoEhJu7Qi4WYAQwrcmWjl95LBVQ/ou3'
                            'roWG3lVubUkflR5KGTLRABtVfiYdNpWp2Eo3T39xNY0kQhP'
                            'KzinwyWgSNpsSyXIqfXdIdS4AVmu8sqWZnpkz57iTFV0kdl'
                            'sacqFgXAxauxaKLYS57O5q3IIwV1rcD6VtWjQPSjH33GSb4'
                            'KZGmYjp2HXKmy8mjDFY9fOCup+UsPDd2oBgejlOT2xycXwb'
                            'GLbnjdqV/Lu00oYmZUboySuWrpuVgHxpZ1NjixGgUE0g9+'
                            'odLPv4W73pgRw3tBtICnULHBPFBtOjK1vNo8TE4WV4AHFwd'
                            'NxJ7swrvxwteUbyY51MpVV2vm+HRewGhFnGG9bmn92kva+v'
                            'w8mDdAxwbUN2Kn8Rh/tM413hiTIJhpzWuaczWeQ4yTdXDzf'
                            'B6M4CtbVoTIYGe; _ym_isad=2; _ym_visorc=b;'
                            'is_role_agent=false; cted=modId%3Dop885zi2%3Bc'
                            'lient_id%3D422080909.1759945935%3Bya_client_id'
                            '%3D175994593610628113; _ct_ids=op885zi2%3A4283'
                            '1%3A653446908; _ct_session_id=653446908;'
                            '_ct_site_id=42831; advcake_track_url=%3D20250'
                            'and113np58QnHo45qG8dw96qXpqzuwQGJ3r1fxZBArUZS'
                            '0lkpGDxM3KBF4G7PKdJG8LpDxUAuALjWXJY9cw0dJyAf1'
                            'w8%2FVvNmekgj9%2F%2Bjk1RVpndXJ4AqPZy%2FNTJPxV'
                            'MDgudkBiQmWsgErsdZXOcDyfzeoHVW09DcBc%2B5Cglsf'
                            'ifV4dW%2BlVyHQOFIQbnout53R1a9yP5mE2BsohYxsAhA'
                            'AOBlvyBBoOMOAkVXtK9Re9rWgechz7QB0doJXXMymsd4U'
                            'CKT6H6xwvPHQXd3iw4KMxr5ZPKhnqt274%2BGBObI%2Fw'
                            'FUbpn1Pc5tNopQIzLhjtd8GkpPGPlxO520iY9UfL9stHp'
                            '2dumC07MJUNCnMSOqIvl%2FQEmtJ17q7ib%2BaIx5nx%2'
                            'BcRTcNsaNNksJ1zDOOMa2ADZ%2B9zZ3inFwMyQCbARt0p'
                            '7CPGP1wUQT8gAWI1eqhoUPm%2F4CmHetx5Ov29Iw5rZgE'
                            '%2FwKhipo%2FrmlPbQxbZROQZo4Hq5KOxzWe%2F9krZUK'
                            'd9XIPH4U1X1BtcMzRLRU6lpBqvhF6qnXfkyBt34cOrai5'
                            'gONAxYpOZ73uJABvO3UuTDqhhw26BcK59QRV0szfTS085'
                            '9vmvqwYOFtj3P%2B1Woki596DGvEI4zv9TteIqjREw8hF'
                            'si2eJNvZh%2FC5hWN%2BzGPEiwIzhHx7LgW9ArheqNLwj'
                            'Yj2UWydLpgosELytzZ8%3D; spsc=1760959185660_c0'
                            'a28a0bd79f49f28bc300fa131a9033_s-y2Tn3GPvkUUK'
                            'h2Ny8ASkAggjVUUbJFt7WKVx4eVRoZ; PageNumber=3;'
                            'XSRF-TOKEN=eyJpdiI6InlwdnI2SVA2aGxTSTBKY3BWV'
                            'nFCNEE9PSIsInZhbHVlIjoiRU9iVzhhQ1J5TVdnOExsO'
                            'WM3M2hBTmlaTEc2NTNEMGYrQnhjOVh6bVdkRmVxUGd0Y'
                            'UZlV0hDczRsWk5QVWxvM3VIYkVHZFlJMzJFWkcyZEErQ'
                            '1FXYlBZUFZTcTM4K3hDQ29WQ1NId1E2MXRSOTRiVDJYO'
                            'XNDTWY4SUFhdFY5QlYiLCJtYWMiOiI5MmE0YmU3YWFjNG'
                            'JjZWQ2ZjlmOTFhMTU1NTI4MjVmNDViYmI2MTk0ZDcwYz'
                            'kwYmFhNTlkYmQyNjRlNDA1NDMxIn0%3D;'
                            'funsan_session=eyJpdiI6ImdlQ045UEpYWmJYRzBW'
                            'OTQrYUpiN1E9PSIsInZhbHVlIjoick85QVlxaXBkQ2g'
                            'wQkZlNWJOT204TWZ3MDFTOVhqRFovS2x4cFhIamIzL2'
                            'xlTmxnQWUrMEVIRHJNOVlVU295TWtXMEdOTFdSVDJHO'
                            'XJHUUNZV21UcUJ2cEpVLzlPTklqV0R6THVSVDduTzFW'
                            'V0VGNmxrcXRPVDdSbXBvZUt0Y3AiLCJtYWMiOiI3NTh'
                            'iNzk2Yzk4NWQ0ZmIwYzFlMDk2MWNmYzZiOTUwYjI5YW'
                            'M2ZDJmOGEyZDdiMWVjMGI3YWJmN2ZiMTQ0NWNiIn0%3D;'
                            '_spx=eyJpZCI6Ijg1ODIwNDAyLTczZjgtNDc1Yy05'
                            'NTg5LWU5ZWM2NGU5MzJlOSIsInNvdXJjZSI6IiIsI'
                            'mZpeGVkIjp7InN0YWNrIjpbMCwwLDAsMF19fQ%3D%3D;'
                            'call_s=___op885zi2.1760960987.653446908.'
                            '241285:745570|2___; tmr_detect=0%7C17609591'
                            '89723; _ga_GJ17DPCPJY=GS2.1.s1760957658$o16'
                            '$g1$t1760959197$j16$l0$h0'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)


# 2. Поиск тура при вводе в запрос номера arrivalCountryId страны,
#  которая есть в списке стран вкладки "Куда", например: "Турция"

def test_positive_search_tour2():
    url = "https://fstravel.com/searchtour/country/europe/"
    "russia?departureCityId=708868&arrivalCountryId=210357"
    "&minStartDate=2025-11-03&maxStartDate=2025-11-03"
    "&minNightsCount=7&maxNightsCount=7&adults=2&flightTypes=all"

    payload = {}
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;'
        'q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/'
        'signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'referer': 'https://fstravel.com/searchtour',
        'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8",'
        ' "Chromium";v="141"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)'
        ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Mobile'
        ' Safari/537.36',
        'Cookie': 'is_role_agent=false; spid=1759945933331_3525d277eb1a4dc4e'
        '01874b9310c1ae2_i77mh1scah4h6wh5; __ddg1_=goFa24s6VCc0XIeMxkF7;'
        '_ga=GA1.1.422080909.1759945935; adrcid=AUJVUtkKWnNkh1SgaTgVDjw;'
        'flocktory-uuid=6cce39d7-d616-4f25-866c-694873d07482-5;'
        ' _ymab_param=i2F1e-pEE4ul20Huet8XPoYx8WtIy1fymYEy4NbvnOhAfe7OOU'
        '_mldljzvEonEP6s0KqoRmoONG37Gja4pf6NPizIKU; _ym_uid=175994593610'
        '628113; _ym_d=1759945936; tmr_lvid=572dc590a568b50263e90859e4f3'
        '96bd; tmr_lvidTS=1759945935881; popmechanic_sbjs_migrations=pop'
        'mechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C14'
        '71519752605%3D1; _ct=1700000000423386978;'
        '_ct_client_global_id=9dc8d198-a5c9-5510-80a4-d17167669ef9;'
        'rai=b8cc547af6e96ad7188b9890915536ca;'
        'advcake_track_id=b1281536-227f-47a7-3f9c-ae13a27d1f1d;'
        'advcake_session_id=a907d419-5daf-3fea-7608-4f69ecd86830;'
        'r2UserId=1759945946866477; uxs_uid=8d66b910-a46f-11f0-b95a-893ca'
        'ab4cf73; has_action=true; analytic_id=1759945946972488;'
        'mindboxDeviceUUID=0ce09a14-8a7c-4de6-a1cb-498b257cc557;'
        'directCrm-session=%7B%22deviceGuid%22%3A%220ce09a14-8a7c-4de6-a1'
        'cb-498b257cc557%22%7D; acs_3=%7B%22hash%22%3A%221aa3f9523ee6c269'
        '0cb34fc702d4143056487c0d%22%2C%22nst%22%3A1760970765084%2C%22sl%22%'
        '3A%7B%22224%22%3A1760884365084%2C%221228%22%3A1760884365084%7D%7D;'
        'domain_sid=7RDOPdKftNZl87aKOMk3h%3A1760884365541;'
        'token_type_fs=Bearer; access_token_fs=eyJhbGciOiJSUzI1NiIsImtpZCI6I'
        'jU4MUNCNTNGRUE1RDg1MjI3QjA2MDU2MEMzMEYxRDkwNTlEQkNBMEEiLCJ4NXQiOiJX'
        'QnkxUC1wZGhTSjdCZ1Znd3c4ZGtGbmJ5Z28iLCJ0eXAiOiJhdCtqd3QifQ.eyJpc3Mi'
        'OiJodHRwczovL2F1dGgyLmZzdHJhdmVsLmNvbS8iLCJleHAiOjE3NjExNDM2MDcsIml'
        'hdCI6MTc2MDg4NDQwNywiYXVkIjoid2ViYXBpIiwic2NvcGUiOiJwcm9maWxlIGVtY'
        'WlsIHJvbGVzIG9mZmxpbmVfYWNjZXNzIHBob25lIHdlYmFwaSIsImp0aSI6IjhlMjY'
        '1YjQ1LTM1ZGEtNDUxZC1iNjdhLWNjNzNlMmRhZDcxMSIsInN1YiI6ImE3MWJkZDAzL'
        'TEwNWUtNDFiMy05ZTcxLTZlNzJmMGZiZGVkYiIsInBob25lX251bWJlciI6Iis3OTY'
        'wMjE0MzA5MiIsImVtYWlsIjoidjY3ODcwOTk1QGdtYWlsLmNvbSIsInJvbGUiOiJVc'
        '2VyIiwiYnV5ZXJJZCI6MjA0MTQ3Niwib2lfYXVfaWQiOiJlZTA0ZGVlMy03ZjhhLTQ'
        '3ZGMtYWY5My0zOGRlOThmMWYzODciLCJvaV9wcnN0IjoiYjJjLnB1YmxpYy5jbGllb'
        'nQiLCJjbGllbnRfaWQiOiJiMmMucHVibGljLmNsaWVudCIsIm9pX3Rrbl9pZCI6ImY'
        '0NTg2ZjY1LWRiNWItNDY0Zi1hMTFlLTlkZTk1MGFmZTllYSJ9.HQA3wVKMIxXDqGQQ'
        'HUaPnREnFc8JyIizR4vrTcnSNZt66XAX6rUf6_QRxbcZhAQOlqIjeEalLp1YxDLsVw'
        'masdFpFaKKqfF3R-fQ3OCt-PqKZ2HrzqnzrBogh_CYZ47kTKBMhZRN-yN1-wR01J-S'
        'UWMMV5Z2aQ-7dVFqlo6JclpK4pmsx8O9giqU6V7mUpJ47u8V-N49Xc97Huzb4qCXkZ'
        'sfHjcPiDbY0CZUYlFZK6T7b-SQg9fZrtLoMb0xn8EYxHh3M0z2C_4FG9OiorkovYUE'
        '9IrBe3lHAxwrIHDmNBGHS5BFD2Drtyr3wlOs7ChH-R9rDRKJeeVlOxfX4ZXLxg;'
        'PHPSESSID=4sn4umcse0uk9fe58j60lmhb1a; adrdel=1760955002437;'
        'spjs=1760957653533_3d50de78_0135012e_40b95c84684529b694db00fac7c6'
        'ba97_34uIDmbS4jcN2KlszbBSulzbBgtIn/4TSla3elM9rTGYVSXY4Bx9ECdTsldvm'
        'vueptIg352J6Twm08N3T2S0jdDcDeFZBWB8MrvuUioCh/uGejh8lKVwpJjLJL4Us1E'
        '43WgpjUTyYGap1CQ4ZS2N0enVZopX3gsCm0enbhMd2KyRMKGlyPlZWFOygTXNGei/'
        'JlM8ZZ3ENHiEzfgx3FbzivI+X6OOhzcrfL2NXCFEgbCd3gv71uLiQxqOzl9CPJzwi'
        'FS1+ZT4SCQqRsZ6Z1+/MxsHUJMfm2l7E9Kj2f45Y70k99QiOz7++sXNXCGoFOQ/9M'
        'jLtz7iVz3lnq9jSvDgBYotvB2l0dAxjrrr70EH57JKDVGt5yn4cfmFlQihLo+zDeG'
        'hvBRerjbBRRUlS2y8iDCgs/H7Hk/L0oJTZw8FBLlgXc3wz6BwXBb7P4IaJ5Zbsz4L'
        'v0cSY/WuKip/HZAJ5myJKPTDYmxn+PfyDdX93ZErhoWu5s+4FFn0818Szs7up3QFp'
        '+7MPNzQhJBVa04MvIDzP3PKtxJNlDjohT0kRW33q9qGDsZgDoj9XakWslZQeRnd6D'
        'G2RyPqmQj4cpjJRV3AcC/i3u4jCYAFWcE67LYpJzDEnIh4LEWRgTVdSsqephJj5++7'
        'ey8k36jQy7bROQE/DdKq12U7oN+MBT6FBfF4LBlepYHw1Q86rV2WA6Omb1rEiPAMb'
        'dB5oiZ/4mmr5r/iYg/IvHyEcSVVAYlI7ihgYMl129BJLYRfD3yEN7a4iX8++GqHRr'
        '8w/Y3xWDSkOJFcOn4Fk2G3DP9q3nYB4bSEyRrdpIBQJCvXtzsDDv6imlYF2YG9TSE'
        'LJNbZIBv7v7dDIvb+qloONdGhRU0o6Ly0YCzSixeWO4NeXHLItUdqEl5f4+uXN7s8'
        'e2uvRxrhR9VQi140EXOXbFd4zcQdz4ObRzRaAh5vMghVp3lDnO+wi1QgV48baj8C0'
        'qb2SxnamCXz4HWdmEm8Ed798ngWxTqGXilxzJVgmVf7/qVtReOxD1wq+UfKYiYFWb'
        'l0RQDRvhzKBjtjSzhkLCGgKLbLGoe/olXY57s9kHTxdTHZbH38Cp3OCjJmlsL7ILP'
        'R3LYXM4P+JPKrHmaYDt3/0F/S8l7Hah3owcG0MChMfGlhgMPVArlp9eTBuo6qY+Ur'
        'Sxyq8AWp2gY+YpLO9yS3d7/kFEB4rN0JPovKjoRQoPSdGOS/dlAt+1sDS6sT//7SH'
        'IMC/9ecDPFoEhJu7Qi4WYAQwrcmWjl95LBVQ/ou3roWG3lVubUkflR5KGTLRABtVf'
        'iYdNpWp2Eo3T39xNY0kQhPKzinwyWgSNpsSyXIqfXdIdS4AVmu8sqWZnpkz57iTFV'
        '0kdlsacqFgXAxauxaKLYS57O5q3IIwV1rcD6VtWjQPSjH33GSb4KZGmYjp2HXKmy8'
        'mjDFY9fOCup+UsPDd2oBgejlOT2xycXwbGLbnjdqV/Lu00oYmZUboySuWrpuVgHxp'
        'Z1NjixGgUE0g9+odLPv4W73pgRw3tBtICnULHBPFBtOjK1vNo8TE4WV4AHFwdNxJ7'
        'swrvxwteUbyY51MpVV2vm+HRewGhFnGG9bmn92kva+vw8mDdAxwbUN2Kn8Rh/tM41'
        '3hiTIJhpzWuaczWeQ4yTdXDzfB6M4CtbVoTIYGe; _ym_isad=2; _ym_visorc=b;'
        'is_role_agent=false; cted=modId%3Dop885zi2%3Bclient_id%3D422080909.'
        '1759945935%3Bya_client_id%3D175994593610628113; _ct_ids=op885zi2%3A'
        '42831%3A653446908; _ct_session_id=653446908; _ct_site_id=42831;'
        'PageNumber=4; _spx=eyJpZCI6Ijg1ODIwNDAyLTczZjgtNDc1Yy05NTg5LWU5ZWM'
        '2NGU5MzJlOSIsInNvdXJjZSI6IiIsImZpeGVkIjp7InN0YWNrIjpbMCwwLDAsMCwtM'
        'jEwMTI5NjYzXX19; advcake_track_url=%3D20250113ibkNERA0J4nXYQ9dlmNi'
        '89jTsRL%2BlpJ6t4vxIb8U41jPjT6AJQY%2BVZWoBKyPL6SfzokIeRlCcGgBn1nzWW'
        'P3nW1nu%2BeU9KXxGREo4pl%2FRhU12abgX%2Ffn9OwIsuAdpKyVt06yek0mdxkVff'
        'N%2FvYzWQQpOlPcNlvp3pAHoZ2g1%2B9VNxYZeDg%2F%2FqAqpewnEa1lDCLwAuwJM'
        '3fUorykdjrgXrk30XokABRhjUs95eEZXDGwjDmluLHJHX7%2FGkV3Z5oq%2B%2B9V%'
        '2FIhT5%2BGZahZEi4FKSv5CLAU4aajAKgWTTbzAYtJvXThBRtpC68rZ0UofmeL3faC'
        'wQUSAY8a5c5nXcn3HlHbCG4PvCivEGylBRlQ%2F8GRICEc0SszFRtknCOqWXx5O6Wc'
        'jNud%2Bu2XrcuOgHuE8TYq2dleraEPMkEEnLfApYxX8HhEHDgOhTZAAQLdUtezi94'
        'CooiQovA8I4AnIjK6uUWLqzBRL%2FORNLCZ95UinEoLLGMVv112ITkAJiw7bA0jiN'
        'kzPEU%2B5nx1Sd8Im3kukL7ONduBiK0VWujHMiCSiYjcL%2B%2F2ZkqN8xNTbEOgy'
        '8GHk1kAwat4nofzq%2F3Ud4L%2BH0EDA%2FSqlEJfYiIVU499DSPDdCqUNVu%2FHA'
        'm66jhBgszViQICM8N1ncb1bfUnlGFpvFavUJ4FebagCqct3e3YDanJ8s%2BsbLRZV'
        '4jDw%3D; call_s=___op885zi2.1760960999.653446908.241285:745570|2___;'
        'tmr_detect=0%7C1760959201364; __ddg10_=1760959207;'
        '__ddg9_=176.15.168.183; __ddg8_=uhnDqboixxEup4iq;'
        'XSRF-TOKEN=eyJpdiI6ImYyVVJybWs3WHFKK0paT3FaWXVSRUE9PSIsInZhbHVlI'
        'joiZ2NjWGdhK0loSFl5azVISTFjUGxWTnkvdnNjNEtBNnowZEdWcW9icTI4bllnY'
        'nhhRGlFdWNQSllEMTNoWlh1NVd2RVRlNFJZQ0c0b0V6ajkrRXpzTzVJSzRyN2Yvc'
        'UFoeGhYRU1kalUvdFJCYWlNb2hhWVlDdUhKSXBLbm9oMjciLCJtYWMiOiIzY2Q3N'
        'mM0YTNmZjk3NGIyZWM0ODk1MDczNGIxYThkNWM3ZjExMjI4NjdiYmQzNDA2ZTQ0ZT'
        'Y0YzUyOTM1NmVkIn0%3D; funsan_session=eyJpdiI6InpXZnQ1YVY1Ti9YRm9'
        'RQTJNaG00QkE9PSIsInZhbHVlIjoidWJzVkZrbFJZWTRIbWZaM1pKREdUaUZkTmh'
        'BekdIVlFYM0pONG8yS1pKcjJ5Z1VsT09tanBmcEFQSmpkVzgyeERPak9hcGQvS2h'
        'WWTVMK3E1cFd0T1VSdTg0bDFUNEVRWE10b01XMUtzNFQyS2RYMHprczZiMDV0dGR'
        '2bjZGKzciLCJtYWMiOiI4MWZmZWE3YjM4NjZhMDQzNzljMGNmYzY4ZDJmYjE5OTN'
        'lZTExOTEzYzhmMDNlOGY5MDUwYTJlMTMzMWRiMzI4In0%3D; spsc=1760960548'
        '834_e197ff96562d054246d88ea69c67e476_g6eerSLIAaqq611bK1uoq2f758Z'
        'nPQhfrIv5ZuOfjwcZ; _ga_GJ17DPCPJY=GS2.1.s1760957658$o16$g1$t1760'
        '960562$j37$l0$h0'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

    # # 1. Ввод в поиск запроса номера departureCityId города,
    # #  которого нет в списке городов вкладки "Откуда"(нет id = 908868)


def test_negative_search_tour1():

    url = "https://fstravel.com/searchtour/country/europe/"
    "russia?departureCityId=908868&arrivalCountryId=210357"
    "&minStartDate=2025-11-03&maxStartDate=2025-11-03&minNightsCount=7"
    "&maxNightsCount=7&adults=2&flightTypes=all"

    payload = {}
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;'
        'q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/'
        'signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'referer': 'https://fstravel.com/searchtour',
        'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8",'
        ' "Chromium";v="141"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)'
        ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0'
        ' Mobile Safari/537.36',
        'Cookie': 'is_role_agent=false; spid=1759945933331_3525d277eb1a4dc4e01874b9310c1ae2_i77mh1scah4h6wh5; __ddg1_=goFa24s6VCc0XIeMxkF7; _ga=GA1.1.422080909.1759945935; adrcid=AUJVUtkKWnNkh1SgaTgVDjw; flocktory-uuid=6cce39d7-d616-4f25-866c-694873d07482-5; _ymab_param=i2F1e-pEE4ul20Huet8XPoYx8WtIy1fymYEy4NbvnOhAfe7OOU_mldljzvEonEP6s0KqoRmoONG37Gja4pf6NPizIKU; _ym_uid=175994593610628113; _ym_d=1759945936; tmr_lvid=572dc590a568b50263e90859e4f396bd; tmr_lvidTS=1759945935881; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; _ct=1700000000423386978; _ct_client_global_id=9dc8d198-a5c9-5510-80a4-d17167669ef9; rai=b8cc547af6e96ad7188b9890915536ca; advcake_track_id=b1281536-227f-47a7-3f9c-ae13a27d1f1d; advcake_session_id=a907d419-5daf-3fea-7608-4f69ecd86830; r2UserId=1759945946866477; uxs_uid=8d66b910-a46f-11f0-b95a-893caab4cf73; has_action=true; analytic_id=1759945946972488; mindboxDeviceUUID=0ce09a14-8a7c-4de6-a1cb-498b257cc557; directCrm-session=%7B%22deviceGuid%22%3A%220ce09a14-8a7c-4de6-a1cb-498b257cc557%22%7D; acs_3=%7B%22hash%22%3A%221aa3f9523ee6c2690cb34fc702d4143056487c0d%22%2C%22nst%22%3A1760970765084%2C%22sl%22%3A%7B%22224%22%3A1760884365084%2C%221228%22%3A1760884365084%7D%7D; domain_sid=7RDOPdKftNZl87aKOMk3h%3A1760884365541; token_type_fs=Bearer; access_token_fs=eyJhbGciOiJSUzI1NiIsImtpZCI6IjU4MUNCNTNGRUE1RDg1MjI3QjA2MDU2MEMzMEYxRDkwNTlEQkNBMEEiLCJ4NXQiOiJXQnkxUC1wZGhTSjdCZ1Znd3c4ZGtGbmJ5Z28iLCJ0eXAiOiJhdCtqd3QifQ.eyJpc3MiOiJodHRwczovL2F1dGgyLmZzdHJhdmVsLmNvbS8iLCJleHAiOjE3NjExNDM2MDcsImlhdCI6MTc2MDg4NDQwNywiYXVkIjoid2ViYXBpIiwic2NvcGUiOiJwcm9maWxlIGVtYWlsIHJvbGVzIG9mZmxpbmVfYWNjZXNzIHBob25lIHdlYmFwaSIsImp0aSI6IjhlMjY1YjQ1LTM1ZGEtNDUxZC1iNjdhLWNjNzNlMmRhZDcxMSIsInN1YiI6ImE3MWJkZDAzLTEwNWUtNDFiMy05ZTcxLTZlNzJmMGZiZGVkYiIsInBob25lX251bWJlciI6Iis3OTYwMjE0MzA5MiIsImVtYWlsIjoidjY3ODcwOTk1QGdtYWlsLmNvbSIsInJvbGUiOiJVc2VyIiwiYnV5ZXJJZCI6MjA0MTQ3Niwib2lfYXVfaWQiOiJlZTA0ZGVlMy03ZjhhLTQ3ZGMtYWY5My0zOGRlOThmMWYzODciLCJvaV9wcnN0IjoiYjJjLnB1YmxpYy5jbGllbnQiLCJjbGllbnRfaWQiOiJiMmMucHVibGljLmNsaWVudCIsIm9pX3Rrbl9pZCI6ImY0NTg2ZjY1LWRiNWItNDY0Zi1hMTFlLTlkZTk1MGFmZTllYSJ9.HQA3wVKMIxXDqGQQHUaPnREnFc8JyIizR4vrTcnSNZt66XAX6rUf6_QRxbcZhAQOlqIjeEalLp1YxDLsVwmasdFpFaKKqfF3R-fQ3OCt-PqKZ2HrzqnzrBogh_CYZ47kTKBMhZRN-yN1-wR01J-SUWMMV5Z2aQ-7dVFqlo6JclpK4pmsx8O9giqU6V7mUpJ47u8V-N49Xc97Huzb4qCXkZsfHjcPiDbY0CZUYlFZK6T7b-SQg9fZrtLoMb0xn8EYxHh3M0z2C_4FG9OiorkovYUE9IrBe3lHAxwrIHDmNBGHS5BFD2Drtyr3wlOs7ChH-R9rDRKJeeVlOxfX4ZXLxg; PHPSESSID=4sn4umcse0uk9fe58j60lmhb1a; adrdel=1760955002437; spjs=1760957653533_3d50de78_0135012e_40b95c84684529b694db00fac7c6ba97_34uIDmbS4jcN2KlszbBSulzbBgtIn/4TSla3elM9rTGYVSXY4Bx9ECdTsldvmvueptIg352J6Twm08N3T2S0jdDcDeFZBWB8MrvuUioCh/uGejh8lKVwpJjLJL4Us1E43WgpjUTyYGap1CQ4ZS2N0enVZopX3gsCm0enbhMd2KyRMKGlyPlZWFOygTXNGei/JlM8ZZ3ENHiEzfgx3FbzivI+X6OOhzcrfL2NXCFEgbCd3gv71uLiQxqOzl9CPJzwiFS1+ZT4SCQqRsZ6Z1+/MxsHUJMfm2l7E9Kj2f45Y70k99QiOz7++sXNXCGoFOQ/9MjLtz7iVz3lnq9jSvDgBYotvB2l0dAxjrrr70EH57JKDVGt5yn4cfmFlQihLo+zDeGhvBRerjbBRRUlS2y8iDCgs/H7Hk/L0oJTZw8FBLlgXc3wz6BwXBb7P4IaJ5Zbsz4Lv0cSY/WuKip/HZAJ5myJKPTDYmxn+PfyDdX93ZErhoWu5s+4FFn0818Szs7up3QFp+7MPNzQhJBVa04MvIDzP3PKtxJNlDjohT0kRW33q9qGDsZgDoj9XakWslZQeRnd6DG2RyPqmQj4cpjJRV3AcC/i3u4jCYAFWcE67LYpJzDEnIh4LEWRgTVdSsqephJj5++7ey8k36jQy7bROQE/DdKq12U7oN+MBT6FBfF4LBlepYHw1Q86rV2WA6Omb1rEiPAMbdB5oiZ/4mmr5r/iYg/IvHyEcSVVAYlI7ihgYMl129BJLYRfD3yEN7a4iX8++GqHRr8w/Y3xWDSkOJFcOn4Fk2G3DP9q3nYB4bSEyRrdpIBQJCvXtzsDDv6imlYF2YG9TSELJNbZIBv7v7dDIvb+qloONdGhRU0o6Ly0YCzSixeWO4NeXHLItUdqEl5f4+uXN7s8e2uvRxrhR9VQi140EXOXbFd4zcQdz4ObRzRaAh5vMghVp3lDnO+wi1QgV48baj8C0qb2SxnamCXz4HWdmEm8Ed798ngWxTqGXilxzJVgmVf7/qVtReOxD1wq+UfKYiYFWbl0RQDRvhzKBjtjSzhkLCGgKLbLGoe/olXY57s9kHTxdTHZbH38Cp3OCjJmlsL7ILPR3LYXM4P+JPKrHmaYDt3/0F/S8l7Hah3owcG0MChMfGlhgMPVArlp9eTBuo6qY+UrSxyq8AWp2gY+YpLO9yS3d7/kFEB4rN0JPovKjoRQoPSdGOS/dlAt+1sDS6sT//7SHIMC/9ecDPFoEhJu7Qi4WYAQwrcmWjl95LBVQ/ou3roWG3lVubUkflR5KGTLRABtVfiYdNpWp2Eo3T39xNY0kQhPKzinwyWgSNpsSyXIqfXdIdS4AVmu8sqWZnpkz57iTFV0kdlsacqFgXAxauxaKLYS57O5q3IIwV1rcD6VtWjQPSjH33GSb4KZGmYjp2HXKmy8mjDFY9fOCup+UsPDd2oBgejlOT2xycXwbGLbnjdqV/Lu00oYmZUboySuWrpuVgHxpZ1NjixGgUE0g9+odLPv4W73pgRw3tBtICnULHBPFBtOjK1vNo8TE4WV4AHFwdNxJ7swrvxwteUbyY51MpVV2vm+HRewGhFnGG9bmn92kva+vw8mDdAxwbUN2Kn8Rh/tM413hiTIJhpzWuaczWeQ4yTdXDzfB6M4CtbVoTIYGe; _ym_isad=2; _ym_visorc=b; is_role_agent=false; cted=modId%3Dop885zi2%3Bclient_id%3D422080909.1759945935%3Bya_client_id%3D175994593610628113; _ct_ids=op885zi2%3A42831%3A653446908; _ct_session_id=653446908; _ct_site_id=42831; PageNumber=4; _spx=eyJpZCI6Ijg1ODIwNDAyLTczZjgtNDc1Yy05NTg5LWU5ZWM2NGU5MzJlOSIsInNvdXJjZSI6IiIsImZpeGVkIjp7InN0YWNrIjpbMCwwLDAsMCwtMjEwMTI5NjYzXX19; advcake_track_url=%3D20250113ibkNERA0J4nXYQ9dlmNi89jTsRL%2BlpJ6t4vxIb8U41jPjT6AJQY%2BVZWoBKyPL6SfzokIeRlCcGgBn1nzWWP3nW1nu%2BeU9KXxGREo4pl%2FRhU12abgX%2Ffn9OwIsuAdpKyVt06yek0mdxkVffN%2FvYzWQQpOlPcNlvp3pAHoZ2g1%2B9VNxYZeDg%2F%2FqAqpewnEa1lDCLwAuwJM3fUorykdjrgXrk30XokABRhjUs95eEZXDGwjDmluLHJHX7%2FGkV3Z5oq%2B%2B9V%2FIhT5%2BGZahZEi4FKSv5CLAU4aajAKgWTTbzAYtJvXThBRtpC68rZ0UofmeL3faCwQUSAY8a5c5nXcn3HlHbCG4PvCivEGylBRlQ%2F8GRICEc0SszFRtknCOqWXx5O6WcjNud%2Bu2XrcuOgHuE8TYq2dleraEPMkEEnLfApYxX8HhEHDgOhTZAAQLdUtezi94CooiQovA8I4AnIjK6uUWLqzBRL%2FORNLCZ95UinEoLLGMVv112ITkAJiw7bA0jiNkzPEU%2B5nx1Sd8Im3kukL7ONduBiK0VWujHMiCSiYjcL%2B%2F2ZkqN8xNTbEOgy8GHk1kAwat4nofzq%2F3Ud4L%2BH0EDA%2FSqlEJfYiIVU499DSPDdCqUNVu%2FHAm66jhBgszViQICM8N1ncb1bfUnlGFpvFavUJ4FebagCqct3e3YDanJ8s%2BsbLRZV4jDw%3D; call_s=___op885zi2.1760960999.653446908.241285:745570|2___; tmr_detect=0%7C1760959201364; __ddg10_=1760959207; __ddg9_=176.15.168.183; __ddg8_=uhnDqboixxEup4iq; XSRF-TOKEN=eyJpdiI6ImYyVVJybWs3WHFKK0paT3FaWXVSRUE9PSIsInZhbHVlIjoiZ2NjWGdhK0loSFl5azVISTFjUGxWTnkvdnNjNEtBNnowZEdWcW9icTI4bllnYnhhRGlFdWNQSllEMTNoWlh1NVd2RVRlNFJZQ0c0b0V6ajkrRXpzTzVJSzRyN2YvcUFoeGhYRU1kalUvdFJCYWlNb2hhWVlDdUhKSXBLbm9oMjciLCJtYWMiOiIzY2Q3NmM0YTNmZjk3NGIyZWM0ODk1MDczNGIxYThkNWM3ZjExMjI4NjdiYmQzNDA2ZTQ0ZTY0YzUyOTM1NmVkIn0%3D; funsan_session=eyJpdiI6InpXZnQ1YVY1Ti9YRm9RQTJNaG00QkE9PSIsInZhbHVlIjoidWJzVkZrbFJZWTRIbWZaM1pKREdUaUZkTmhBekdIVlFYM0pONG8yS1pKcjJ5Z1VsT09tanBmcEFQSmpkVzgyeERPak9hcGQvS2hWWTVMK3E1cFd0T1VSdTg0bDFUNEVRWE10b01XMUtzNFQyS2RYMHprczZiMDV0dGR2bjZGKzciLCJtYWMiOiI4MWZmZWE3YjM4NjZhMDQzNzljMGNmYzY4ZDJmYjE5OTNlZTExOTEzYzhmMDNlOGY5MDUwYTJlMTMzMWRiMzI4In0%3D; spsc=1760960548834_e197ff96562d054246d88ea69c67e476_g6eerSLIAaqq611bK1uoq2f758ZnPQhfrIv5ZuOfjwcZ; _ga_GJ17DPCPJY=GS2.1.s1760957658$o16$g1$t1760960562$j37$l0$h0'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

    # 2. Ввод в поиск запроса номера города вылета
    # departureCityId=(без номера), или имитация пустого поля  "Откуда".


def test_negative_search_tour2():

    url = "https://fstravel.com/searchtour/country/europe/"
    "russia?departureCityId=&arrivalCountryId=210357&minStartDate=2025-11-03"
    "&maxStartDate=2025-11-03&minNightsCount=7&maxNightsCount=7"
    "&adults=2&flightTypes=all"

    payload = {}
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
        'image/avif,image/webp,image/apng,*/*;q=0.8,application/'
        'signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'referer': 'https://fstravel.com/searchtour',
        'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8",'
        ' "Chromium";v="141"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)'
        ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0'
        ' Mobile Safari/537.36',
        'Cookie': 'is_role_agent=false; spid=1759945933331_3525d277eb1a4dc4e01874b9310c1ae2_i77mh1scah4h6wh5; __ddg1_=goFa24s6VCc0XIeMxkF7; _ga=GA1.1.422080909.1759945935; adrcid=AUJVUtkKWnNkh1SgaTgVDjw; flocktory-uuid=6cce39d7-d616-4f25-866c-694873d07482-5; _ymab_param=i2F1e-pEE4ul20Huet8XPoYx8WtIy1fymYEy4NbvnOhAfe7OOU_mldljzvEonEP6s0KqoRmoONG37Gja4pf6NPizIKU; _ym_uid=175994593610628113; _ym_d=1759945936; tmr_lvid=572dc590a568b50263e90859e4f396bd; tmr_lvidTS=1759945935881; popmechanic_sbjs_migrations=popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1; _ct=1700000000423386978; _ct_client_global_id=9dc8d198-a5c9-5510-80a4-d17167669ef9; rai=b8cc547af6e96ad7188b9890915536ca; advcake_track_id=b1281536-227f-47a7-3f9c-ae13a27d1f1d; advcake_session_id=a907d419-5daf-3fea-7608-4f69ecd86830; r2UserId=1759945946866477; uxs_uid=8d66b910-a46f-11f0-b95a-893caab4cf73; has_action=true; analytic_id=1759945946972488; mindboxDeviceUUID=0ce09a14-8a7c-4de6-a1cb-498b257cc557; directCrm-session=%7B%22deviceGuid%22%3A%220ce09a14-8a7c-4de6-a1cb-498b257cc557%22%7D; acs_3=%7B%22hash%22%3A%221aa3f9523ee6c2690cb34fc702d4143056487c0d%22%2C%22nst%22%3A1760970765084%2C%22sl%22%3A%7B%22224%22%3A1760884365084%2C%221228%22%3A1760884365084%7D%7D; domain_sid=7RDOPdKftNZl87aKOMk3h%3A1760884365541; token_type_fs=Bearer; access_token_fs=eyJhbGciOiJSUzI1NiIsImtpZCI6IjU4MUNCNTNGRUE1RDg1MjI3QjA2MDU2MEMzMEYxRDkwNTlEQkNBMEEiLCJ4NXQiOiJXQnkxUC1wZGhTSjdCZ1Znd3c4ZGtGbmJ5Z28iLCJ0eXAiOiJhdCtqd3QifQ.eyJpc3MiOiJodHRwczovL2F1dGgyLmZzdHJhdmVsLmNvbS8iLCJleHAiOjE3NjExNDM2MDcsImlhdCI6MTc2MDg4NDQwNywiYXVkIjoid2ViYXBpIiwic2NvcGUiOiJwcm9maWxlIGVtYWlsIHJvbGVzIG9mZmxpbmVfYWNjZXNzIHBob25lIHdlYmFwaSIsImp0aSI6IjhlMjY1YjQ1LTM1ZGEtNDUxZC1iNjdhLWNjNzNlMmRhZDcxMSIsInN1YiI6ImE3MWJkZDAzLTEwNWUtNDFiMy05ZTcxLTZlNzJmMGZiZGVkYiIsInBob25lX251bWJlciI6Iis3OTYwMjE0MzA5MiIsImVtYWlsIjoidjY3ODcwOTk1QGdtYWlsLmNvbSIsInJvbGUiOiJVc2VyIiwiYnV5ZXJJZCI6MjA0MTQ3Niwib2lfYXVfaWQiOiJlZTA0ZGVlMy03ZjhhLTQ3ZGMtYWY5My0zOGRlOThmMWYzODciLCJvaV9wcnN0IjoiYjJjLnB1YmxpYy5jbGllbnQiLCJjbGllbnRfaWQiOiJiMmMucHVibGljLmNsaWVudCIsIm9pX3Rrbl9pZCI6ImY0NTg2ZjY1LWRiNWItNDY0Zi1hMTFlLTlkZTk1MGFmZTllYSJ9.HQA3wVKMIxXDqGQQHUaPnREnFc8JyIizR4vrTcnSNZt66XAX6rUf6_QRxbcZhAQOlqIjeEalLp1YxDLsVwmasdFpFaKKqfF3R-fQ3OCt-PqKZ2HrzqnzrBogh_CYZ47kTKBMhZRN-yN1-wR01J-SUWMMV5Z2aQ-7dVFqlo6JclpK4pmsx8O9giqU6V7mUpJ47u8V-N49Xc97Huzb4qCXkZsfHjcPiDbY0CZUYlFZK6T7b-SQg9fZrtLoMb0xn8EYxHh3M0z2C_4FG9OiorkovYUE9IrBe3lHAxwrIHDmNBGHS5BFD2Drtyr3wlOs7ChH-R9rDRKJeeVlOxfX4ZXLxg; PHPSESSID=4sn4umcse0uk9fe58j60lmhb1a; adrdel=1760955002437; spjs=1760957653533_3d50de78_0135012e_40b95c84684529b694db00fac7c6ba97_34uIDmbS4jcN2KlszbBSulzbBgtIn/4TSla3elM9rTGYVSXY4Bx9ECdTsldvmvueptIg352J6Twm08N3T2S0jdDcDeFZBWB8MrvuUioCh/uGejh8lKVwpJjLJL4Us1E43WgpjUTyYGap1CQ4ZS2N0enVZopX3gsCm0enbhMd2KyRMKGlyPlZWFOygTXNGei/JlM8ZZ3ENHiEzfgx3FbzivI+X6OOhzcrfL2NXCFEgbCd3gv71uLiQxqOzl9CPJzwiFS1+ZT4SCQqRsZ6Z1+/MxsHUJMfm2l7E9Kj2f45Y70k99QiOz7++sXNXCGoFOQ/9MjLtz7iVz3lnq9jSvDgBYotvB2l0dAxjrrr70EH57JKDVGt5yn4cfmFlQihLo+zDeGhvBRerjbBRRUlS2y8iDCgs/H7Hk/L0oJTZw8FBLlgXc3wz6BwXBb7P4IaJ5Zbsz4Lv0cSY/WuKip/HZAJ5myJKPTDYmxn+PfyDdX93ZErhoWu5s+4FFn0818Szs7up3QFp+7MPNzQhJBVa04MvIDzP3PKtxJNlDjohT0kRW33q9qGDsZgDoj9XakWslZQeRnd6DG2RyPqmQj4cpjJRV3AcC/i3u4jCYAFWcE67LYpJzDEnIh4LEWRgTVdSsqephJj5++7ey8k36jQy7bROQE/DdKq12U7oN+MBT6FBfF4LBlepYHw1Q86rV2WA6Omb1rEiPAMbdB5oiZ/4mmr5r/iYg/IvHyEcSVVAYlI7ihgYMl129BJLYRfD3yEN7a4iX8++GqHRr8w/Y3xWDSkOJFcOn4Fk2G3DP9q3nYB4bSEyRrdpIBQJCvXtzsDDv6imlYF2YG9TSELJNbZIBv7v7dDIvb+qloONdGhRU0o6Ly0YCzSixeWO4NeXHLItUdqEl5f4+uXN7s8e2uvRxrhR9VQi140EXOXbFd4zcQdz4ObRzRaAh5vMghVp3lDnO+wi1QgV48baj8C0qb2SxnamCXz4HWdmEm8Ed798ngWxTqGXilxzJVgmVf7/qVtReOxD1wq+UfKYiYFWbl0RQDRvhzKBjtjSzhkLCGgKLbLGoe/olXY57s9kHTxdTHZbH38Cp3OCjJmlsL7ILPR3LYXM4P+JPKrHmaYDt3/0F/S8l7Hah3owcG0MChMfGlhgMPVArlp9eTBuo6qY+UrSxyq8AWp2gY+YpLO9yS3d7/kFEB4rN0JPovKjoRQoPSdGOS/dlAt+1sDS6sT//7SHIMC/9ecDPFoEhJu7Qi4WYAQwrcmWjl95LBVQ/ou3roWG3lVubUkflR5KGTLRABtVfiYdNpWp2Eo3T39xNY0kQhPKzinwyWgSNpsSyXIqfXdIdS4AVmu8sqWZnpkz57iTFV0kdlsacqFgXAxauxaKLYS57O5q3IIwV1rcD6VtWjQPSjH33GSb4KZGmYjp2HXKmy8mjDFY9fOCup+UsPDd2oBgejlOT2xycXwbGLbnjdqV/Lu00oYmZUboySuWrpuVgHxpZ1NjixGgUE0g9+odLPv4W73pgRw3tBtICnULHBPFBtOjK1vNo8TE4WV4AHFwdNxJ7swrvxwteUbyY51MpVV2vm+HRewGhFnGG9bmn92kva+vw8mDdAxwbUN2Kn8Rh/tM413hiTIJhpzWuaczWeQ4yTdXDzfB6M4CtbVoTIYGe; _ym_isad=2; _ym_visorc=b; is_role_agent=false; cted=modId%3Dop885zi2%3Bclient_id%3D422080909.1759945935%3Bya_client_id%3D175994593610628113; _ct_ids=op885zi2%3A42831%3A653446908; _ct_session_id=653446908; _ct_site_id=42831; PageNumber=4; _spx=eyJpZCI6Ijg1ODIwNDAyLTczZjgtNDc1Yy05NTg5LWU5ZWM2NGU5MzJlOSIsInNvdXJjZSI6IiIsImZpeGVkIjp7InN0YWNrIjpbMCwwLDAsMCwtMjEwMTI5NjYzXX19; advcake_track_url=%3D20250113ibkNERA0J4nXYQ9dlmNi89jTsRL%2BlpJ6t4vxIb8U41jPjT6AJQY%2BVZWoBKyPL6SfzokIeRlCcGgBn1nzWWP3nW1nu%2BeU9KXxGREo4pl%2FRhU12abgX%2Ffn9OwIsuAdpKyVt06yek0mdxkVffN%2FvYzWQQpOlPcNlvp3pAHoZ2g1%2B9VNxYZeDg%2F%2FqAqpewnEa1lDCLwAuwJM3fUorykdjrgXrk30XokABRhjUs95eEZXDGwjDmluLHJHX7%2FGkV3Z5oq%2B%2B9V%2FIhT5%2BGZahZEi4FKSv5CLAU4aajAKgWTTbzAYtJvXThBRtpC68rZ0UofmeL3faCwQUSAY8a5c5nXcn3HlHbCG4PvCivEGylBRlQ%2F8GRICEc0SszFRtknCOqWXx5O6WcjNud%2Bu2XrcuOgHuE8TYq2dleraEPMkEEnLfApYxX8HhEHDgOhTZAAQLdUtezi94CooiQovA8I4AnIjK6uUWLqzBRL%2FORNLCZ95UinEoLLGMVv112ITkAJiw7bA0jiNkzPEU%2B5nx1Sd8Im3kukL7ONduBiK0VWujHMiCSiYjcL%2B%2F2ZkqN8xNTbEOgy8GHk1kAwat4nofzq%2F3Ud4L%2BH0EDA%2FSqlEJfYiIVU499DSPDdCqUNVu%2FHAm66jhBgszViQICM8N1ncb1bfUnlGFpvFavUJ4FebagCqct3e3YDanJ8s%2BsbLRZV4jDw%3D; call_s=___op885zi2.1760960999.653446908.241285:745570|2___; tmr_detect=0%7C1760959201364; __ddg10_=1760959207; __ddg9_=176.15.168.183; __ddg8_=uhnDqboixxEup4iq; XSRF-TOKEN=eyJpdiI6ImYyVVJybWs3WHFKK0paT3FaWXVSRUE9PSIsInZhbHVlIjoiZ2NjWGdhK0loSFl5azVISTFjUGxWTnkvdnNjNEtBNnowZEdWcW9icTI4bllnYnhhRGlFdWNQSllEMTNoWlh1NVd2RVRlNFJZQ0c0b0V6ajkrRXpzTzVJSzRyN2YvcUFoeGhYRU1kalUvdFJCYWlNb2hhWVlDdUhKSXBLbm9oMjciLCJtYWMiOiIzY2Q3NmM0YTNmZjk3NGIyZWM0ODk1MDczNGIxYThkNWM3ZjExMjI4NjdiYmQzNDA2ZTQ0ZTY0YzUyOTM1NmVkIn0%3D; funsan_session=eyJpdiI6InpXZnQ1YVY1Ti9YRm9RQTJNaG00QkE9PSIsInZhbHVlIjoidWJzVkZrbFJZWTRIbWZaM1pKREdUaUZkTmhBekdIVlFYM0pONG8yS1pKcjJ5Z1VsT09tanBmcEFQSmpkVzgyeERPak9hcGQvS2hWWTVMK3E1cFd0T1VSdTg0bDFUNEVRWE10b01XMUtzNFQyS2RYMHprczZiMDV0dGR2bjZGKzciLCJtYWMiOiI4MWZmZWE3YjM4NjZhMDQzNzljMGNmYzY4ZDJmYjE5OTNlZTExOTEzYzhmMDNlOGY5MDUwYTJlMTMzMWRiMzI4In0%3D; spsc=1760960548834_e197ff96562d054246d88ea69c67e476_g6eerSLIAaqq611bK1uoq2f758ZnPQhfrIv5ZuOfjwcZ; _ga_GJ17DPCPJY=GS2.1.s1760957658$o16$g1$t1760960562$j37$l0$h0'
        }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)

    #  3. Поиск тура при вводе в запрос номера arrivalCountryId страны,
    #  которая есть в списке стран вкладки "Куда", например: "Турция" ,
    #  без Cookie токена


def test_negative_search_tour3():

    url = "https://fstravel.com/searchtour/country/europe/"
    "russia?departureCityId=&arrivalCountryId=210357&minStartDate=2025-11-03"
    "&maxStartDate=2025-11-03&minNightsCount=7&maxNightsCount=7&adults=2"
    "&flightTypes=all"

    payload = {}
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,'
        'image/avif,image/webp,image/apng,*/*;q=0.8,application/'
        'signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'referer': 'https://fstravel.com/searchtour',
        'sec-ch-ua': '"Google Chrome";v="141", "Not?A_Brand";v="8",'
        ' "Chromium";v="141"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)'
        ' AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Mobile'
        ' Safari/537.36',
        'Cookie': 'is_role_agent=false; spid='
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
