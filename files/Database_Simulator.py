from problems import HealthcareProblem
from simulator import Simulator
from  import your

problem = HealthcareProblem()
simulator = Simulator(your_planner, problem)
result = simulator.rub(365*24)
