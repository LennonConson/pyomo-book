import pyomo.environ as pyo

model = pyo.ConcreteModel()

N = ['Harlingen', 'Memphis', 'Ashland']
M = ['NYC', 'LA', 'Chicago', 'Houston']

P = 2

d = {('Harlingen', 'NYC'): 1956, \
    ('Harlingen', 'LA'): 1606, \
    ('Harlingen', 'Chicago'): 1410, \
    ('Harlingen', 'Houston'): 330, \
    ('Memphis', 'NYC'): 1096, \
    ('Memphis', 'LA'): 1792, \
    ('Memphis', 'Chicago'): 531, \
    ('Memphis', 'Houston'): 567, \
    ('Ashland', 'NYC'): 485, \
    ('Ashland', 'LA'): 2322, \
    ('Ashland', 'Chicago'): 324, \
    ('Ashland', 'Houston'): 1236 }

model.x = pyo.Var(N, M, bounds=(0,1))
model.y = pyo.Var(N, within=pyo.Binary)

model.num_warehouses = pyo.Constraint(expr=sum(model.y[n] for n \
       in N) <= P)

model.obj = pyo.Objective(expr=sum(d[n,m]*model.x[n,m] for n in \
        N for m in M))
