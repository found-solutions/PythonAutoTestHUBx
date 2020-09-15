# -*- coding: utf-8 -*-
# @Author ：Mingjie Huang
# @Time   ：2019/8/13 16:12
# @IDE    ：PyCharm
import requests
requests.packages.urllib3.disable_warnings()
# import requests
#
# _header = {
# 'Accept': 'application/prs.CRM-Back-End.v2+json',
# 'Authorization':'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjliNWM2NDZiYjMzMTQyYjZhMGZiZWNlZDJiZjZjNDhlMzcwNDc4ODNiNDRkMDI0OTk3ZmY4NDNiYzJmOGRlMDFjYWVjMDEzNTYwYmMxNzkzIn0.eyJhdWQiOiIxIiwianRpIjoiOWI1YzY0NmJiMzMxNDJiNmEwZmJlY2VkMmJmNmM0OGUzNzA0Nzg4M2I0NGQwMjQ5OTdmZjg0M2JjMmY4ZGUwMWNhZWMwMTM1NjBiYzE3OTMiLCJpYXQiOjE1NjU2Nzc5NzcsIm5iZiI6MTU2NTY3Nzk3NywiZXhwIjoxNTY2MjgyNzc3LCJzdWIiOiIxMCIsInNjb3BlcyI6WyIqIl19.HP0Rkd9oKUwnHEXK7dEiQr9ra6OVV3RgBKqDXNuqQhmnsWTrdaAkWUW1KqWXDbaa5FExvmxouJ3dGyl28Y1m28KJ2-OzV4Ab31kA4g4sv6-XFWpyUZ5uLxYVBFQRajopBDjxHpc2uWpC6whRslNwFFRnMivBMlRo_O7fc51Jo0JBqpByoUk_k32DVHwiSEXv49KrfsUC7dtYFW_4IrdhY_MqUQiIObiW0_MrdKki3gAJ-QPJTzKo0JZFIR-GoWnTSPckSm97aZzegR8hCAbB8owF8ORkowEoYYaqUVNbByOjEhEATNb2YPO6MaHqbnReZutWkKTEXBIQKDtYeX4Xh9BSJ_9hxyylf_V83WKvv2EnoV3hA9vxUae5ojhY5E6RUPU0sXQmoTOisjLSvz0PFs2uzfi1OkW_Yac8-N2OANRB1QdMW2Hkp0BEjntt9Mk04FbN5VeF_vnuj715EaxiIAW11TyrhWY8t8OCIO-Ar4AhOCY0xCBBWa67RToFnbLBa1Ia4qyt8G7bpzaVqRvS7gQiFfktUvgYZP6dNZTFgS-LTBuniORZvGa0iBznp0R18JWkCvcC7ZrO3EkJ4V5p32nRGPtlp6GcxvkAawi0gXh99n60-GWr4UxFfTj1WLmkKDesfFofbCxyTAK13gtPdLJvEcjpIzr3eqPypsD0Hnk',
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
# 'Content-Type': 'application/x-www-form-urlencoded',
#         }
# _url = 'https://staging-portal-api.trademax.global/api/funding/transactions/assign'
#
# def test():
#     for i in (1241,1235):
#         data = {'action': 1, 'transaction_id': i}
#         r= requests.patch(url=_url, headers=_header, data=data, verify=False)
#         print(r.text,r.status_code)
#
#
# if __name__ == '__main__':
#     test()

# import time,datetime
# import requests
# from multiprocessing import Process
# from multiprocessing import Pool
#
# parameters = {
#     "times": 1, # 并发量
#     "url": "https://staging-portal-api.trademax.global/api/funding/transactions/assign",
#     "header": {
#     "Accept": "application/prs.CRM-Back-End.v2+json",
#     "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjgzY2ZiNmQ2YTI3MGY3ZmEyNjFlOGY5NmFjNmY0ODBmMmYwMThkY2E2YTY2NTY3MjI5NGQ2YjFhYWY2MGE1NGJiZDk0OTNlY2JlNjkwZjRkIn0.eyJhdWQiOiIxIiwianRpIjoiODNjZmI2ZDZhMjcwZjdmYTI2MWU4Zjk2YWM2ZjQ4MGYyZjAxOGRjYTZhNjY1NjcyMjk0ZDZiMWFhZjYwYTU0YmJkOTQ5M2VjYmU2OTBmNGQiLCJpYXQiOjE1NzA2OTA2NjIsIm5iZiI6MTU3MDY5MDY2MiwiZXhwIjoxNTcxMjk1NDYyLCJzdWIiOiIxIiwic2NvcGVzIjpbIioiXX0.NnaZgbX0jImM-aZJBgYMIOaYszhXP15EHp-_pwfvfeXaIvjfWrOpYK7PpTkekaT1w4iYG-Vq6nPSJ93dnsbhyzNDLwSU8x-HDTAKgYWdmoe1V4ryvhq6J8UMWzSovWNjWZEmmv2eJuQ8Qt2tobnDT3ff2riirmqm0StmAa3bTGs4E_0Ef8yznh2_VahnUFgPIIrdS7yk4FVjImfsf-CxMutk0e6uFdcxMsaXueS8FR9WX5-_p77fduEIhJoUS2dHVVTQm3dWt5sva05jsbfGMxFoMUIV4YloVeLmUQbJtNPCPBl8ys-DWgK8qDunfXbnR6dIaew8N8R47ta_blQQhXr-TiN0FvDNZEiwaWe8UBRgq4sk2d5OXjmoQDuzfz3XI3g2rZfQYMomFuPWCOJNiTr3PmXHAD9e7N0UeFhLrWx0aIH4c9yd_5qXBK7wKYpcCQ4rXKL2_dTmGTQFXQvfmZtBUc0WysBCiu93PaFMRKZDyyFrr5zPA2RlE5f-nzckLlB-15-fvv7MyjEcyKn2ibEZlWTk8rwXZFQNzctdcV0wCxuN5BHJOAsDZcpxD2ohOJlwL346FoTLIsEMoEupG7wPUOynCKR2X3KC0DpSiVrajALhB82rZPvTtCcohse-k1VNncrIV6CuIXuMrmvexFHpDN4Yuc-m-FdkP4TUvck",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
#     "Content-Type": "application/x-www-form-urlencoded",
#             }
# }
#
# def run_task(idx):
#     for i in (2320,2322):
#         data = {'action': 1, 'transaction_id': i}
#         response = requests.patch(url=parameters["url"], data=data, headers=parameters["header"])
#         print(datetime.datetime.now().strftime('%Y_%m_%d_%H:%M:%S.%f'))
#         if response.status_code == 204:
#             result = response.content.decode('utf-8')
#         else:
#             result = "访问失败"
#         print("第 %s 次执行：%s \n" % (idx, result))
#         print(response.text)
#
# if __name__ == '__main__':
#     p = Pool(parameters["times"])
#     for index in range(parameters["times"]):
#         p.apply_async(run_task, args=(index + 1,))
#
#     p.close()
#     p.join()
#     print("执行结束.")

