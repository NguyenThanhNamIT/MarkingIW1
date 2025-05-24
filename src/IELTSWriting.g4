grammar IELTSWriting;

essay: sentence+ EOF;
sentence: trend | comparison | data | overview | other;
trend: NOUN VERB ADVERB? PUNCT;              // e.g., "Sales increased sharply."
comparison: NOUN COMPARE NOUN PUNCT;         // e.g., "USA was higher than China."
data: NOUN 'in' YEAR NUMBER UNIT? PUNCT;     // e.g., "Sales in 2020 were 100 units."
overview: 'Overall' WORD+ PUNCT;             // e.g., "Overall sales rose."
other: WORD+ PUNCT;

NOUN: 'sales' | 'price' | 'USA' | 'China' | 'Japan' | [a-zA-Z]+;
VERB: 'increased' | 'decreased' | 'rose' | 'fell' | 'remained';
ADVERB: 'sharply' | 'gradually' | 'steadily' | 'slightly';
COMPARE: 'higher than' | 'lower than' | 'equal to' | 'similar to';
YEAR: [0-9]{4};
NUMBER: [0-9]+;
UNIT: 'units' | 'percent' | 'dollars';
PUNCT: '.' | '!';
WORD: [a-zA-Z]+;
WS: [ \t\r\n]+ -> skip;
