import undetected_chromedriver as uc
import argparse
from util import page_handler
from util import text_handler


# parser = argparse.ArgumentParser()
# parser.add_argument('target', type=str)
# args = parser.parse_args()
# target = args.target + '/review'
# print(target)
# driver = uc.Chrome(use_subprocess=False)
# driver.get(target)
# print(page_handler.get_comments(driver))

result = text_handler.get_tag("Ibu pergi ke pasar yang jauh di hari yang panas.........")