def f_to_c(f):
    ctemp = (f - 32) * 5/9
    return round(ctemp, 1)

def get_force(mass, acceleration):
    return mass * acceleration

def get_energy(mass):
    c = 3 * 10 ** 8
    return mass * c

def get_work(m, a, d):
    return get_force(m, a) * d


train_mass = 500
train_acceleration = 120
train_distance = 1000

train_work = get_work(train_mass, train_acceleration, train_distance)
ge = get_force(train_mass, train_acceleration)

bomb_mass = 1

bomb_energy = get_energy(bomb_mass)

print(f_to_c(0))
print(f"The GE train supplies {ge} Newtons of force.")
print(f"A 1 kg bomb supplies {bomb_energy} Joules.")
print(f"The GE train does {train_work} Joules of work over {train_distance} meters.")