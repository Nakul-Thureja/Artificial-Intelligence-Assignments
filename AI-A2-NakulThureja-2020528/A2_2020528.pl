/* Nakul Thureja */
/* ROLL NO :- 2020528 */
/* BRANCH  :- CSE */
/* AI Assignment 2 */

/* To run consult the file and run the command start. */

start :- 
    nl,write("Road Distance System:- "),nl,
    read_data("capitalroaddistance.csv"),
    read_heuristic("heuristics.csv"),
    write("Enter the source city: "),nl,
    read(Source),
    nl,write("Enter the destination city: "),nl,
    read(Destination),
    find_path(Source,Destination),!.

find_path(Source,Destination):-
    nl,write("Which algorithm do you want to use: "),nl,
    print_list(["Depth First Search","Best First Search"],1),read(Choice),
    (Choice=1->dfs([[Source]],Destination,Path),reverse(Path,Path1,[]),nl,write("The Path found by Depth First Search Algorithm: "),nl,print_list(Path1,1),nl,nl,write("The Cost of Path: "),cost(Path1,Cost),write(Cost),nl;
    Choice=2->bestfs([[Source]],Destination,Path),reverse(Path,Path1,[]),nl,write("The Path found by Best First Search Algorithm: "),nl,print_list(Path1,1),nl,nl,write("The Cost of Path: "),cost(Path1,Cost),write(Cost),nl;
    nl,write("Wrong Choice"),nl).


reverse([],Z,Z).
reverse([H|T],Z,Acc) :- reverse(T,Z,[H|Acc]).

cost([_|[]],0).
cost([H1|[H2|T]],X):- distance(H1,H2,Y),cost([H2|T],Z), X is Y + Z.

set_maker([], []).
set_maker([Head | Tail], Result) :- member(Head, Tail), !,
set_maker(Tail, Result).
set_maker([Head | Tail], [Head | Result]) :- set_maker(Tail,Result).

print_list([],_).
print_list([H|T],C):-format("~d. ~s~n",[C,H]),C1 is C+1,print_list(T,C1).                                                                         
    
read_data(File) :-
    csv_read_file(File,Rows,[functor(cities), arity(21)]),
    maplist(assert,Rows),
    setof([City,D1,D2,D3,D4,D5,D6,D7,D8,D9,D10,D11,D12,D13,D14,D15,D16,D17,D18,D19,D20],
    cities(City,D1,D2,D3,D4,D5,D6,D7,D8,D9,D10,D11,D12,D13,D14,D15,D16,D17,D18,D19,D20),List),nl,
    get_header_dfs(List).

read_heuristic(File) :-
    csv_read_file(File,Rows1,[functor(heuristic), arity(3)]),
    maplist(assert,Rows1).

get_head([Head|_],Head).
get_tail([_|Tail],Tail).

get_header_dfs(List):-
    get_head(List,Head),
    get_tail(List,DistList),
    get_tail(Head,CityList),
    make_list_for_facts(CityList,DistList).

make_list_for_facts(_,[]).
make_list_for_facts(CityList,[Head|Tail]):-
    make_facts(CityList,Head),
    make_list_for_facts(CityList,Tail).

make_facts([],_).
make_facts([City1Name|CityList],[City2Name|[Dist|DistList]]):-
    assert(distance(City1Name,City2Name,Dist)),
    assert(distance(City2Name,City1Name,Dist)),
    make_facts(CityList,[City2Name|DistList]).

dfs([[D|P]|_],D,[D|P]).
dfs([Head|Tail],D,Path) :-
    add(Head,PossiblePaths),
    append(PossiblePaths,Tail,AllPaths),
    dfs(AllPaths,D,Path).

add([Head|Tail],PossiblePaths) :-
    findall([Next,Head|Tail],(distance(Head,Next,_),not(member(Next,[Head|Tail]))), PossiblePaths1),
    set_maker(PossiblePaths1,PossiblePaths).

bestfs([[D|P]|_],D,[D|P]).
bestfs([Head|Tail],D,Path) :-
    add(Head,PossiblePaths),
    append(PossiblePaths,Tail,AllPaths),
    bubble_sort(AllPaths,SortedPaths,D),
    bestfs(SortedPaths,D,Path).

bubble_sort(List,Sorted,Goal):-b_sort(List,[],Sorted,Goal).
b_sort([],Acc,Acc,_).
b_sort([H|T],Acc,Sorted,Goal):-bubble(H,T,NT,Max,Goal),b_sort(NT,[Max|Acc],Sorted,Goal).

bubble([H2|T2],[],[],[H2|T2],_).
bubble([H2|T2],[[H1|T1]|T],[[H1|T1]|NT],Ma,Goal):- heuristic(H2,Goal,A),heuristic(H1,Goal,Z),A>Z,bubble([H2|T2],T,NT,Ma,Goal).
bubble([H2|T2],[[H1|T1]|T],[[H2|T2]|NT],Ma,Goal):- heuristic(H2,Goal,A),heuristic(H1,Goal,Z),A=<Z,bubble([H1|T1],T,NT,Ma,Goal).