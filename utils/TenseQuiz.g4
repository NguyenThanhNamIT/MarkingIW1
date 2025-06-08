grammar TenseQuiz;

answer: correct_sentence | fill_in_the_blank;

fill_in_the_blank: verb;

correct_sentence: subject_verb_pair (direct_object)? (optional_content)? (expression)? (PUNCTUATION)?;

// Subject-verb agreement rules
subject_verb_pair: 
    third_person_singular third_person_verb |
    non_third_person non_third_person_verb |
    any_subject past_or_future_verb;

third_person_singular: ('he' | 'she' | 'it') | singular_noun_phrase;
non_third_person: ('i' | 'you' | 'we' | 'they') | plural_noun_phrase;
any_subject: third_person_singular | non_third_person;

singular_noun_phrase: (DETERMINER)? SINGULAR_NOUN;
plural_noun_phrase: (DETERMINER)? PLURAL_NOUN;

third_person_verb: THIRD_PERSON_PRESENT | 'is' | 'was';
non_third_person_verb: NON_THIRD_PERSON_PRESENT | 'am' | 'are' | 'were';
past_or_future_verb: PAST | FUTURE;

verb: THIRD_PERSON_PRESENT | NON_THIRD_PERSON_PRESENT | PAST | FUTURE | BE_PRESENT | BE_PAST;

direct_object: noun_phrase | singular_noun_phrase | plural_noun_phrase;

optional_content: prepositional_phrase | WORD;

prepositional_phrase: PREPOSITION (PRONOUN | noun_phrase | singular_noun_phrase | plural_noun_phrase)+;

expression: PAST_EXPRESSION | NOW_EXPRESSION | FUTURE_EXPRESSION;

noun_phrase: (DETERMINER)? WORD;

BE_PRESENT: 'is' | 'are' | 'am';
BE_PAST: 'was' | 'were';

PRONOUN: 'i' | 'me' | 'you' | 'he' | 'him' | 'she' | 'her' | 'it' | 'we' | 'us' | 'they' | 'them';
DETERMINER: 'the' | 'a' | 'an';
SINGULAR_NOUN: 'person' | 'man' | 'woman' | 'child' | 'student' | 'teacher' | 'dog' | 'cat' | 'book' | 'car' | 'house' | 'school' | 'park' | 'party' | 'dinner' | 'football' | 'weekend';
PLURAL_NOUN: 'people' | 'men' | 'women' | 'children' | 'students' | 'teachers' | 'dogs' | 'cats' | 'books' | 'cars' | 'houses' | 'schools' | 'parks' | 'parties' | 'weekends';
THIRD_PERSON_PRESENT: 'goes' | 'does' | 'has' | 'runs' | 'walks' | 'eats' | 'writes' | 'plays' | 'studies' | 'drives' | 'makes' | 'sees' | 'takes' | 'gives';
NON_THIRD_PERSON_PRESENT: 'go' | 'do' | 'have' | 'run' | 'walk' | 'eat' | 'write' | 'play' | 'study' | 'drive' | 'make' | 'see' | 'take' | 'give';
PAST: 'did' | 'went' | 'had' | 'ran' | 'walked' | 'ate' | 'wrote' | 'played' | 'studied' | 'drove' | 'made' | 'saw' | 'took' | 'gave';
FUTURE: 'will go' | 'will do' | 'will have' | 'will run' | 'will walk' | 'will eat' | 'will read' | 'will write' | 'will play' | 'will study' | 'will drive' | 'will make' | 'will see' | 'will take' | 'will give';
PAST_EXPRESSION: 'yesterday' | 'last week' | 'previously' | 'last night' | 'last year' | 'earlier' | 'in the past' | 'a moment ago' | 'before';
NOW_EXPRESSION: 'today' | 'daily' | 'now' | 'currently' | 'at the moment' | 'right now' | 'these days' | 'at present' | 'this moment';
FUTURE_EXPRESSION: 'tomorrow' | 'next week' | 'soon' | 'next day' | 'in the future' | 'later' | 'next year' | 'afterwards' | 'someday' | 'eventually';
PREPOSITION: 'to' | 'in' | 'at' | 'on' | 'with' | 'for' | 'by' | 'about' | 'over' | 'under' | 'between' | 'among' | 'through' | 'during' | 'without' | 'within' | 'against' | 'along' | 'across' | 'behind' | 'beside' | 'beyond' | 'from' | 'into' | 'near' | 'off' | 'onto' | 'outside' | 'past' | 'since' | 'toward' | 'upon' | 'via';

WORD: [a-zA-Z]+;

UNDERSCORE: '_'+ -> skip;
PARENTHESES: [()]+ -> skip;

PUNCTUATION: [.!?;,];
WS: [ \t\r\n]+ -> skip;