# import time
# import requests
# from multiprocessing import Process
# from multiprocessing import Pool
#
# parameters = {
#     "times": 1, # 并发量
#     "url": "https://staging-portal-api.trademax.global/api/funding/transactions/assign",
#     "header": {
#     "Accept": "application/prs.CRM-Back-End.v2+json",
#     "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjY1MTIwYTBmNGExZjYyZGU1ODY2ODdhODU3NzE1YjljZDRjMDVmYzU3ZTMxYTk0NTc0OGY4MjljNTIxMDlkMjNkN2Q0Y2I5MTU3MGQ1NTlmIn0.eyJhdWQiOiIxIiwianRpIjoiNjUxMjBhMGY0YTFmNjJkZTU4NjY4N2E4NTc3MTViOWNkNGMwNWZjNTdlMzFhOTQ1NzQ4ZjgyOWM1MjEwOWQyM2Q3ZDRjYjkxNTcwZDU1OWYiLCJpYXQiOjE1NjYwMjQ1MzYsIm5iZiI6MTU2NjAyNDUzNiwiZXhwIjoxNTY2NjI5MzM2LCJzdWIiOiIyOSIsInNjb3BlcyI6WyIqIl19.N2yK-MVOj1bx9O6pVi_M0JjnqhsK9DoZ9tQgrCyUha4J1j8ZnTTVSBQR5f-YmZ3YysOD8_Zx9DclA_lA9CjIOK_Tl7UMhqe7JVXjnsxeiXmkDc5rDL5OQ_HoF66MLxwx3lOadl2wh0nK9HOeHtFa7MyzF2T8V01yXnEjS1HPoBOwJNr7JC7jIhB7xN-dnwOA3H2WC91_b4D-kky9Oj1fcB6L7_Qsu2Rg7iZ44pRZ8uREQpDoEtHmdQPtvamQ4PuXMU7WKvhESHGJ4fTiOGe6tOVknhjibHuGUchLqr5R9gwVv05tgzXB-XRT0BIckrdjgbB0w18W5s4ofckjNBSiiORXTiC2WvhuC2fqdxwJfa85WR05xLBD7yDfwLBSnQqiC-llH2xlaav0kynUDi5Hl4sDpTZtzNtpVoO96IsACHogtgeDXsj6STcB9kOQ_l2GXWAJ_rntVcHqqKbAp8-HVtp8yjtdXXUOFMge88X6EshiFaKCO2pdRgvivwe5yHsCRRjjyuaEJ-qQ43wbLCD4rG5j_5Jy0iQt6IkKM0wk2Wld3ZkyC2HNImJwbDH7L2RIEqjxkE4ooNfNWZ7sxa9l4HeXorFJjit7blL4MPD8sGfNVKVJtyFxd0y6zCW5c9e01iP1_YAeuQT5HDpaYq63W1vSO9jRe5aJkTtTX8n4f8M",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
#     "Content-Type": "application/x-www-form-urlencoded",
#             }
# }
#
# def run_task(idx):
#     for i in (1,2):
#         data = {'action': i, 'transaction_id': 130,'notes':'notes_{}'.format(time.strftime('%Y-%m-%d %H_%M_%S'))}
#         response = requests.patch(url=parameters["url"], data=data, headers=parameters["header"])
#         if response.status_code == 204:
#             result = response.content.decode('utf-8')
#         else:
#             result = "访问失败"
#         print("第 %s 次执行：%s \n" % (idx, result))
#         print(response.text)
#
# if __name__ == '__main__':
#     p = Pool(parameters["times"])
#     for index in range(parameters["times"]):
#         p.apply_async(run_task, args=(index + 1,))
#
#     p.close()
#     p.join()
#     print("执行结束.")

