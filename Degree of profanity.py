import re

def calculate_profanity_score(sentence, slurs):
   
    pattern = re.compile(r'\b({})\b'.format('|'.join(slurs)), re.IGNORECASE)

    
    matches = pattern.findall(sentence)

  
    return len(matches)

def calculate_profanity_scores(tweets_file, slurs):
    
    profanity_scores = []
    with open(tweets_file, 'r') as f:
        for tweet in f:
            score = calculate_profanity_score(tweet, slurs)
            profanity_scores.append((tweet, score))
    return profanity_scores


slurs = ['nigger', 'faggot', 'cunt']
tweets_file = 'tweets.txt'
profanity_scores = calculate_profanity_scores(tweets_file, slurs)
for tweet, score in profanity_scores:
    print(f'Tweet: {tweet}Profanity score: {score}')
