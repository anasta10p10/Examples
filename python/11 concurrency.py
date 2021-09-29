# task 1
# ........................................................
# Дано:
# 
# import random
# import time
# from collections import defaultdict
# from threading import Thread


# class Player(Thread):
#     targets = (0, 10, 20, 50, 100)

#     def __init__(self, name, bullets, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.name = name
#         self.result = defaultdict(int)
#         self.bullets = bullets

#     def run(self):
#         for bullet in range(1, self.bullets + 1):
#             print(
#                 f"{self.name} is shooting with the bullet #{bullet}. Waiting for the fire\n",
#                 flush=True
#             )
#             # _ = 10000 ** random.randint(100, 10000)
#             time.sleep(0.01)
#             shot = random.choice(Player.targets)
#             # try:
#             #     print(f"the system equals {1/random.randint(0,4)}\n", flush=True)
#             # except Exception as e:
#             #     print(f"The exception is detected: {e.args}")
#             if shot == 0:
#                 print(f"{self.name} got nothing\n", flush=True)
#                 self.result[shot] += 1
#             else:
#                 print(f"{self.name} got {shot}\n", flush=True)
#                 self.result[shot] += 1

# def threads_work(players):
#     for player in players:
#         player.start()
#     for player in players:
#         player.join()

# player_names = [
#     "Tom",
#     "Jack",
#     "Anna",
#     "Helen",
#     "Tom",
#     "Jack",
#     "Anna",
#     "Helen",
#     "Tom",
#     "Jack",
#     "Anna",
#     "Helen",
#     "Tom",
#     "Jack",
#     "Anna",
#     "Helen",
# ]
# players = [Player(name, 100) for name in player_names]
# threads_work(players)

# ///////////////////////////////////////
# Подсчитать суммарный результат игры, выглядящий как словарь, в котором в качестве ключей будут выступать значения из targets, 
# а в качестве значений - количество попаданий. Получить результаты двумя способами:
# Через глобальный словарь (используя блокировки)

# import random
# import time
# from collections import defaultdict
# from threading import Thread
# import threading

# lock = threading.Lock()

# class Player(Thread):
#     targets = (0, 10, 20, 50, 100)

#     def __init__(self, name, bullets, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.name = name
#         self.result = defaultdict(int)
#         self.bullets = bullets

#     def run(self):
#         for bullet in range(1, self.bullets + 1):
#             # print(
#             #     f"{self.name} is shooting with the bullet #{bullet}. Waiting for the fire\n",
#             #     flush=True
#             # )
#             # _ = 10000 ** random.randint(100, 10000)
#             time.sleep(0.01)
#             shot = random.choice(Player.targets)
#             # try:
#             #     print(f"the system equals {1/random.randint(0,4)}\n", flush=True)
#             # except Exception as e:
#             #     print(f"The exception is detected: {e.args}")
#             if shot == 0:
#                 # print(f"{self.name} got nothing\n", flush=True)
#                 self.result[shot] += 1
#                 lock.acquire()
#                 slov[shot]+=1
#                 lock.release()
#             else:
#                 # print(f"{self.name} got {shot}\n", flush=True)
#                 self.result[shot] += 1
#                 lock.acquire()
#                 slov[shot]+=1
#                 lock.release()

# def threads_work(players):
#     for player in players:
#         player.start()
#     for player in players:
#         player.join()

# n=time.time()
# player_names = [
#     "Tom",
#     "Jack",
#     "Anna",
#     "Helen",
#     "Tom",
#     "Jack",
#     "Anna",
#     "Helen",
#     "Tom",
#     "Jack",
#     "Anna",
#     "Helen",
#     "Tom",
#     "Jack",
#     "Anna",
#     "Helen",
# ]
# slov=defaultdict(int)
# players = [Player(name, 1000) for name in player_names]
# threads_work(players)
# print(slov)
# t=time.time()
# print(t-n)

# # //////////////////////////
# # Через суммирование локальных self.result в конце

# import random
# import time
# from collections import defaultdict
# from threading import Thread


