# Пользователь вводит абсолютный путь к директории с большим количеством фотографий, лежащих в этой
# директории. Далее пользователь вводит параметр, по которому нужно группировать фотографии(год, 
# год+месяц, год+месяц+день). Разделить фотографии, по папкам по заданному параметру группировки. 
# Папки создаются динамически исходя из даты создания(редактирования) изображения(файла). 
# ..................................................................................
# import shutil

# from datetime import datetime

# import os
# link=input('Введите путь к файлу')
# norm_path = os.path.normpath(link)
# p=input('Как вы хотите группировать? год, год+месяц, год+месяц+день')
# os.chdir(link)
# full_list=os.listdir(norm_path)
# file_date={}
# months={'01':'Январь','02':'Февраль','03':'Март','04':'Апрель','05':'Май','06':'Июнь',
# '07':'Июль','08':'Август','09':'Сентябрь','10':'Октябрь','11':'Ноябрь','12':'Декабрь'}
# for file in full_list:
#     os.chdir(link)
#     time_sec = datetime.fromtimestamp(os.path.getmtime(file)).strftime('%Y-%m-%d')
#     # datetime.fromtimestamp(time_sec).strftime('%Y-%m-%d')[5:7])
#     if time_sec[0:4] in file_date:
#         pass
#     else:
#         os.mkdir(time_sec[0:4])
#         file_date[time_sec[0:4]]={}
#     path_y=os.path.join(link,time_sec[0:4])
#     shutil.copy(os.path.join(norm_path, file), path_y)
#     if p== 'год+месяц' or p=='год+месяц+день':
#         if months[time_sec[5:7]] in file_date[time_sec[0:4]]:
#             pass
#         else:
#             os.chdir(path_y)
#             os.mkdir(months[time_sec[5:7]])
#             file_date[time_sec[0:4]][months[time_sec[5:7]]]={}
#         path_m=os.path.join(path_y,months[time_sec[5:7]])
#         shutil.move(os.path.join(path_y, file), path_m)
#         if p=='год+месяц+день':
#             if time_sec[8:10] in file_date[time_sec[0:4]][months[time_sec[5:7]]]:
#                 pass
#             else:
#                 os.chdir(path_m)
#                 os.mkdir(time_sec[8:10])
#                 file_date[time_sec[0:4]][months[time_sec[5:7]]][time_sec[8:10]]={}
#             path_d=os.path.join(path_m,time_sec[8:10])
#             shutil.move(os.path.join(path_m, file), path_d)
# //////////////////////////////////////////////////////////////////
# Модифицировать блокировщик сайтов таким образом, чтобы он убирал блокировку в нерабочее время.(sites_blocking.py)
import time
from datetime import datetime as dt
windows = "C:\\Windows\\System32\\drivers\\etc\\hosts"
linux = "/etc/hosts"
nastya="host.txt"
hosts_path=nastya
redirect="127.0.0.1"
website_list=["www.facebook.com","facebook.com"]

while True:
    mas=[]
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,17):
        print("Working hours...")
        with open(hosts_path,'r+') as file:
            content=file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+ website+"\n")
                
    else:
        print('free')
        with open(hosts_path,'r',encoding='UTF-8') as file:
            for line in file:
                mas.append(line)
            for website in website_list:
                for i in range(len(mas)):
                    if mas[i]==redirect+" "+ website+"\n":
                        mas[i]=''
        with open(hosts_path,'w') as file:
            file.write("".join(mas))   
    time.sleep(5)