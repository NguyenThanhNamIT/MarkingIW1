grammar TenseQuiz;

answer: correct_sentence | fill_in_the_blank | EOF;

fill_in_the_blank: verb;

correct_sentence: subject_verb_pair (direct_object)? (optional_content)? (expression)? (PUNCTUATION)?;

subject_verb_pair: 
    third_person_singular third_person_verb |
    non_third_person non_third_person_verb |
    any_subject past_or_future_verb;

third_person_singular: 
    ('he' | 'He' | 'she' | 'She' | 'it' | 'It') | 
    singular_noun_phrase;

non_third_person: 
    ('i' | 'I' | 'you' | 'You' | 'we' | 'We' | 'they' | 'They') | 
    plural_noun_phrase;

any_subject: third_person_singular | non_third_person;

singular_noun_phrase: (DETERMINER)? (SINGULAR_NOUN | CAPITALIZED_SINGULAR_NOUN);
plural_noun_phrase: (DETERMINER)? (PLURAL_NOUN | CAPITALIZED_PLURAL_NOUN);

third_person_verb: THIRD_PERSON_PRESENT | 'is' | 'was';
non_third_person_verb: NON_THIRD_PERSON_PRESENT | 'am' | 'are' | 'were';
past_or_future_verb: PAST | FUTURE;

verb: THIRD_PERSON_PRESENT | NON_THIRD_PERSON_PRESENT | PAST | FUTURE | BE_PRESENT | BE_PAST;

direct_object: noun_phrase | singular_noun_phrase | plural_noun_phrase | PRONOUN;

optional_content: prepositional_phrase | WORD | CAPITALIZED_WORD;

prepositional_phrase: PREPOSITION (PRONOUN | noun_phrase | singular_noun_phrase | plural_noun_phrase | CAPITALIZED_WORD | WORD)+;

expression: PAST_EXPRESSION | NOW_EXPRESSION | FUTURE_EXPRESSION;

noun_phrase: (DETERMINER)? (WORD | CAPITALIZED_WORD);

BE_PRESENT: 'is' | 'Is' | 'are' | 'Are' | 'am' | 'Am';
BE_PAST: 'was' | 'Was' | 'were' | 'Were';

PRONOUN: 'i' | 'I' | 'me' | 'Me' | 'you' | 'YOU' | 'he' | 'He' | 'him' | 'Him' | 'she' | 'She' | 'her' | 'Her' | 'it' | 'It' | 'we' | 'We' | 'us' | 'Us' | 'they' | 'They' | 'them' | 'Them';
DETERMINER: 'the' | 'The' | 'THE' | 'a' | 'A' | 'an' | 'An' | 'AN';

// Lowercase nouns
SINGULAR_NOUN: 'person' | 'man' | 'woman' | 'child' | 'student' | 'teacher' | 'dog' | 'cat' | 'book' | 'car' | 'house' | 'school' | 'park' | 'party' | 'dinner' | 'football' | 'weekend' | 'sandwich' | 'letter';
PLURAL_NOUN: 'people' | 'men' | 'women' | 'children' | 'students' | 'teachers' | 'dogs' | 'cats' | 'books' | 'cars' | 'houses' | 'schools' | 'parks' | 'parties' | 'weekends' | 'sandwiches' | 'letters';

