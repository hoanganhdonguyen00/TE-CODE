import random
class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed < 0:
            self.current_speed = 0
    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours
if __name__ == "__main__":
    cars = []
    for i in range(1, 11):
        reg_num = f"ABC-{i}"
        max_spd = random.randint(150, 200)
        cars.append(Car(reg_num, max_spd))
    race_over = False
    while not race_over:
        for c in cars:
            speed_change = random.randint(-10, 15)
            c.accelerate(speed_change)
            c.drive(1.0)
            if c.travelled_distance >= 10000:
                race_over = True
    print(f"{'Registration':<15} | {'Max Speed (km/h)':<20} | {'Current Speed (km/h)':<22} | {'Distance (km)':<20}")
    print("-" * 85)
    for c in cars:
        print(f"{c.registration_number:<15} | {c.max_speed:<20} | {c.current_speed:<22} | {c.travelled_distance:<20.1f}")