# import time
# import requests
# from multiprocessing import Process
# from multiprocessing import Pool
#
# parameters = {
#     "times": 1, # 并发量
#     "url": "https://staging-portal-api.trademax.global/api/front/transactions/cancel",
#     "header": {
#     "Accept": "application/prs.CRM-Back-End.v2+json",
#     "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjY3YTRlOTgzMWMwODA4Y2MxYTIxMjZmMTk2ZDUwZWM3N2FlYzY5NDM5MjA0ZTJlZGYxNzUzMmZkMTBhMDllYzFjNzk2NTRlYmQxZDVjOGY0In0.eyJhdWQiOiIyIiwianRpIjoiNjdhNGU5ODMxYzA4MDhjYzFhMjEyNmYxOTZkNTBlYzc3YWVjNjk0MzkyMDRlMmVkZjE3NTMyZmQxMGEwOWVjMWM3OTY1NGViZDFkNWM4ZjQiLCJpYXQiOjE1NjYwMzA0NTgsIm5iZiI6MTU2NjAzMDQ1OCwiZXhwIjoxNTY2NjM1MjU4LCJzdWIiOiIxNSIsInNjb3BlcyI6WyIqIl19.L9f7JDXb1F-ajjsh_JKmo154QnwrL0EsY9SkWuEx4ybmEh_iR8nH1deCsIlktE2-fvCWiC9tH26N1KwpNgk99ysgb3nmakGsGyHa7vuze-MvqRcPLCBmRFtvKAgEJknLRz9v0z__AffcEW1YvPItzYNc_5KtLF1oT1XcMNy_z6uQH6GwdUV5sySYTe9l6ck-D5MVzYk2vpdf7z-AOIj0rg9m7eDtYsaicLw5cYkIH-1H6YUfMKIam8m0ec4RteYgLnwItE3V9sF4a66eBV32bcBKyCA0A3dHICMYPp03gXrxaokp3n_xuzDoY7sQny8oFPR58AqR_sNroFhQHPETvBYYlA3tNREPV_Os9ekar9CIONgi4ukkfxWIqY0dAssdC1gZmyLtzBvkvOA0XFpTNn5LJzH4XbzE_SzsNRIZcPVCugpC8vZyt75z2bbYm485mnARM02a_pHE_AT9W3Su8xEAsZKKyZTj1Mog2rbauwPdbWOhLrn0vBu9mnpodtKveNE2qDJcaaA5CQhqav4TjaW37Ny_vKYdlA43NOx2nikXdrj7n5p5O2iLi9A932oA1sadKSKFfiAsnwrSuPpztNhRQANxV4sx5A6B3hUIb6oGul3DHMi5doOtLvsxR0jZQC_IF3p_JSMVQamaBngNPk7JkacG4-eB-qryMUQEoj4",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
#     "Content-Type": "application/x-www-form-urlencoded",
#             }
# }
#
# def run_task(idx):
#     data = { 'transaction_id': 115}
#     response = requests.patch(url=parameters["url"], data=data, headers=parameters["header"])
#     if response.status_code == 204:
#         result = response.content.decode('utf-8')
#     else:
#         result = "访问失败"
#     print("第 %s 次执行：%s \n" % (idx, result))
#     print(response.text)
#
# if __name__ == '__main__':
#     p = Pool(parameters["times"])
#     for index in range(parameters["times"]):
#         p.apply_async(run_task, args=(index + 1,))
#
#     p.close()
#     p.join()
#     print("执行结束.")


# import time
# import requests
# from multiprocessing import Process
# from multiprocessing import Pool
#
# parameters = {
#     "times": 1,  # 并发量
#     "url": "https://staging-portal-api.trademax.global/api/front/fundings/withdrawal",
#     "header": {
#         "Accept": "application/prs.CRM-Back-End.v2+json",
#         "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6Ijg0NTYyODFlODYxYWUwMzU5MmFlN2FmNGFiYmEyNmQ5M2Q5OGYyMjI3MTUwNzc1ZGRmN2U3Y2Q0ZDVlNGY5ODM5ZGViY2IyODg4YTUzZTNkIn0.eyJhdWQiOiIyIiwianRpIjoiODQ1NjI4MWU4NjFhZTAzNTkyYWU3YWY0YWJiYTI2ZDkzZDk4ZjIyMjcxNTA3NzVkZGY3ZTdjZDRkNWU0Zjk4MzlkZWJjYjI4ODhhNTNlM2QiLCJpYXQiOjE1NjYwMTIyMTQsIm5iZiI6MTU2NjAxMjIxNCwiZXhwIjoxNTY2NjE3MDE0LCJzdWIiOiIxNSIsInNjb3BlcyI6WyIqIl19.UhU2Xvg5NorO7f3HB-9sUUtIT5kYY7pe_tLdI2Zc8GkchAJen6V4jRLiMUFzmmkctS3Ew1NIG86Dq1RLfWPnaAGOo8z0HlhV0lKweb49H3f_Crr8rAnDr_r8MQdQS18RvJ0kp6P_ebm2QSIsruD_5_IhO0zQHk1c_jI29t4H7Fn36QF2wLuibQm03hniBUHPSQUq8W76pKauZB14WKliem13yOqqazuY3s11A3353bEZklfiky9v1UGGv0Yn-f_XMA9VyGsArmnJvz61ZfH1FsU9sC-OP6uwl1wHWgTGBoH9_HyNj_qfpwsyFTzamdX1wIf8-AAeIlcZKJHQvahh1HBdMGTYHDulm68MoEI3DOPk7p0m3j8pKpvRsokjuQQ-CldfWl6lTo1kMX63Y20FTujyZpCZklxdra9ESTqjNjx8k6ChuMaLWmHxm_ie0bqBhqHCfjxbJIjOG8INvZQNqswMxNDH1jjselP5scbPwxKcA7JpWalayjApeOuIyyqyqxc31xWcFNCs74Y7-wavxfBhpeEcU_GMbslhAMgrbrFvSH5njOJjJrGKLvlC7ZyVZu9s3-PyELQEne-c8G2yyzfqPuK2Q1DbxYmc6v1DihkxlT6bcjMcxIhWeZ9dcQNxr1-9bA2g8egUXzqx5slxmHy3nbt7vMUvcV6T-WJ5Lv4",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
#         "Content-Type": "application/x-www-form-urlencoded",
#     }
# }
#
#
# def run_task(idx):
#     data = {'funding_method_id': '9',
#             'trading_server_id': 1,
#             'external_id': 316524,
#             'template': 'Skrill',
#             'fund_amount': 100,
#             'payment_currency': 'USD',
#             'name': '',
#             'bank_name': '',
#             'bank_account_number': '',
#             'BSB': '',
#             'swift_code': '',
#             'bank_address': '',
#             'soft_code': '',
#             'account_holder_address': '',
#             'account_holder_name': '1111',
#             'is_save': 0
#             }
#     response = requests.post(
#         url=parameters["url"],
#         data=data,
#         headers=parameters["header"])
#     if response.status_code == 204:
#         result = response.content.decode('utf-8')
#     else:
#         result = "访问失败"
#     print("第 %s 次执行：%s \n" % (idx, result))
#     print(response.text)
#
#
# if __name__ == '__main__':
#     p = Pool(parameters["times"])
#     for index in range(parameters["times"]):
#         p.apply_async(run_task, args=(index + 1,))
#
#     p.close()
#     p.join()
#     print("执行结束.")


