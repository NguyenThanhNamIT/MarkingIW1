grammar IELTSWriting;

essay: sentence+ EOF; 
sentence: trend | comparison | data | overview | other;

trend: (NOUN | ADJ NOUN) VERB (ADVERB | PREP | NUMBER | UNIT | WORD)* PUNCT; 
comparison: (NOUN | ADJ NOUN) COMPARE (NOUN | ADJ NOUN) (PREP | NUMBER | UNIT | WORD)* PUNCT; 
data: (NOUN | ADJ NOUN) (PREP | WORD)* NUMBER UNIT (ADVERB | PREP | NUMBER | COMPARE | WORD)* PUNCT; 
overview: 'Overall' (NOUN | ADJ | VERB | ADVERB | PREP | NUMBER | COMPARE | UNIT | WORD)* PUNCT; 
other: (NOUN | ADJ | VERB | ADVERB | PREP | NUMBER | COMPARE | UNIT | WORD)+ PUNCT;

NOUN: 'sales' | 'price' | 'United States' | 'China' | 'Japan' | 'figures' | 'countries' | 'market' | 'presence' | 'performance' | 'total'; 
ADJ: 'Chinese' | 'Japanese' | 'American' | 'highest' | 'lowest' | 'substantial' | 'respectable' | 'weaker' | 'strong' | 'clear'; 
VERB: 'increased' | 'decreased' | 'rose' | 'fell' | 'remained' | 'reached' | 'achieved' | 'recorded' | 'presents' | 'stood' | 'emphasizes' | 'reflects' | 'surpassed' | 'exceeded'; 
ADVERB: 'sharply' | 'gradually' | 'steadily' | 'slightly' | 'significantly' | 'markedly' | 'notably' | 'considerably' | 'only' | 'substantially'; 
COMPARE: 'higher than' | 'lower than' | 'equal to' | 'similar to'; 
PREP: 'in' | 'with' | 'for' | 'by' | 'at' | 'than' | 'among' | 'to' | 'of'; 
NUMBER: [0-9]+; UNIT: 'units' | 'percent' | 'dollars'; 
PUNCT: '.' | ',' | '#'; 
WORD: [a-zA-Z]+; 
WS: [ \t\r\n]+ -> skip; // Skip all whitespace