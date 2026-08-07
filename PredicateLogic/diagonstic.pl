% Facts
battery_voltage(low).
starter(inactive).
engine_cranks(slow).

% Rules
car_wont_start :- battery_voltage(low), starter(inactive).
engine_cranks_but_not_start :- fuel_level(low), battery_voltage(normal).
battery_problem :- car_wont_start, engine_cranks(slow).
