can have a word count aswell . and then when the line is 11 words long and we match 11 words in the dictionary , we know all other words dont apply to that title
checking every word of every title , while we match the first word. iterating through a limited number of lines. might allow us to search more lines with equal processing


we could also improve it to start with the "best" first word . Like a search algorithm would.  Searching titles that contain at least 1 word that is very popularly searched . and then search only 100k results that contain that word first... and then search those 100k results for the next most popular result . Then also set threshholds for how many maximum titles to search .. and another threshhold above that for how many results to return at a minimum. It will hit the maximum titles to search threshhold if it does not reach it's minimum search results
typed that a while ago
we can use an API that links to googles API
the API that says which words are popular



how long is it to search a single dictionary of 100k entries?
jax — Today at 6:57 PM
10 microsec



youre just running a word into a function
that hash is prb linked to some memory address
swordy — Today at 7:05 PM
trying to find an algorithm .
so thats why we dont need to generate a hash, python automatically generates the hash , and it's stored in memory like you said



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
yeah
i mean looks like we can keep 10k articles per search word and brute force it
i can run prb run 1 billion cycles and not have an issue
but i like your idea as well
also these words are very unique
swordy — Today at 7:44 PM
so with the idea of omitting words i see we would be having a secondary dictionary that lists all the words that aren't unique
jax — Today at 7:44 PM
like deoxyribose
or 1,2-hydroxysomething
swordy — Today at 7:44 PM
and they just wouldnt be used for a search query
but we still store them
(have to know what they are to not use them)
jax — Today at 7:45 PM
i mean we can filter simple words
but google isnt gonna help us with scientific words much
i was thinking of using the quantum computers online
lol
swordy — Today at 7:46 PM
google also going to get shite about API calls
jax — Today at 7:47 PM
yeah they limit everything
swordy — Today at 7:47 PM
I think we can index all specific words in a subject .. up to a limit
jax — Today at 7:47 PM
tried their voice apis limit was 50/day
swordy — Today at 7:48 PM
could show top articles based on those words
thats a value
jax — Today at 7:49 PM
lol i hate n^2 problems
the thing is sometimes an off shoot article may be meaningful
so well have to brute it
swordy — Today at 7:50 PM
this thing can search all of those articles based on waht users are looking for .. and then further index based on inclusion of specific words in those articles .
maybe even more specifically how many times... and designing a quality index
jax — Today at 7:50 PM
i mean out of 20 mill articles well prb get some 10k entries for each term
so not bad
caching comes in later
swordy — Today at 7:51 PM
the main thing is 20 million articles is nuts to obtain , and continuously retrieving 20 million new articles
jax — Today at 7:52 PM
yeah the list is larger
well its no complete
but would make a difference in searching
one idea is also to connect this to opencog
opencog is a general ai thing
that way it can do research much faster
u know sophia the ai on youtube
her brains are on github
swordy — Today at 7:53 PM
i've heard an AI that answers phones
havent heard of sophia the AI
jax — Today at 7:54 PM
the way they put info is in a knowledge base
essentially a tree
so u cut braches, add new ones, compare etc
kinda like what a human brain does
in science usually new articles have more worth than old ones
so popularity in this case isnt gonna work best
its usually about the things we dont know yet
swordy — Today at 7:56 PM
imagine generating new articles based on old ones :smile:
jax — Today at 7:56 PM
yeah thats the idea
i do learn new things from old articles
theres an project called entrez for bio
usually lets u do searches across their dbs
one thing that seems to be an issue with mass data is speed
i mean another thing would be to just build a massive hashmap
as much as u can fit
lol
swordy — Today at 7:59 PM
always thinking what is the file size
and how long does it take to query it
in 20 million , maybe its not a big thing . but it is scalable i see
jax — Today at 8:00 PM
well file size would be in TB
and query would be in microsecs range
swordy — Today at 8:01 PM
thats incredible