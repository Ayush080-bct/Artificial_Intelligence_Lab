% Facts
dog(tommy).
forall_dog_is_animal(X) :- dog(X), animal(X).
forall_animal_will_die(X) :- animal(X), will_die(X).

% Rules
animal(X) :- dog(X).
will_die(X) :- animal(X).

% Query
?- will_die(tommy).