# import time
# import requests
# from multiprocessing import Process
# from multiprocessing import Pool
#
# parameters = {
#     "times": 1,  # 并发量
#     "url": "https://staging-portal-api.trademax.global/api/front/fundings/transfer",
#     "header": {
#         "Accept": "application/prs.CRM-Back-End.v2+json",
#         "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6Ijg0NTYyODFlODYxYWUwMzU5MmFlN2FmNGFiYmEyNmQ5M2Q5OGYyMjI3MTUwNzc1ZGRmN2U3Y2Q0ZDVlNGY5ODM5ZGViY2IyODg4YTUzZTNkIn0.eyJhdWQiOiIyIiwianRpIjoiODQ1NjI4MWU4NjFhZTAzNTkyYWU3YWY0YWJiYTI2ZDkzZDk4ZjIyMjcxNTA3NzVkZGY3ZTdjZDRkNWU0Zjk4MzlkZWJjYjI4ODhhNTNlM2QiLCJpYXQiOjE1NjYwMTIyMTQsIm5iZiI6MTU2NjAxMjIxNCwiZXhwIjoxNTY2NjE3MDE0LCJzdWIiOiIxNSIsInNjb3BlcyI6WyIqIl19.UhU2Xvg5NorO7f3HB-9sUUtIT5kYY7pe_tLdI2Zc8GkchAJen6V4jRLiMUFzmmkctS3Ew1NIG86Dq1RLfWPnaAGOo8z0HlhV0lKweb49H3f_Crr8rAnDr_r8MQdQS18RvJ0kp6P_ebm2QSIsruD_5_IhO0zQHk1c_jI29t4H7Fn36QF2wLuibQm03hniBUHPSQUq8W76pKauZB14WKliem13yOqqazuY3s11A3353bEZklfiky9v1UGGv0Yn-f_XMA9VyGsArmnJvz61ZfH1FsU9sC-OP6uwl1wHWgTGBoH9_HyNj_qfpwsyFTzamdX1wIf8-AAeIlcZKJHQvahh1HBdMGTYHDulm68MoEI3DOPk7p0m3j8pKpvRsokjuQQ-CldfWl6lTo1kMX63Y20FTujyZpCZklxdra9ESTqjNjx8k6ChuMaLWmHxm_ie0bqBhqHCfjxbJIjOG8INvZQNqswMxNDH1jjselP5scbPwxKcA7JpWalayjApeOuIyyqyqxc31xWcFNCs74Y7-wavxfBhpeEcU_GMbslhAMgrbrFvSH5njOJjJrGKLvlC7ZyVZu9s3-PyELQEne-c8G2yyzfqPuK2Q1DbxYmc6v1DihkxlT6bcjMcxIhWeZ9dcQNxr1-9bA2g8egUXzqx5slxmHy3nbt7vMUvcV6T-WJ5Lv4",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
#         "Content-Type": "application/x-www-form-urlencoded",
#     }
# }
#
#
# def run_task(idx):
#     data = {'from_external_id':316526,
#             'from_trading_server_id':1,
#             'to_external_id':316523,
#             'to_trading_server_id':1,
#             'fund_currency':'USD',
#             'fund_amount':'100.00'}
#     response = requests.post(
#         url=parameters["url"],
#         data=data,
#         headers=parameters["header"])
#     if response.status_code == 204:
#         result = response.content.decode('utf-8')
#     else:
#         result = "访问失败"
#     print("第 %s 次执行：%s \n" % (idx, result))
#     print(response.text)
#
#
# if __name__ == '__main__':
#     p = Pool(parameters["times"])
#     for index in range(parameters["times"]):
#         p.apply_async(run_task, args=(index + 1,))
#
#     p.close()
#     p.join()
#     print("执行结束.")