# class Player(Thread):
#     targets = (0, 10, 20, 50, 100)

#     def __init__(self, name, bullets, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.name = name
#         self.result = defaultdict(int)
#         self.bullets = bullets

#     def run(self):
#         for bullet in range(1, self.bullets + 1):
#             # print(
#             #     f"{self.name} is shooting with the bullet #{bullet}. Waiting for the fire\n",
#             #     flush=True
#             # )
#             # _ = 10000 ** random.randint(100, 10000)
#             time.sleep(0.01)
#             shot = random.choice(Player.targets)
#             # try:
#             #     print(f"the system equals {1/random.randint(0,4)}\n", flush=True)
#             # except Exception as e:
#             #     print(f"The exception is detected: {e.args}")
#             if shot == 0:
#                 # print(f"{self.name} got nothing\n", flush=True)
#                 self.result[shot] += 1
#             else:
#                 # print(f"{self.name} got {shot}\n", flush=True)
#                 self.result[shot] += 1

# def threads_work(players):
#     for player in players:
#         player.start()
#     for player in players:
#         player.join()

# n=time.time()

# player_names = [
#     "Tom",
#     "Jack",
#     "Anna",
#     "Helen",
#     "Tom",
#     "Jack",
#     "Anna",
#     "Helen",
#     "Tom",
#     "Jack",
#     "Anna",
#     "Helen",
#     "Tom",
#     "Jack",
#     "Anna",
#     "Helen",
# ]
# players = [Player(name, 1000) for name in player_names]
# threads_work(players)
# slov=defaultdict(int)
# for player in players:
#     for key in player.result.keys():
#         slov[key]+=player.result[key]
# print(slov)
# t=time.time()
# print(t-n)



# task 2
# Определить время выполнения и сравнить его с однопоточной версией
# Вывести 3 оптимальных по времени NUM_CUNSOMERS и NUM_PRODUCERS для скачивания 5000 картинок и для каждого из них вывести 
# время работы
# 
import queue
import threading
import random
import requests
import time


def save_image(id, url):
    with open(f"data\\pic{id}.jpg", "wb") as image:
        response = requests.get(url)
        image.write(response.content)


def consumer(q):
    while True:
        try:
            id = q.get(timeout = 0.1)
            result = requests.get(f"https://jsonplaceholder.typicode.com/photos/{id}")
            url = result.json()["thumbnailUrl"]
            save_image(id, url)
            # print(f"Save image {id}")
        except queue.Empty:
            if not any(producer.is_alive() for producer in producers):
                break


def producer(q, arr):
    for i in range(len(arr)):
        id = random.choice(arr)
        arr.remove(id)
        q.put(id)
slov=[]
x=1

for c in range(4,11):
    for p in range(1,5):
        NUM_CUNSOMERS = c
        NUM_PRODUCERS = p
        q = queue.Queue()
        consumers = []
        producers = []
        # arr_1 = [item for item in range(1, 101)]
        # arr_2 = [item for item in range(101, 201)]
        # arr = [arr_1, arr_2]
        n=200

        arr=[[i for i in range(1,int(n/NUM_PRODUCERS)+1)] for j in range(NUM_PRODUCERS)]


        n_p=time.time()

        for i in range(NUM_CUNSOMERS):
            worker = threading.Thread(target=consumer, args=(q,))
            worker.start()
            consumers.append(worker)

        for i in range(NUM_PRODUCERS):
            worker = threading.Thread(target=producer, args=(q,arr[i]))
            worker.start()
            producers.append(worker)


        for w in consumers:
            w.join()

        for w in producers:
            w.join()

        k_p=time.time()
        p_t=k_p - n_p

        slov.append({'N_C':NUM_CUNSOMERS,'N_P':NUM_PRODUCERS,'time':p_t})
        x+=1
        
# //////////////////////////

# n_o = time.time()

# for i in range(1,201):
#     q.put(i)

# consumer(q)

# k_o = time.time()

# o_t = k_o - n_o

# print(o_t)


slov.sort(key=lambda dict_ : dict_['time'])

for i in range(len(slov)):
    print(slov[i])

