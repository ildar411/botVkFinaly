import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import requests
from vk_api.utils import get_random_id
import time
from lxml import html
from parserOldPrintMipt import ParserPrint



def print_info(info):
    for inf in info:
        print(inf)

def parse_print():
    p_obj = ParserPrint()
    return p_obj

def vk_bot():
    asd = []
    info = []
    info2 = []
    status = []
    trigger = 0
    clients = ['248950122', '58917585', '32298906', '168272786']
    session = requests.Session()
    vkSession = vk_api.VkApi(token = token1)
    vk = vkSession.get_api()
    longpoll = VkLongPoll(vkSession)
    lists = []
    for event in longpoll.listen():
        info = []
        info.clear()
        time.sleep(600)
        status = ParserPrint()
        for stat in status:
            if stat not in lists:
                print(stat, " NOT in list")
                info.append('Printer: ' + stat.get('Printer') + 
                        '\n Status: ' + stat.get('Status') +
                        '\n Error: ' + stat.get('Error') +
                        '\n Paper: ' + stat.get('Paper'))    
                trigger = 1
        if lists != status:
            print("!=")
            print_info(info)
            lists = status
        else:
            print("list = status")
        
             

        for stat in status:    
            info2.append('Printer: ' + stat.get('Printer') + 
                        '\n Status: ' + stat.get('Status') +
                        '\n Error: ' + stat.get('Error') +
                        '\n Paper: ' + str(stat.get('Paper')))

        
    
        for client in clients:
            for inf in info:    
                vk.messages.send(
                    user_id = client,#event.user_id,#'248950122',
                    random_id = get_random_id(),
                    message = inf
                )
            if trigger == 1:
                vk.messages.send(
                    user_id = client,
                    random_id = get_random_id(),
                    message = '**********\n**********\n'                                                                          
                    )

            print(client)
            trigger = 0
        continue

        
        
        
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            print('id{}: "{}"'.format(event.user_id, event.text), end=" ")
            #status = ParserPrint()
            for inf in info2:     
                vk.messages.send(
                    user_id = event.user_id ,#'248950122', #event.user_id
                    random_id = get_random_id(),
                    message = inf
                )
                vk.messages.send(
                    user_id = event.user_id,
                    random_id = get_random_id(),
                    message = "***********\n*******\n"
                )
            print('no result')
            continue
                    
    
            #отправка ильдару
            #status = ParserPrint()
        
      
try:        
    vk_bot()
except:
    vk_bot()









"""
i = 0
        trigger = 0
        if len(status) == len(lists):
            while i < len(status):
                if not(lists[i].get('Printer') == status[i].get('Printer') and 
                    lists[i].get('Status') == status[i].get('Status') and 
                    lists[i].get('Paper') == status[i].get('Paper')):   
                    info.append("Printer: " + status[i].get('Printer') +
                                    "\n Status: " + status[i].get('Status') +
                                    "\n Error: " + status[i].get('Error') +
                                    "\n Paper: " + status[i].get('Paper'))
                    trigger = 1
                i += 1
                if i == 1:
                    lists = status
        elif len(status) > len(lists):
            while i < len(lists):
                if not(lists[i].get('Printer') == status[i].get('Printer') and 
                    lists[i].get('Status') == status[i].get('Status') and 
                    lists[i].get('Paper') == status[i].get('Paper')):
                        
                    #info.append("Printer: " + status[i].get('Printer') +
                     #               "\n Status: " + status[i].get('Status') +
                      #              "\n Error: " + status[i].get('Error') +
                       #             "\n Paper: " + status[i].get('Paper'))
                    trigger = 1
                i += 1
                if i == 1:
                    lists = status
            while i < len(status):
                
                info.append("Printer: " + status[i].get('Printer') +
                                    "\n Status: " + status[i].get('Status') +
                                    "\n Error: " + status[i].get('Error') +
                                    "\n Paper: " + status[i].get('Paper'))
                
                i += 1
            lists = status
        elif len(status) < len(lists):
            while i < len(status):
                if not(lists[i].get('Printer') == status[i].get('Printer') and 
                    lists[i].get('Status') == status[i].get('Status') and 
                    lists[i].get('Paper') == status[i].get('Paper')):    
                    info.append("Printer: " + status[i].get('Printer') +
                                    "\n Status: " + status[i].get('Status') +
                                    "\n Error: " + status[i].get('Error') +
                                    "\n Paper: " + str(status[i].get('Paper')))
                    trigger = 1
                i += 1
            lists = status
"""
