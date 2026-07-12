import pyomo.environ as pyo

model = pyo.ConcreteModel()

model.x = pyo.Var()
model.y = pyo.Var(bounds=(-2,4))
model.z = pyo.Var(initialize=1.0, within=pyo.NonNegativeReals)

model.obj = pyo.Objective(expr=model.x**2 + model.y + model.z)

model.eq_con = pyo.Constraint(expr=model.x + model.y + model.z \
        == 1) 

model.ineq_con = pyo.Constraint(expr=model.x + model.y <= 0)

opt = pyo.SolverFactory('ipopt')
result = opt.solve(model)
pyo.assert_optimal_termination(result)

model.display()
