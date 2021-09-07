from bs4 import BeautifulSoup
from urllib.request import urlopen
import json,re
import asyncio
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import database
class cardSakura():
    def __init__(self,id,name,sign,magicType,capturedAnime,capturedManga,transformedAnime,transformedManga,link_img_clow,link_img_sakura):
        self.id = id
        self.name = name
        self.sign = sign
        self.magicType = magicType
        self.capturedAnime = capturedAnime
        self.capturedManga = capturedManga
        self.transformedAnime = transformedAnime
        self.transformedManga = transformedManga
        self.link_img_clow = link_img_clow
        self.link_img_sakura = link_img_sakura
    def to_dict(self):
        return {
            'id': self.id,
            'nameCard': self.name,
            'sign': self.sign,
            'magicType': self.magicType,
            'capturedAnime': self.capturedAnime,
            'capturedManga': self.capturedManga,
            'transformedAnime': self.transformedAnime,
            'transformedManga': self.transformedManga,
            'link_clow': self.link_img_clow,
            'link_sakura': self.link_img_sakura
        }
    def get_list_cards():
        url = f"https://ccsakura.fandom.com/api.php?action=parse&page=Clow_Cards&prop=wikitext&formatversion=2&format=json"
        respone = urlopen(url)
        data = json.loads(respone.read())
        wikitext = data['parse']['wikitext']
        str_list_card = wikitext[wikitext.find("List of Cards"):wikitext.find("</gallery>")]
        pattern = "\[\[(.*?)\]\]"
        list_cards = re.findall(pattern, str_list_card)
        return list_cards
    def get_info_cards(card_name):
        card_name = '_'.join(card_name.split())
        url = f"https://ccsakura.fandom.com/api.php?action=parse&page={card_name}&prop=wikitext&formatversion=2&format=json"
        respone = urlopen(url)
        data = json.loads(respone.read())
        wikitext = data['parse']['wikitext']
        pattern = "\[\[(.*?)\]\]"
        list_image_str = re.findall(pattern,wikitext[wikitext.find("image"):wikitext.find("caption")])
        image_clow_file = list_image_str[0].split("|")[0].split(":")[1]
        image_sakura_file = list_image_str[1].split("|")[0].split(":")[1]
        sign = re.findall(pattern,wikitext[wikitext.find("sign"):wikitext.find("hiegherarchy")])[0].split("|")[1]
        magic_type = " ".join(wikitext[wikitext.find("magic type"):wikitext.find("captured")].split()[3:5])
        captured_transform_list = list(wikitext[wikitext.find("captured ep"):wikitext.find("}}")].replace("[","").replace("]","").split("|"))
        captured_ep = "N/A"
        captured_ch = "N/A"
        transformed_ep = "N/A"
        transformed_ch = "N/A"
        for i in range(len(captured_transform_list)):
            if captured_transform_list[i].find("captured ep") != -1:
                captured_ep = captured_transform_list[i].split("=")[1]
            elif captured_transform_list[i].find("transformed ep") != -1:
                transformed_ep =captured_transform_list[i].split("=")[1]
            elif captured_transform_list[i].find("captured ch") != -1:
                captured_ch = captured_transform_list[i].split("=")[1]
            elif captured_transform_list[i].find("transformed ch") != -1:
                transformed_ch =captured_transform_list[i].split("=")[1]
        return {
            'nameCard': card_name.replace("_"," "),
            'sign': sign,
            'magicType': magic_type,
            'capturedAnime': captured_ep,
            'capturedManga': captured_ch,
            'transformedAnime': transformed_ep,
            'transformedManga': transformed_ch,
            'link_clow': f"https://ccsakura.fandom.com/wiki/Special:Redirect/file/{image_clow_file}?width=326",
            'link_sakura': f"https://ccsakura.fandom.com/wiki/Special:Redirect/file/{image_sakura_file}?width=326"
        }
    def create_list_sakura():
        card_sakura_db = {'card':[]}
        list_cards = cardSakura.get_list_cards()
        for i in range(len(list_cards)):
            card_info = cardSakura.get_info_cards(list_cards[i])
            card = cardSakura(
                i+1,
                card_info['nameCard'],
                card_info['sign'],
                card_info['magicType'],
                card_info['capturedAnime'],
                card_info['capturedManga'],
                card_info['transformedAnime'],
                card_info['transformedManga'],
                card_info['link_clow'],
                card_info['link_sakura']
            )
            card_sakura_db['card'].append(card.to_dict())
        return card_sakura_db
        
        