# import time
# import requests
# from multiprocessing import Process
# from multiprocessing import Pool
#
# parameters = {
#     "times": 1,  # 并发量
#     "url": "https://staging-portal-api.trademax.global/api/front/agree",
#     "header": {
#         "Accept": "application/prs.CRM-Back-End.v2+json",
#         "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6Ijg0NTYyODFlODYxYWUwMzU5MmFlN2FmNGFiYmEyNmQ5M2Q5OGYyMjI3MTUwNzc1ZGRmN2U3Y2Q0ZDVlNGY5ODM5ZGViY2IyODg4YTUzZTNkIn0.eyJhdWQiOiIyIiwianRpIjoiODQ1NjI4MWU4NjFhZTAzNTkyYWU3YWY0YWJiYTI2ZDkzZDk4ZjIyMjcxNTA3NzVkZGY3ZTdjZDRkNWU0Zjk4MzlkZWJjYjI4ODhhNTNlM2QiLCJpYXQiOjE1NjYwMTIyMTQsIm5iZiI6MTU2NjAxMjIxNCwiZXhwIjoxNTY2NjE3MDE0LCJzdWIiOiIxNSIsInNjb3BlcyI6WyIqIl19.UhU2Xvg5NorO7f3HB-9sUUtIT5kYY7pe_tLdI2Zc8GkchAJen6V4jRLiMUFzmmkctS3Ew1NIG86Dq1RLfWPnaAGOo8z0HlhV0lKweb49H3f_Crr8rAnDr_r8MQdQS18RvJ0kp6P_ebm2QSIsruD_5_IhO0zQHk1c_jI29t4H7Fn36QF2wLuibQm03hniBUHPSQUq8W76pKauZB14WKliem13yOqqazuY3s11A3353bEZklfiky9v1UGGv0Yn-f_XMA9VyGsArmnJvz61ZfH1FsU9sC-OP6uwl1wHWgTGBoH9_HyNj_qfpwsyFTzamdX1wIf8-AAeIlcZKJHQvahh1HBdMGTYHDulm68MoEI3DOPk7p0m3j8pKpvRsokjuQQ-CldfWl6lTo1kMX63Y20FTujyZpCZklxdra9ESTqjNjx8k6ChuMaLWmHxm_ie0bqBhqHCfjxbJIjOG8INvZQNqswMxNDH1jjselP5scbPwxKcA7JpWalayjApeOuIyyqyqxc31xWcFNCs74Y7-wavxfBhpeEcU_GMbslhAMgrbrFvSH5njOJjJrGKLvlC7ZyVZu9s3-PyELQEne-c8G2yyzfqPuK2Q1DbxYmc6v1DihkxlT6bcjMcxIhWeZ9dcQNxr1-9bA2g8egUXzqx5slxmHy3nbt7vMUvcV6T-WJ5Lv4",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
#         "Referer":"https://staging-portal.trademax.global/agreements-documents"
#
#     }
# }
#
#
# def run_task(idx):
#     data = {'agreement_id': '7'}
#     response = requests.get(
#         url=parameters["url"],
#         data=data,
#         headers=parameters["header"])
#     if response.status_code == 204:
#         result=response.content.decode('utf-8')
#     else:
#         result="访问失败"
#     print("第 %s 次执行：%s \n" % (idx, result))
#     print(response.text)
#
#
# if __name__ == '__main__':
#     p=Pool(parameters["times"])
#     for index in range(parameters["times"]):
#         p.apply_async(run_task, args=(index + 1,))
#
#     p.close()
#     p.join()
#     print("执行结束.")


# import time
# import requests
# from multiprocessing import Process
# from multiprocessing import Pool
#
# parameters = {
#     "times": 1,  # 并发量
#     "url": "https://staging-portal-api.trademax.global/api/front/tradingAccounts/leverageChange",
#     "header": {
#         "Accept": "application/prs.CRM-Back-End.v2+json",
#         "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjJkZDNmMWYxYjQ3Njk1NzM0OTExODk2MGE2ODEyOGQ1OTI4NzhjYmM3MjA4M2FmMTg3YzNiNDQxZTllY2E5NGJmNjExZTA2NTk3NTRiMTBlIn0.eyJhdWQiOiIyIiwianRpIjoiMmRkM2YxZjFiNDc2OTU3MzQ5MTE4OTYwYTY4MTI4ZDU5Mjg3OGNiYzcyMDgzYWYxODdjM2I0NDFlOWVjYTk0YmY2MTFlMDY1OTc1NGIxMGUiLCJpYXQiOjE1NjYwNDYxNTUsIm5iZiI6MTU2NjA0NjE1NSwiZXhwIjoxNTY2NjUwOTU1LCJzdWIiOiIxNSIsInNjb3BlcyI6WyIqIl19.dwz5ZgNJbGPEAW8WdM-0c7bkzyoLqAjLS2M1-TGxPN_-saD0ABz9YCrmIjwC-CwnzpuZTebBWwmL3t6uN9xr0d1Uom03qAHHePnKn-p-HeWnc1EDkIAJpbdt5fsZzSVU81rDywqEi-klHl_hu60J4zjzVIMNA5y2zsOWJFwfBkyj3oabgMYgCynXmjDVZ4x3l0YWLKi4dfK1JVy8nm0CaFAtsEiGcXrH0PncO8yYRVlTqvnf5NcGIkqdmgbGc-ZxbilQcC1lljUS_eRXx1l31JPh0A7RaBUdUEo5rTYo3cXuK0V7RDs5JSIZ9DhO_PDoA_LT0MpUY-XyTrY3x_RWBH4it-CHPuKf9hfGkQCXJMBWiht0Ij760qNVIbSCPbQieOagx_Zu7P11ZWtBXAUjBFfPBsg6kXOR54yI2ZH0lSKc5Ftu3uweD5poOYB4CkH8CAFoPXYoauZS9PwJRKN89LdFYuDZwmUglUrzR2UNqUyllp_RjQpya23eNbh-8SsAM6oPmQrxLkHcsGkbQnSmP7OTmJdFT5S3k7ezj1-ZareaWbap1cAWFLX3Z6ge0IuDA4SD-aZwiEgOLGvf303wUJxbibhfl5mO7baNSjcJ7y2qyqvTOIWly5p-tyv8DQiGuGNPJi5dLGoe4RbDZMiBrBDTsbcgD5dD-4lC3QmPeYQ",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
#         "Content-Type": "application/x-www-form-urlencoded",
#     }
# }
#
#
# def run_task(idx):
#     data = {'user_id':15,
#             'trading_account_id':15,
#             'trading_server_id':1,
#             'change_leverage':1,
#             }
#     response = requests.post(
#         url=parameters["url"],
#         data=data,
#         headers=parameters["header"])
#     if response.status_code == 200:
#         result = response.content.decode('utf-8')
#     else:
#         result = "访问失败"
#     print("第 %s 次执行：%s \n" % (idx, result))
#     print(response.text)
#
#
# if __name__ == '__main__':
#     p = Pool(parameters["times"])
#     for index in range(parameters["times"]):
#         p.apply_async(run_task, args=(index + 1,))
#
#     p.close()
#     p.join()
#     print("执行结束.")

