import multiprocessing

def main():
    args = ['农业', '悠倍儿', '炖香居', '实府', '尖之味', '小梅来野', '山冲水水', '奇迹星空', '爱夫堂', '旺东农牧', '荣盛园', '中国天津网', '休品易站', '昆仑冈', '娄东堂', '极简无痛一站式', '惺惺之恋']
    results = []
    for arg in args:
        results.append(arg)
    return results

if __name__ == '__main__':
    with multiprocessing.Pool(processes=2) as pool:
        result = pool.map(main, [])
    print(result)
