grammar TenseQuiz;

answer: verb EOF;

verb: PAST | PRESENT | FUTURE;

PAST: 'went' | 'was' | 'were' | 'saw' | 'ate' | 'drank' | 'ran' | 'wrote' | 'spoke' | 'took' | 'gave' | 'made' | 'did' | 'had' | 'came' | 'left' | 'bought' | 'sold' | 'built' | 'broke' | 'caught' | 'chose' | 'drew' | 'drove' | 'fell' | 'felt' | 'found' | 'flew' | 'got' | 'grew' | 'heard' | 'held' | 'kept' | 'knew' | 'led' | 'lost' | 'met' | 'paid' | 'rode' | 'sang' | 'sat' | 'sent' | 'stood' | 'swam' | 'taught' | 'thought';
PRESENT: 'goes' | 'is' | 'are' | 'sees' | 'eats' | 'drinks' | 'runs' | 'writes' | 'speaks' | 'takes' | 'gives' | 'makes' | 'does' | 'has' | 'comes' | 'leaves' | 'buys' | 'sells' | 'builds' | 'breaks' | 'catches' | 'chooses' | 'draws' | 'drives' | 'falls' | 'feels' | 'finds' | 'flies' | 'gets' | 'grows' | 'hears' | 'holds' | 'keeps' | 'knows' | 'leads' | 'loses' | 'meets' | 'pays' | 'rides' | 'sings' | 'sits' | 'sends' | 'stands' | 'swims' | 'teaches' | 'thinks';
FUTURE: 'will go' | 'will be' | 'will see' | 'will eat' | 'will drink' | 'will run' | 'will write' | 'will speak' | 'will take' | 'will give' | 'will make' | 'will do' | 'will have' | 'will come' | 'will leave' | 'will buy' | 'will sell' | 'will build' | 'will break' | 'will catch' | 'will choose' | 'will draw' | 'will drive' | 'will fall' | 'will feel' | 'will find' | 'will fly' | 'will get' | 'will grow' | 'will hear' | 'will hold' | 'will keep' | 'will know' | 'will lead' | 'will lose' | 'will meet' | 'will pay' | 'will ride' | 'will sing' | 'will sit' | 'will send' | 'will stand' | 'will swim' | 'will teach' | 'will think' | 'will need';

WS: [ \t\r\n]+ -> skip;