# import time
# import requests
# from multiprocessing import Process
# from multiprocessing import Pool
#
# parameters = {
#     "times": 1,  # 并发量
#     "url": "https://staging-portal-api.trademax.global/api/front/leverageChanges/cancel",
#     "header": {
#         "Accept": "application/prs.CRM-Back-End.v2+json",
#         "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjU5MTNkNmYyZjIxMzg3MzBjNDkzMjhmMzU0MmE3NWYzOGNmNjBlNjZjOTBhMGM1MDM1MTE0NzIzYmY4NDAwYWQ3MDRkZDZjOTY5MTExNjgzIn0.eyJhdWQiOiIyIiwianRpIjoiNTkxM2Q2ZjJmMjEzODczMGM0OTMyOGYzNTQyYTc1ZjM4Y2Y2MGU2NmM5MGEwYzUwMzUxMTQ3MjNiZjg0MDBhZDcwNGRkNmM5NjkxMTE2ODMiLCJpYXQiOjE1NjYxODA1NzQsIm5iZiI6MTU2NjE4MDU3NCwiZXhwIjoxNTY2Nzg1Mzc0LCJzdWIiOiIxNSIsInNjb3BlcyI6WyIqIl19.EQ0o_C8KaEAOObirtb9rVKwSaQg-WWpA2zQcdqKyVsb7Qbwt7Ilvtjc1dRGaKnaaYC83tZNElvRanfXqvnm6pmRj2ZLZru-IIc7WBcJmHgUa9iVxTZ_3IebMCvT_L6ohYjDxQaH75ECeb-IMzMbfXj_ncgurjudvE8Ru25FirEcGnMBx952J2NNO_tHt2OFv2qKPXYT_IGB5VILaoen5loJHgj2KQ8UPnENW68hXlABct0RsR5wy-QlP7MzMfRByRhauB4xOzSsO1_vUHqAuMu2EwUG2vYLrAbg_xcNd5yj1Kh_VfR4kQ7rZta0JNWqFduFhnm8kH4unqs2tcvrT158HYQJgwJ4GiSCm5rBTYD6S1b3xhY5HNAbmfpJzJ5EVGOWgm904ECkI9NYmG10bgBbIjezdzllfn_cuagjsacIGgNDSbXOnpBwAYqK8Lr9WbwR_3Xsra_Nm2Uu664IzLEV_0hsQxmC8flwKvcKByZkqPsv-iX5fbTXnAeKwkK9bFrbZMOoudQHipXdn6BKH3PYLqvWoSqK4T7k-W2F_IPAKBwwkK8CEAD8FYilvWdV3ayyCuMUlXR-uvFjHpezfj9_rNl3W4LaXuAr-kFlQs7xp1y3t2k3B4KZpdr1zPYQ8CCiOwI_6PihGN3cXnyR0eXtkhFwJiidDT9pUCSj7yfE",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
#         "Content-Type": "application/x-www-form-urlencoded",
#     }
# }
#
#
# def run_task(idx):
#     data = {'leverage_change_id':13
#             }
#     response = requests.post(
#         url=parameters["url"],
#         data=data,
#         headers=parameters["header"])
#     if response.status_code == 204:
#         result = response.content.decode('utf-8')
#     else:
#         result = "访问失败"
#     print("第 %s 次执行：%s \n" % (idx, result))
#     print(response.text)
#
#
# if __name__ == '__main__':
#     p = Pool(parameters["times"])
#     for index in range(parameters["times"]):
#         p.apply_async(run_task, args=(index + 1,))
#
#     p.close()
#     p.join()
#     print("执行结束.")


