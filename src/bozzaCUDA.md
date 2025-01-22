L'idea è quella di far si che tutti i thread contemporaneamente controllino lo stesso 
pattern partendo da un punto diverso della sequenza 


Esempio : 

Sequenza [0 1 2 3 4 5 6 7 8 9 10]      indicati gli indici e non i caratteri 
Pattern da trovare : pattern[i] di lunghezza pat_length[i]

i thread si dividono i possibili indici della sequenza lunga 11 
Ad esempio, ci sono 3 thread, supponiamo che pat_length[i] = 4

il thread 0 controlla partendo dall'indice 0 i successivi 3 caratteri, 
controllando la sotto sequenza [0 1 2 3]

il thread 1 controlla partendo dall'indice 1 i successivi 3 caratteri, 
controllando la sotto sequenza [1 2 3 4]

il thread 2 controlla partendo dall'indice 2 i successivi 3 caratteri, 
controllando la sotto sequenza [2 3 4 5]

il thread 0 controlla partendo dall'indice 3 i successivi 3 caratteri, 
controllando la sotto sequenza [3 4 5 6]

$\vdots$

il thread 1 controlla partendo dall'indice 7 i successivi 3 caratteri, 
controllando la sotto sequenza [7 8 9 10]

(l'assegnamento in questo caso è round robin, può avvenire anche sequenzialmente, ad esempio il thread
0 deve controllare le sotto sequenze [0 1 2 3],[1 2 3 4]...ecc)

ATTENZIONE : SOLAMENTE IL PRIMO THREAD CHE TROVA IL PATTERN DOVRà INCREMENTARE pat_matches


In generale il thread i partendo dall'indice i controlla la sotto sequenza [i,i+pat_length], e la prossima sequenza 
da controllare per lui sarà [i+pat_length,i+2pat_length]


Quando un thread trova il pattern controlla legge pat_found, se questo ha un valore diverso da -1, lo sostituisce 
con l'indice in cui ha trovato il pattern se e solo se è minore dell'indice già presente su pat_found. La sostituzione 
deve avvenire in maniera atomica. La lettura di pat_found può avvenire parallelamente, difficilmente si creerà race condition,
questo avverrà se e solo se 
    - due thread hanno entrambi trovato un pattern 
    - per entrambi i thread, l'indice in cui lo hanno trovato è minore all'indice presente su pat_found (oppure quest'ultimo è -1)


Quando un thread trova un pattern, può smettere di cercare dato che controllerà solamente sotto sequenze
successive a quella che in cui lo ha trovato. Se le sequenze sono assegnate in modo sequenziale ed il thread 0
trova un pattern, allora è sicuramente la prima occorrenza di questo, tutti i thread possono smettere di cercare.

Se i thread controllano le sotto-sequenze in maniera sequenziale, allora succederà che due thread debbano 
accedere contemporaneamente a seq_matches solo se trovano un pattern che si trova nell'HALO

esempio :
SEQUENZA 
[0 1 2 3 4]         il pattern è lungo 2

thread 1 controlla 
[0 1 - - - ]
[- 1 2 - - ]


il thread 2 controlla 
[- - 2 3 - ]
[- - - 3 4 ]

L'unica parte della sequenza che controllano entrambi i thread è quella di indice 2, questi dovranno 
accedere sequenzialmente a seq matches se e solo se 

thread 1 trova un pattern su [- 1 2 - - ]
thread 2 trova un pattern su [- - 2 3 - ]

ATTENZIONE : In questo caso quando il thread 2 controlla [- - 2 3 - ], il thread 1 starà controllando 
[0 1 - - - ], quindi NON è possibile che accedano entrambi a seq_matches in scrittura 
