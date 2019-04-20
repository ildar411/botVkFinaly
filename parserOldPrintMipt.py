from lxml import html
import requests

def get_el(id):
    page = html.parse('http://old.print.mipt.ru/panel/')
    r_id = page.getroot().get_element_by_id(id)
    return r_id

e = get_el('psa46')
error = "pst"
state = 'psa'
paper = 'pcp'
switcher = {4 : '1a',23 : '1b', 
    7 : '2a', 22 : "2b",
    3 : '3a', 21 : '3b',
    13 : '3c', 5 : '4',
    1 : '6a', 24 : '6b',
    2 : '7a',20 : "7b",
    6 : '8a', 19 : '8b',
    25 : '9.1', 18 : '9.2',
    8 : "9.3", 43 : '11.1',
    44 : '11.2', 47 : '11.3a',
    10 : '11.3b', 45 : '12a',
    46 : '12b', 16 : 'GK',
    17 : 'NK'}
stat = []
papr = []
err = []
info = []


def getIdErr(i):
    id = error + str(i)
    try  :
        inf = get_el(id)
    except KeyError:
        return None
    infor = inf.text_content()
    infor = str(infor)
    return infor

def getIdState(i):
    id = state + str(i)
    try  :
        inf = get_el(id)
    except KeyError:
        return None
    infor = inf.text_content()
    infor = str(infor)
    return infor

def getIdPaper(i):
    id = paper + str(i)
    try  :
        inf = get_el(id)
    except KeyError:
        return None
    infor = inf.text_content()
    infor = str(infor)
    return infor

def ParserPrint():
    info = []
    for i in range(1,48):
        stat = getIdState(i)
        if not stat:
            continue
        err = getIdErr(i)
        papr = getIdPaper(i)
        if int(papr) < 51:
            if stat == 'Готов':
                err = "ВСЕ НОРМ"
            a = dict(Printer = switcher.get(i), Status = stat, Error = err, Paper = papr)
            info.append(a)
            continue
        if stat == 'Готов':
            err = "ВСЕ НОРМ"
            """
            a = dict(Printer = switcher.get(i), Status = stat, Error = err, Paper = papr)
            info.append(a)
            """
        else :
            a = dict(Printer = switcher.get(i), Status = stat, Error = err, Paper = papr)
            info.append(a)
        
    return info
#info = ParserPrint()

#for inf in info:
    #print(inf)