// Capitalized nouns
CAPITALIZED_SINGULAR_NOUN: 'Person' | 'Man' | 'Woman' | 'Child' | 'Student' | 'Teacher' | 'Dog' | 'Cat' | 'Book' | 'Car' | 'House' | 'School' | 'Park' | 'Party' | 'Dinner' | 'Football' | 'Weekend' | 'Sandwich' | 'Letter';
CAPITALIZED_PLURAL_NOUN: 'People' | 'Men' | 'Women' | 'Children' | 'Students' | 'Teachers' | 'Dogs' | 'Cats' | 'Books' | 'Cars' | 'Houses' | 'Schools' | 'Parks' | 'Parties' | 'Weekends' | 'Sandwiches' | 'Letters';
THIRD_PERSON_PRESENT: 'goes' | 'Goes' | 'does' | 'Does' | 'has' | 'Has' | 'runs' | 'Runs' | 'walks' | 'Walks' | 'eats' | 'Eats' | 'writes' | 'Writes' | 'plays' | 'Plays' | 'studies' | 'Studies' | 'drives' | 'Drives' | 'makes' | 'Makes' | 'sees' | 'Sees' | 'takes' | 'Takes' | 'gives' | 'Gives';
NON_THIRD_PERSON_PRESENT: 'go' | 'Go' | 'do' | 'Do' | 'have' | 'Have' | 'run' | 'Run' | 'walk' | 'Walk' | 'eat' | 'Eat' | 'write' | 'Write' | 'play' | 'Play' | 'study' | 'Study' | 'drive' | 'Drive' | 'make' | 'Make' | 'see' | 'See' | 'take' | 'Take' | 'give' | 'Give';
PAST: 'did' | 'Did' | 'went' | 'Went' | 'had' | 'Had' | 'ran' | 'Ran' | 'walked' | 'Walked' | 'ate' | 'Ate' | 'wrote' | 'Wrote' | 'played' | 'Played' | 'studied' | 'Studied' | 'drove' | 'Drove' | 'made' | 'Made' | 'saw' | 'Saw' | 'took' | 'Took' | 'gave' | 'Gave';
FUTURE: 'will go' | 'Will go' | 'will do' | 'Will do' | 'will have' | 'Will have' | 'will run' | 'Will run' | 'will walk' | 'Will walk' | 'will eat' | 'Will eat' | 'will read' | 'Will read' | 'will write' | 'Will write' | 'will play' | 'Will play' | 'will study' | 'Will study' | 'will drive' | 'Will drive' | 'will make' | 'Will make' | 'will see' | 'Will see' | 'will take' | 'Will take' | 'will give' | 'Will give';
PAST_EXPRESSION: 'yesterday' | 'Yesterday' | 'last week' | 'Last week' | 'previously' | 'Previously' | 'last night' | 'Last night' | 'last year' | 'Last year' | 'earlier' | 'Earlier' | 'in the past' | 'In the past' | 'a moment ago' | 'A moment ago' | 'before' | 'Before';
NOW_EXPRESSION: 'today' | 'Today' | 'daily' | 'Daily' | 'now' | 'Now' | 'currently' | 'Currently' | 'at the moment' | 'At the moment' | 'right now' | 'Right now' | 'these days' | 'These days' | 'at present' | 'At present' | 'this moment' | 'This moment';
FUTURE_EXPRESSION: 'tomorrow' | 'Tomorrow' | 'next week' | 'Next week' | 'soon' | 'Soon' | 'next day' | 'Next day' | 'in the future' | 'In the future' | 'later' | 'Later' | 'next year' | 'Next year' | 'afterwards' | 'Afterwards' | 'someday' | 'Someday' | 'eventually' | 'Eventually';
PREPOSITION: 'to' | 'To' | 'in' | 'In' | 'at' | 'At' | 'on' | 'On' | 'with' | 'With' | 'for' | 'For' | 'by' | 'By' | 'about' | 'About' | 'over' | 'Over' | 'under' | 'Under' | 'between' | 'Between' | 'among' | 'Among' | 'through' | 'Through' | 'during' | 'During' | 'without' | 'Without' | 'within' | 'Within' | 'against' | 'Against' | 'along' | 'Along' | 'across' | 'Across' | 'behind' | 'Behind' | 'beside' | 'Beside' | 'beyond' | 'Beyond' | 'from' | 'From' | 'into' | 'Into' | 'near' | 'Near' | 'off' | 'Off' | 'onto' | 'Onto' | 'outside' | 'Outside' | 'past' | 'Past' | 'since' | 'Since' | 'toward' | 'Toward' | 'upon' | 'Upon' | 'via' | 'Via';

// Generic word patterns for unrecognized words
CAPITALIZED_WORD: [A-Z][a-z]*;
WORD: [a-z]+;

UNDERSCORE: '_'+ -> skip;
PARENTHESES: [()]+ -> skip;

PUNCTUATION: [.!?;,];
WS: [ \t\r\n]+ -> skip;