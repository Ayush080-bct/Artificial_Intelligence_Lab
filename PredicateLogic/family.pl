% Facts
parent(bob, charlie).
parent(charlie, david).

% Inference Rule (If X is a parent of Y, and Y is a parent of Z, then X is a grandparent of Z)
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
