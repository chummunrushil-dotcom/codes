from __future__ import annotations
import typing
# import random
# import time
# import typing 
# random.seed(time.time())
# data: typing.List = [*range(100)]
# random.shuffle(data)
# random_value =random.randint(1,100)
# print(random_value)
# data.append(random_value)

# print(len(data))

# my_data = [*range(0,100)]
# all_data = my_data+ data
# test = 0
# for i in all_data:
#     test = test ^ i
# print(f"{test^0}")

import random
import matplotlib.pyplot as plt
def function_gen() -> typing.Generator:
    for i in range(100):
        def do_somethings(a:float,b:float,c:float)->str:
            d=a/b
            c=a/c
            e=b/c
            f=((d**2)*(c**2)*(e**2))**0.5
            g=((2*a*f-(f+2+2*c)/(e**2+c**2+d**2)))+d + ((2*a*f-(f-2+2*c)/(e**2+c**2+d**2)))-d /(((((2*a*f-(f-2+2*c)/(e**2+c**2+d**2)))-d )**2)**0.5) -2*((2*a*f-(f-2+2*c)/(e**2+c**2+d**2)))-d
            return float(g)
        yield do_somethings(random.uniform(2,10),random.uniform(2,10),random.uniform(2,10))



# stored = []
# for i in range(100):
#     data = [*function_gen()]
#     stored.append(data)
#     plt.plot(data, color='purple')
#     plt.savefig(f"codes/testing/cool_plot_{i}.jpg")
#     plt.clf()
import pandas as pd
# df =pd.DataFrame(stored)
# df.to_csv("codes/testing/data.csv")


df = pd.read_csv("codes/testing/data.csv")
print(df.head())
print(df.info())
print(df.describe(include='all'))
print(df.describe())