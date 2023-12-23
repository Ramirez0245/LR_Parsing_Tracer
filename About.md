Given the following CFG and the LR Parsing table. A program to trace the input strings 
(1) (i+i)*i$       (2) (i*)$.  

(1)	E-->E + T
(2)	E -->E – T
(3)	E --> T
(4)	T-->T * F
(5)	T--> T/F
(6)	T--> F
(7)	F-->( E )
(8)	F--> i	
FIRST( E ) ={    (  i       }
FIRST (T ) = {   (  i       }
FIRST( F ) = {   (   i      }	
FOLLOW( E ) = {   $  + - )        }
FOLLOW( T ) = {   $ +  - ) * /   }
FOLLOW( F ) = {   $ +  - ) * /   }