# import time
# import requests
# from multiprocessing import Process
# from multiprocessing import Pool
#
# parameters = {
#     "times": 1,  # 并发量
#     "url": "https://staging-portal-api.trademax.global/api/front/leverageChanges/cancel",
#     "header": {
#         "Accept": "application/prs.CRM-Back-End.v2+json",
#         "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjU5MTNkNmYyZjIxMzg3MzBjNDkzMjhmMzU0MmE3NWYzOGNmNjBlNjZjOTBhMGM1MDM1MTE0NzIzYmY4NDAwYWQ3MDRkZDZjOTY5MTExNjgzIn0.eyJhdWQiOiIyIiwianRpIjoiNTkxM2Q2ZjJmMjEzODczMGM0OTMyOGYzNTQyYTc1ZjM4Y2Y2MGU2NmM5MGEwYzUwMzUxMTQ3MjNiZjg0MDBhZDcwNGRkNmM5NjkxMTE2ODMiLCJpYXQiOjE1NjYxODA1NzQsIm5iZiI6MTU2NjE4MDU3NCwiZXhwIjoxNTY2Nzg1Mzc0LCJzdWIiOiIxNSIsInNjb3BlcyI6WyIqIl19.EQ0o_C8KaEAOObirtb9rVKwSaQg-WWpA2zQcdqKyVsb7Qbwt7Ilvtjc1dRGaKnaaYC83tZNElvRanfXqvnm6pmRj2ZLZru-IIc7WBcJmHgUa9iVxTZ_3IebMCvT_L6ohYjDxQaH75ECeb-IMzMbfXj_ncgurjudvE8Ru25FirEcGnMBx952J2NNO_tHt2OFv2qKPXYT_IGB5VILaoen5loJHgj2KQ8UPnENW68hXlABct0RsR5wy-QlP7MzMfRByRhauB4xOzSsO1_vUHqAuMu2EwUG2vYLrAbg_xcNd5yj1Kh_VfR4kQ7rZta0JNWqFduFhnm8kH4unqs2tcvrT158HYQJgwJ4GiSCm5rBTYD6S1b3xhY5HNAbmfpJzJ5EVGOWgm904ECkI9NYmG10bgBbIjezdzllfn_cuagjsacIGgNDSbXOnpBwAYqK8Lr9WbwR_3Xsra_Nm2Uu664IzLEV_0hsQxmC8flwKvcKByZkqPsv-iX5fbTXnAeKwkK9bFrbZMOoudQHipXdn6BKH3PYLqvWoSqK4T7k-W2F_IPAKBwwkK8CEAD8FYilvWdV3ayyCuMUlXR-uvFjHpezfj9_rNl3W4LaXuAr-kFlQs7xp1y3t2k3B4KZpdr1zPYQ8CCiOwI_6PihGN3cXnyR0eXtkhFwJiidDT9pUCSj7yfE",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
#         "Content-Type": "application/x-www-form-urlencoded",
#     }
# }
#
#
# def run_task(idx):
#     data = {'leverage_change_id':13
#             }
#     response = requests.post(
#         url=parameters["url"],
#         data=data,
#         headers=parameters["header"])
#     if response.status_code == 204:
#         result = response.content.decode('utf-8')
#     else:
#         result = "访问失败"
#     print("第 %s 次执行：%s \n" % (idx, result))
#     print(response.text)
#
#
# if __name__ == '__main__':
#     p = Pool(parameters["times"])
#     for index in range(parameters["times"]):
#         p.apply_async(run_task, args=(index + 1,))
#
#     p.close()
#     p.join()
#     print("执行结束.")
# def register():
#     parameters = {
#         "url" : "https://staging-portal-api.trademax.global/api/registerFour",
#         "header" : {
#         "Accept": "application/prs.CRM-Back-End.v2+json",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
#         "Content-Type": "application/x-www-form-urlencoded"}
#     }
#     for i in range(102,1000):
#         data = {
#         "first_name": "li",
#         "last_name": "ya{}".format(i),
#         "email": "yali{}@qq.com".format(i),
#         "mobile": "18908389434",
#         "country": "China",
#         "country_code": "+86",
#         "title": "Mr",
#         "gender": "Male",
#         "birthday": "1980-02-04",
#         "postcode": "123",
#         "address": "a",
#         "city": "b",
#         "state": "c",
#         "language": "en",
#         "promotion": "bbbb1111",
#         "third[ID]": "identification_card",
#         "third[title]": "Mr",
#         "third[number]": "350524198901082000",
#         "third[first_name_cn]": "力",
#         "third[last_name_cn]": "压",
#         "trading_server_id": "1",
#         "questions[0][question_id]": "67",
#         "questions[0][subject]": "Financial Details Q1",
#         "questions[0][answer_status]": "1",
#         "questions[0][description]": "<p>What is your current employment status?</p>",
#         "questions[0][options]": '[{"key":"Option 1","value":"Employed","status":1},{"key":"Option 2","value":"Self-employed","status":0},{"key":"Option 3","value":"Retired","status":0},{"key":"Option 4","value":"Student","status":0},{"key":"Option 5","value":"Unemployed","status":0}]',
#         "questions[1][question_id]": "68",
#         "questions[1][subject]": "Financial Details Q2",
#         "questions[1][answer_status]": "1",
#         "questions[1][description]": "<p>If you are employed/self-employed, which industry/sector are you working in?</p>",
#         "questions[1][options]": '[{"key":"Option 1","value":"Accounting","status":0},{"key":"Option 2","value":"Agriculture","status":0},{"key":"Option 3","value":"Banking & Finance                                                   ","status":0},{"key":"Option 4","value":"Catering Hospitality","status":0},{"key":"Option 5","value":"Construction & Property","status":0},{"key":"Option 6","value":"Customer Service","status":0},{"key":"Option 7","value":"Education","status":0},{"key":"Option 8","value":"Engineering","status":0},{"key":"Option 9","value":"Health","status":1},{"key":"Option 10","value":"Human Resources","status":0},{"key":"Option 11","value":"Induatrials","status":0},{"key":"Option 12","value":"Legal","status":0},{"key":"Option 13","value":"Leisure","status":0},{"key":"Option 14","value":"Management","status":0},{"key":"Option 15","value":"Marketing","status":0},{"key":"Option 16","value":"Media","status":0},{"key":"Option 17","value":"Public Sector","status":0},{"key":"Option 18","value":"Retailing","status":0},{"key":"Option 19","value":"Sales","status":0},{"key":"Option 20","value":"Support Services","status":0},{"key":"Option 21","value":"Information Technology","status":0},{"key":"Option 22","value":"Transport","status":0},{"key":"Option 23","value":"Military","status":0},{"key":"Option 24","value":"Others","status":0},{"key":"Option 25","value":"Not Applicable","status":0}]',
#         "questions[2][question_id]": "69",
#         "questions[2][subject]": "Financial Details Q3",
#         "questions[2][answer_status]": "0",
#         "questions[2][description]": "<p>What is your position? (Optional)</p>",
#         "questions[2][options]": '[{"key":"Answer","value":"d","status":1}]',
#         "questions[3][question_id]": "80",
#         "questions[3][subject]": "Financial Knowledge Q6",
#         "questions[3][answer_status]": "1",
#         "questions[3][description]": "<p><strong style='color: rgb(51, 51, 51);'>Which of the following statements best describe high volatility?</strong></p>",
#         "questions[3][options]": '[{"key":"Option 1","value":"When price fluctuates in a very wide range within a short period of time.","status":1},{"key":"Option 2","value":"When price fluctuates in a very narrow range within a long period of time.","status":0},{"key":"Option 3","value":"A term used to describe a price decrease.","status":0},{"key":"Option 4","value":"None of the above.","status":0}]',
#         "captcha_code": "ubp3e",
#         "captcha_key": "captcha-register-aaF7mRuNQvFaJ9x",
#         "account_type": "21",
#         "currency_id": "1",
#         "leverage": "200",
#         "password": "Lb123456",
#         "is_confirm": "1",
#         "is_read": "1",
#         "is_subscribe": "0"
#         }
#
#         response = requests.post(
#                 url=parameters["url"],
#                 data=data,
#                 headers=parameters["header"],
#         )
#         print(response.content.decode('utf-8'))
#
# if __name__ == '__main__':
#     register()
#     print("执行结束")

