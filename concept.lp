% Generation of concepts.


obj(X):- rel(X,_) ; rel(X,Y): att(Y).
att(Y):- rel(_,Y) ; rel(X,Y): obj(X).

:- not obj(X): obj(X).
:- not att(Y): att(Y).


#show.
#show obj/1.
#show att/1.
