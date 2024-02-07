#1
class Temperature:
    def __init__(self, value):
        self.value = value

class Celsius(Temperature):
    def to_kelvin(self):
        return Kelvin(self.value + 273.15)

    def to_fahrenheit(self):
        return Fahrenheit((self.value * 9/5) + 32)


class Kelvin(Temperature):
    def to_celsius(self):
        return Celsius(self.value - 273.15)

    def to_fahrenheit(self):
        return Fahrenheit((self.value - 273.15) * 9/5 + 32)


class Fahrenheit(Temperature):
    def to_celsius(self):
        return Celsius((self.value - 32) * 5/9)

    def to_kelvin(self):
        return Kelvin((self.value - 32) * 5/9 + 273.15)

#2
import random

class QuantumParticle:
    def __init__(self, x=None, p=None, spin=None):
        self.x = x if x is not None else self.position()
        self.p = p if p is not None else self.momentum()
        self.spin = spin if spin is not None else self.spin_measurement()

    def position(self):
        disturbance = self.disturbance()
        return random.randint(1, 10000) + disturbance

    def momentum(self):
        disturbance = self.disturbance()
        return random.uniform(0, 1) + disturbance

    def spin_measurement(self):
        return random.choice([0.5, -0.5])

    def disturbance(self):
        disturbance = random.uniform(-1, 1)
        self.x += disturbance
        self.p += disturbance
        print('Quantum Interferences!!')
        return disturbance

    def entangle(self, other_particle):
        if isinstance(other_particle, QuantumParticle):
            self.spin = 0.5
            other_particle.spin = -0.5
            print('Spooky Action at a Distance !!')
        else:
            raise ValueError('Entanglement is only possible between QuantumParticles.')

    def __repr__(self):
        return f'QuantumParticle(x={self.x}, p={self.p}, spin={self.spin})'


p1 = QuantumParticle(x=1, p=5.0)
p2 = QuantumParticle(x=2, p=5.0)
p1.entangle(p2)
print(repr(p1))
print(repr(p2))

p3 = QuantumParticle()
p4 = QuantumParticle()
p3.entangle(p4)
print(repr(p3))
print(repr(p4))
