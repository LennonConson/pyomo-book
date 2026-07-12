import pyomo.environ as pyo
def IC_model_dict(ICD):
    # ICD is a dictionary with the data for the problem

    model = pyo.ConcreteModel(name = "(H)")

    model.A = pyo.Set(initialize=ICD["A"])
    model.h = pyo.Param(model.A, initialize=ICD["h"])
    model.d = pyo.Param(model.A, initialize=ICD["d"])
    model.c = pyo.Param(model.A, initialize=ICD["c"])
    model.b = pyo.Param(initialize=ICD["b"])
    model.u = pyo.Param(model.A, initialize=ICD["u"])

    def xbounds_rule(model, i):
        return (0, model.u[i])
    model.x = pyo.Var(model.A, bounds=xbounds_rule)
    
    def obj_rule(model):\
            return sum(model.h[i] * \
                (model.x[i] - (model.x[i]/model.d[i])**2) \
                for i in model.A)
            
    model.z = pyo.Objective(rule=obj_rule,sense=pyo.maximize)

    def budget_rule(model):
        return sum(model.c[i]*model.x[i]\
                for i in model.A) <= model.b
    model.budgetconstr = pyo.Constraint(rule=budget_rule)
    return model
