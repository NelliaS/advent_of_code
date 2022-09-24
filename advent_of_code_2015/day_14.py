class Reindeer:
    def __init__(self, name: str, speed: int, duration: int, rest_time: int):
        self.name = name
        self.speed = speed
        self.duration = duration
        self.rest_time = rest_time
        self.flying_time = 0
        self.remain_to_rest = 0
        self.distance = 0
        self.points = 0

    @property
    def can_fly_now(self):
        return self.flying_time != self.duration

    def __repr__(self):
        return f'{self.name} ({self.distance}km and {self.points} points)'

    def reset_state(self):
        for attribute in 'flying_time', 'remain_to_rest', 'distance', 'points':
            setattr(self, attribute, 0)

    def distance_flown_in_time(self, time: int):
        while time > 0:
            if self.can_fly_now:
                time -= 1
                self.flying_time += 1
                self.distance += self.speed
            else:
                time -= self.rest_time
                self.flying_time = 0

    def fly_one_second(self):
        if self.remain_to_rest == 0:
            self.distance += self.speed
            self.flying_time += 1
            if not self.can_fly_now:
                self.remain_to_rest = self.rest_time
                self.flying_time = 0
        else:
            self.remain_to_rest -= 1


class Calculator:
    def __init__(self):
        self.reindeers: list[Reindeer] = []

    def reset_reindeers(self):
        for reindeer in self.reindeers:
            reindeer.reset_state()

    def find_winner(self):
        max_score = 0
        for reindeer in self.reindeers:
            if reindeer.points > max_score:
                max_score = reindeer.points
        return max_score

    def process_input(self):
        with open('day_14.txt') as f:
            for line in f:
                words = line.rstrip().rstrip('.').split()
                name, speed, duration, rest = words[0], int(words[3]), int(words[6]), int(words[-2])
                self.reindeers.append(Reindeer(name, speed, duration, rest))

    def biggest_distance_in_time(self, time):
        biggest_distance = 0
        for reindeer in self.reindeers:
            reindeer.distance_flown_in_time(time)
            if biggest_distance < reindeer.distance:
                biggest_distance = reindeer.distance
        return biggest_distance

    def highest_score_in_time(self, time):
        for _ in range(time):
            for reindeer in self.reindeers:
                reindeer.fly_one_second()
            self.give_points_for_a_lead()
        return self.find_winner()

    def give_points_for_a_lead(self):
        distances = []
        for reindeer in self.reindeers:
            distances.append(reindeer.distance)
        distances.sort(reverse=True)
        for reindeer in self.reindeers:
            if reindeer.distance == distances[0]:
                reindeer.points += 1


# Results:

# part 1
calculator = Calculator()
calculator.process_input()
result1 = calculator.biggest_distance_in_time(2503)
print(f'Result of part 1: "{result1}"')

# part 2
calculator.reset_reindeers()
result2 = calculator.highest_score_in_time(2503)
print(f'Result of part 2: "{result2}"')
