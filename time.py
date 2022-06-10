import time


def main():

    inf = open('C:/Users/pavel/Downloads/8_Bible_txt/Bible_txt1.txt')
    text = [i.strip(',.?-:!()*;`') for i in inf.read().lower().split()]
    result = {}
    for i in text:
        if i.isalpha():
            result[i] = result.get(i, 0) + 1
    # result = {elem: text.count(elem) for elem in set(text) if elem.isalpha()}
    print(sorted(result.items(), key=lambda item: item[1]))
    # print(result)



tic = time.perf_counter()
main()
toc = time.perf_counter()
print(f"Вычисление заняло {toc - tic} секунд")