import time
import requests
from multiprocessing import Process
from multiprocessing import Pool

# parameters = {
#     "times": 100,  # 并发量
#     "url": "https://staging-portal-api.trademax.global/api/front/tradingAccounts/create",
#     "header": {
#         "Accept": "application/prs.CRM-Back-End.v2+json",
#         "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImE2ODY2ODViNjBjZTNlMDRkMzE3MGY1MWIwZWUxODlkZDg1Y2Q3ZDQzY2Q3Y2U3YmY3Yzg5MjU1ZTgyYWM4MWU1MWI1OWUyYmVlNTVlYjIyIn0.eyJhdWQiOiIyIiwianRpIjoiYTY4NjY4NWI2MGNlM2UwNGQzMTcwZjUxYjBlZTE4OWRkODVjZDdkNDNjZDdjZTdiZjdjODkyNTVlODJhYzgxZTUxYjU5ZTJiZWU1NWViMjIiLCJpYXQiOjE1NzEwMzU0OTUsIm5iZiI6MTU3MTAzNTQ5NSwiZXhwIjoxNTcxNjQwMjk1LCJzdWIiOiI3NjIiLCJzY29wZXMiOlsiKiJdfQ.kdSbWQUiLcEK8qcMlvn5l7i5YFhsEo0t0K81zEsX8d8jwPm84OfBVCvJ_ON_XMwU8qIeBKkmzYg99DKx4LRG90Urzd7ZJqf2kxufEUfM4P1rtBgVoJTgNAceJ10SZu3X9jkG6gZbGRWVOaElIKrXBZacDalvibRz9RdlXzN_BkhRCyK2APWqAx1gy64RGLoqi8kDInsg4ILwSzQ8d2iVNl_iWnGe3zwzS2awDGvHfjKLu4XIES7YC5C0iMjsM_MgtMQyCt8au3YxgNa9j2rNkMapNR2_nukltuvMwO5EN70U0ECuUgIaphQff3GF9xnV2ECd55W4sVhdy7l5AYEFqmN2RfOKaErc3ZcMlsL_vzzfUx9hawEsS56qg9rq9QkvpnoZuQEx40oVIr77pDcgfPEtaKgMgV2ZMdjDD2LZn6kcoZf8OFISvlQdSg1dESarbpKi8q3LZ8TBc8oq7yIlUvnrKAFj92M7okWWxM4A55k2l9Rgb_6VG5ZeMyNkJNT5_EypMuat0O2_fSzSz1BiU2McGJEbrFLVCTbCir1x9HpKvwH9ToXkVSgbTE5HXbHQ1VHxDSOS7zvGvPCAFQud-_Uwb0fhtAg7MpITEhZ8hImYM61sOFsMChg-LEC9F-H4KmWc97QszHJzXaAadXDHNNAYc7A2XSs8BcdUobVNZQw",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36",
#         "Content-Type": "application/x-www-form-urlencoded",
#     }
# }
#
# def createTA():
#     data = {"trading_server_id":1,"leverage":5,"master_password":"Lb123456","master_password_confirmation":"Lb123456"}
#
#     for i in range(100):
#         response = requests.post(
#             url=parameters["url"],
#             data=data,
#             headers=parameters["header"])
#         if response.status_code == 200:
#             result = response.content.decode('utf-8')
#         else:
#             result = "访问失败"
#         print("第 %s 次执行：%s \n" % (i, result))
#         # print(response.text)
#         time.sleep(0.2)
#
# if __name__ == '__main__':
#     createTA()

# def run_task(idx):
#     data = {"trading_server_id":1,"leverage":5,"master_password":"Lb123456","master_password_confirmation":"Lb123456"}
#     response = requests.post(
#         url=parameters["url"],
#         data=data,
#         headers=parameters["header"])
#     if response.status_code == 200:
#         result = response.content.decode('utf-8')
#     else:
#         result = "访问失败"
#     print("第 %s 次执行：%s \n" % (idx, result))
#     print(response.text)
#
#
# if __name__ == '__main__':
#     p = Pool(parameters["times"])
#     for index in range(parameters["times"]):
#         p.apply_async(run_task, args=(index + 1,))
#
#     p.close()
#     p.join()
#     print("执行结束.")