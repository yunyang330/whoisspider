from multiprocessing import Pool

# 定义一个函数用来进行平方和立方运算
def square_and_cube(x):
    return x*2, x*3

# 定义一个需要进行运算的列表
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 创建进程池，设置进程数为4
with Pool(processes=4) as pool:
    # 使用map函数并行运行square_and_cube函数，并将返回的两个值存入两个列表
    results = pool.map(square_and_cube, numbers)
    squares = [r[0] for r in results]
    cubes = [r[1] for r in results]

print("平方结果列表：", squares)
print("立方结果列表：", cubes)
