
import hashlib
import requests

page = requests.get('https://labs.nobitex.ir/')
page_digi = page.text.encode('utf-8')
sipi = hashlib.sha256(page_digi).hexdigest()
bipi = hashlib.blake2b(page.text.encode('utf-8'), digest_size=64).hexdigest()
print(sipi,'\nand blake2B:\n',bipi)