import random


def draw_once(num):
    if num <= 0.5:
        return 1
    elif num <= 0.5517:
        return 2
    else:
        return 0


def draw(draw_time=10):
    res = []
    for i in range(draw_time):
        res.append(draw_once(random.random()))
    return res


def test(test_time=10000000, draw_time=10):
    occur_time = 0
    for i in range(test_time):
        res = draw(draw_time)
        if 2 in res:
            occur_time += 1
    return occur_time


def get_ratio(res):
    num_win = 0
    num_lose = 0
    for i in res:
        if i == 0:
            num_lose += 1
        elif i > 0:
            num_win += 1
    return num_win / (num_win + num_lose)


if __name__ == '__main__':
    # res_list = draw(10000000)
    # print(get_ratio(res_list))
    print(test(draw_time=30))
