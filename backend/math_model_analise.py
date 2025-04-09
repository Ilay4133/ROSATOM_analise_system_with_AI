# -*- coding: utf-8 -*-
import pandas as pd
import repeat as rp
from torchgen.gen_functionalization_type import return_from_mutable_noop_redispatch

user = rp.User(token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjQwNzA5OTUxOTksImlhdCI6MTc0NDA4OTc0MSwidXNlcklkIjoxNjU1fQ.sVYPdjnP5rbEyfiAFY1N1yomSYUpKpvztOQWN60VMeA')
project = 78629
t_interval = rp.TimeInterval(start = 0, end = 1000)
app = rp.Application(user)
model = app.get_exploration_model(project, t_interval)
variables = pd.Series({'DN1000' : 1, 'DN600x17': 0.596, 'TANKPRESS':1e5, 'AREA_FITTING_23V1':0.13900896800234608,
                       'DN600x25': 0.58, 'HOLEAREADESIGN': 0.005281017250684443, 'DN300x13': 0.299,
                       'ROD_POSITION': 1, 'DIAMETER_FITTING_23V2': 0.27075712741610936,
                       'FILTER_RESIST_COEFF':39.15303122952462,'DIAMETER_FITTING_123':0.5459261228146222,
                       'SATURATED_PRESSURE': 90.945e3, 'DN800x9':0.802,'WATER_DENSITY':960,
                       'TANKTEMP':97}, dtype = float)

def getting_values_from_api(model) -> list:
    with model as md:
      md.run(variables)
      flow_rate_mass_flowrate = md.get_results('mass_flowrate')
      drop_filter_press = md.get_results('drop_press_filter')
    max_flow_rate_mass_flowrate: float = float(flow_rate_mass_flowrate.loc[1000])
    max_drop_filter_press: float = float(drop_filter_press.loc[1000])
    print(max_flow_rate_mass_flowrate)
    print("_____")
    print(max_drop_filter_press)
    return [max_drop_filter_press, max_flow_rate_mass_flowrate]
def start_api():
    data_list=getting_values_from_api(model)
    return data_list

