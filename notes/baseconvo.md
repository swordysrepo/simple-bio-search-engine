baseconvo.md

jax — Today at 6:55 PM
sha-1 is fine
for us
but not for crypto since its been shown to be crackable
so back to focus
one hashmap with unique words => lists
that should be the final structure
then comparing those lists will be a pain
swordy — Today at 6:57 PM
how long is it to search a single dictionary of 100k entries?
jax — Today at 6:57 PM
10 microsec
Bones — Today at 6:57 PM
/run py
import hashlib
print(hashlib.sha1(b'hello').hexdigest())
print(hashlib.sha256(b'hello').hexdigest())
print(hashlib.sha512(b'hello').hexdigest())
I Run Code
BOT
 — Today at 6:57 PM
Here is your output @Bones
aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d
2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca72323c3d99ba5c11d7c7acc6e14b8c5da0c4663475c2e5c3adef46f73bcdec043
jax — Today at 6:58 PM
cool
swordy — Today at 6:59 PM
it is then 
{"word" : "tomato" , "hash" : "2cf24dba5fb0a30e26
", "list" : [1,16,55,22,66,44,88,99 ...]},

{"word" : "pomato" , "hash" : "2cf24dba5fb0a30e26e83b3362938b9824
", "list" : [1,16,55,22,66,44,88,99 ...]},

{"word" : "romato" , "hash" : "2cf24dba5fb0a30e26043362938b9824
", "list" : [1,16,55,22,66,44,88,99 ...]}
jax — Today at 6:59 PM
yeap
so list comparisons
swordy — Today at 7:00 PM
why do we need the hash in the dictionary
jax — Today at 7:01 PM
not sure
maybe we dont
not sure how py dicts work
hash is prb internal
swordy — Today at 7:02 PM
at this point i see we can omit it
jax — Today at 7:02 PM
ok
swordy — Today at 7:02 PM
i wonder how a dictionary is "iterated"
to be so quick
jax — Today at 7:03 PM
lol
when u search for something
your search term is the key
to what your accesing
swordy — Today at 7:03 PM
it has to find the key
how does it find the key
jax — Today at 7:03 PM
nope
your search term is the key
i know it takes a while to accept it
but youll get used to it
swordy — Today at 7:04 PM
what is the dictionary algorithm, i am searching
jax — Today at 7:04 PM
i had a similar experience
youre not searching
lol
swordy — Today at 7:05 PM
google i am searching
jax — Today at 7:05 PM
youre just running a word into a function
that hash is prb linked to some memory address
swordy — Today at 7:05 PM
trying to find an algorithm .
so thats why we dont need to generate a hash, python automatically generates the hash , and it's stored in memory like you said
jax — Today at 7:06 PM
yeah
im good at guessing
lol
swordy — Today at 7:07 PM
makes good sense
jax — Today at 7:07 PM
so for list comparisons
im stuck
not sure what a fast way would be
we can prb join the lists
sort
then find dups
swordy — Today at 7:08 PM
potentially hundreds of thousands of lines for each word
and millions
jax — Today at 7:08 PM
yeah
sorting millions takes lots of time
seems like weve reached another dead end
swordy — Today at 7:09 PM
i wonder if the previous method resolves better
jax — Today at 7:09 PM
which one?
swordy — Today at 7:10 PM
the original that was too many dictionaries
jax — Today at 7:10 PM
well 2 terms in 100k words
math would be 100k^2
or no 100k permutations
still huge number
swordy — Today at 7:17 PM
limit the amount of returned results? Search X many lines in each of the matching hashes for a match , and return a result based on only those . Or randomly select which lines to check for matches . (would result in differing results)
but then you're rediscovering for every search
could save a history of any search generated so taht it can be accessed quicker the next time
jax — Today at 7:18 PM
eh okay idea
swordy — Today at 7:19 PM
which is probably microseconds of a difference .. but it would show a search engine algorithm , bringing the searched for results to the top
jax — Today at 7:19 PM
well weve reached a problem more complex
i was thinking of using neural nets
or something
but not sure how
there are also some ant algorithms
swordy — Today at 7:20 PM
i see it could go full circle somehow . maybe by omission . if its 10 words long and we know which 10 words it contains , then we know the 11th word isnt there
because we're working with a limited title
jax — Today at 7:21 PM
well its just numbers well compare
swordy — Today at 7:22 PM
can have a word count aswell . and then when the line is 11 words long and we match 11 words in the dictionary , we know all other words dont apply to that title
jax — Today at 7:23 PM
i see your ommision idea
but im not to thrilled about it
anyhow lets take a break
swordy — Today at 7:25 PM
checking every word of every title , while we match the first word. iterating through a limited number of lines. might allow us to search more lines with equal processing
jax — Today at 7:25 PM
and see what we come up with in a bit
brake time
also need some coffe
one idea is to brute force it with multitasking
i mean the problem is O(n^2)
so for every item in a list we have to compare it to every other item
5 list say a 300k each
1.5m^2
two trillion two hundred fifty billion
lol
so even with multitasking wed have to reduce number to 10000 titles
felix q 10000^2
Felix
BOT
 — Today at 7:39 PM
100000000
swordy — Today at 7:40 PM
we could also improve it to start with the "best" first word . Like a search algorithm would.  Searching titles that contain at least 1 word that is very popularly searched . and then search only 100k results that contain that word first... and then search those 100k results for the next most popular result . Then also set threshholds for how many maximum titles to search .. and another threshhold above that for how many results to return at a minimum. It will hit the maximum titles to search threshhold if it does not reach it's minimum search results
typed that a while ago
we can use an API that links to googles API
the API that says which words are popular
jax — Today at 7:41 PM
okay i see
so say we do a word frequency in all articles
filter those words to meaningful ones
swordy — Today at 7:41 PM
omit words like "and" , "if", "but" ?
jax — Today at 7:42 PM



and also



some hash function
swordy — Today at 6:30 PM
and then theres only one match to that hash
jax — Today at 6:30 PM
whether its sha-256 or any other ones
yes
swordy — Today at 6:31 PM
hash function is generation protocol
jax — Today at 6:31 PM
per word 1 hash
in super rare occasions there may be collisions
in reality never
but theoretically its possible
no need to worry about collisions
so 1 word per 1 hash
regardless of length of word
so 1 list 100k entries, querry max of 5 times..compare lists for dups
and youll have the line numbers to the titles you need
swordy — Today at 6:33 PM
100k unique hashes
jax — Today at 6:33 PM
yes
swordy — Today at 6:34 PM
100k lists?
matched with those hashes
jax — Today at 6:34 PM
nope 1 list
so each word will match 1 hash
when u query say word hello
u get a list of titles
u querry again world
swordy — Today at 6:35 PM
how do you get a list of titles?
jax — Today at 6:35 PM
u get another list of titles
all titles are in one file
we want their line numbers
swordy — Today at 6:36 PM
i see they aren't matched with hashes.
jax — Today at 6:37 PM
no
true
swordy — Today at 6:37 PM
every title would be queried to see whether it matches then
and then we have a slow system
jax — Today at 6:37 PM
well yes when u generate the hashmap it will be slow
since youll have to query each word individually
and generate that list
swordy — Today at 6:38 PM
oh, but the hashmap is a saved search
for that 1 word
jax — Today at 6:38 PM
so next to each hash youll have that list
so word hash list
swordy — Today at 6:38 PM
to me that means it would be a list matched with that hash
jax — Today at 6:38 PM
yes
swordy — Today at 6:39 PM
so we have 100k lists , 100k hashes
jax — Today at 6:39 PM
nope
swordy — Today at 6:39 PM
the hash is the key for each list
jax — Today at 6:39 PM
1 list with 100k words with 100k hashes with 100k lists
swordy — Today at 6:40 PM
and a hash is a randomly generated set of characters
each of the 100k lists is a list of line numbers
jax — Today at 6:40 PM
well the hash is value for each word
swordy — Today at 6:41 PM
the 100k words is a dictionary .. key is the word, value is the hash
jax — Today at 6:41 PM
also need to add list next to hash
swordy — Today at 6:41 PM
and the hash itself is displayed as a random set of characters
jax — Today at 6:42 PM
well idea here is to match a hash to a title_list
so yes
swordy — Today at 6:42 PM
so two structures to search .. {"word": "hash"} x 100k  and {"hash" : "["listitem1" , "listitem2"]} x 100k