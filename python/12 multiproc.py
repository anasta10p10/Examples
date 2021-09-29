# In order to get comfortable with ProcessPoolExecutors, I suggest you try to
# write a program that creates black and white versions of a large number
# of different photos. For this task, I recommend you download Pillow,
# which is a fork of the Python Imaging Library.
# Image processing is computationally expensive, as each pixel within the
# image has to be processed and recalculated when converting to black
# and white.
# The main requirements are as follows:
# The process must utilize the ProcessPoolExecutor class
# - The project should be able to process multiple images in parallel,
# - but ensure it does not process the same image on two different
# processes
# .......................................
# from PIL import Image
# # from concurrent.futures import ProcessPoolExecutor
# # import os
# import time

# def convert(name):
#     try:
#         image_file = Image.open(f"c_img/{name}") # open colour image
#         image_file = image_file.convert('1') # convert image to black and white
#         image_file.save(f'b_img/result_{name}')
#     except:
#         print("er")
    

# # def convert_thread():

# #      with ProcessPoolExecutor(max_workers=4) as executor:
# #         for i in os.listdir("c_img"):
# #             executor.submit(convert, i)

# # if __name__=="__main__":
# #     t=time.time()
# #     convert_thread()
# #     print(time.time()-t)

# import os
# t=time.time()
# for i in os.listdir("c_img"):
#     convert(i)
# print(time.time()-t)


# ////////////////////////////////////////////////////////////////////////////////////////
# Реализовать многопоточный, однопоточный, многопроцесный варианты. Сравнить результаты. (для "pic_multiproc")

# from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
# import random
# import time
# n=10
# def rasch(mas):
#     result=1/(1+(mas[0]-mas[1])**200)
#     for _ in range(100000):
#         __ = str(int(str(random.randint(1,10000000))))
#     return result

# def prosto():
#     res=[['-' for a in range(0,n)] for a in range(0,n)]
#     for i in range(1,n+1):
#         for j in range(1,n+1):
#             res[i-1][j-1]=rasch([i,j])
#     # print(res)
#     return res

# def proc():
#     res=[['-' for a in range(0,n)] for a in range(0,n)]
#     with ProcessPoolExecutor(max_workers=4) as executor:
#         for i in range(1,n+1):
#             for j in range(1,n+1):
#                 r=executor.submit(rasch, [i,j]) 
#                 res[i-1][j-1]=r
#     res = [[res[i][j].result() for j in range(n)] for i in range(n)]
#     # print(res)
#     return res   

# def thread():
#     res=[['-' for a in range(0,n)] for a in range(0,n)]
#     with ThreadPoolExecutor(max_workers=4) as executor:
#         for i in range(1,n+1):
#             for j in range(1,n+1):
#                 r=executor.submit(rasch, [i,j])
#                 res[i-1][j-1]=r
#     res = [[res[i][j].result() for j in range(n)] for i in range(n)]
#     # print(res)
#     return res

# if __name__=="__main__":
#     t=time.time()
#     prosto()
#     print(time.time()-t)

#     t=time.time()
#     proc()
#     print(time.time()-t)

#     t=time.time()
#     thread()
#     print(time.time()-t)
