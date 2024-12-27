import random
from copy import copy

import numpy as np
from dataclasses import dataclass
from tqdm import tqdm

def make_2d_arr(shape: tuple):
    res = []
    for i in range(shape[0]):
        line = []
        for j in range(shape[1]):
            line.append(None)
        res.append(line)
    return res

def decart(l1, l2):
    res = []
    for el1 in l1:
        for el2 in l2:
            res.append((el1, el2))
    return res


class Plane:
    def __init__(self, max_row: int = 20, max_seat: int = 6):
        self.max_row: int = 20
        self.max_seat: int = 6
        self.seats: list[list[Passenger | None]] = make_2d_arr((max_row, max_seat))




class Passenger:
    def __init__(self, row, seat):
        self.row = row
        self.seat = seat
        self.state = 'in-airport'


def sample_passengers(plane: Plane,  capacity_ratio: float = 1.0):
    N = int(plane.max_row * plane.max_seat * capacity_ratio)
    available_places =  decart(range(plane.max_row), range(plane.max_seat))
    chosen_places = random.choices(available_places, k=N)
    result = []
    for row, seat in chosen_places:
        person = Passenger(row, seat)
        result.append(person)
    random.shuffle(result)
    return result


def mov(q1: list, index1: int, q2: list, index2: int):
    assert q2[index2] is None
    pas = copy(q1[index1])
    q1[index1] = None
    q2[index2] = pas

def visualize(in_airport, in_plane):
    result : str = ""
    for el in in_airport:
        if el is not None:
            result += "#"
        else:
            result += "_"
    result += '|||'
    for el in in_plane:
        if el is not None:
            result += "#"
        else:
            result += "_"
    return result


def simulate():
    plane = Plane()
    passengers = sample_passengers(plane)
    in_airport_queue = passengers
    in_plane_queue: list[Passenger | None] = [None for _ in range(plane.max_row)]


    tick = 0
    # [0, 1, ..... n] ____ [0, 1 ... n]
    for step in tqdm(range(100)):
        print(visualize(in_airport_queue, in_plane_queue))
        for i, pas in enumerate(in_airport_queue):
            if pas is None:
                continue
            if i == len(in_airport_queue) - 1 and in_plane_queue[0] is None:
                mov(in_airport_queue, i, in_plane_queue, 0)
                pas.state = 'in-plane'
                continue
            if in_airport_queue[i + 1] is None:
                mov(in_airport_queue, i, in_airport_queue, i+1)
                continue


        for i, pas in enumerate(in_plane_queue):
            if pas is None:
                continue
            if pas.row == i:
                m =  plane.max_seat // 2
                if pas.seat > m:
                    side = 'right'
                else:
                    side = 'left'
                if side == 'left':
                    places_to_check = plane.seats[pas.row][pas.seat:m + 1]
                else:
                    places_to_check = plane.seats[pas.row][m: pas.seat]
                pas.state = 'seat' # TOOD
                in_plane_queue[i] = None
                continue
            if in_plane_queue[i+1] is None:
                mov(in_plane_queue, i, in_plane_queue, i+1)
                continue

if __name__ == "__main__":
    simulate()










