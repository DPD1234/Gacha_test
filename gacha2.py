import random


def draw_once(num, state):
    if num <= 0.5:
        return 1
    if state == 0:
        return 0
    elif state == 1:
        if num <= 0.75:
            return 2
        else:
            return 0
    else:
        return 2


def draw(draw_time=10):
    state = 0
    res = [-1]
    for i in range(draw_time):
        res.append(draw_once(random.random(), state))
        if len(res) >= 3:
            if res[-1] == 0 and res[-2] == 0:
                if res[-3] == 0:
                    state = 2
                else:
                    state = 1
            else:
                state = 0
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
    print(test(draw_time=50))


























