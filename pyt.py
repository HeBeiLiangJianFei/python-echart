import pytesseract
import  requests
from lxml import etree
from PIL import Image
import urllib.request
# url = "https://accounts.douban.com/login"
# headers = {"User-Agent":"Mozilla/5.0"}
#
# rep = requests.get(url,headers)
# rep.encoding = rep.apparent_encoding
# html = rep.text
# #
# #
# #
# #
# # 使用lxml获取验证码图片链接

# result = etree.HTML(html)
# s = result.xpath('//*[@id="captcha_image"]/@src')[0]
# urllib.request.urlretrieve(s,"y.jpg")
image = Image.open("D:\Scrapy框架的使用\瞎搞\y.png")
print(image)
s = pytesseract.image_to_string(image)
print("S-->",s)
