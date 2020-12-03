def latest(scores):
    return scores[-1]


def personal_best(scores):
    high_scores = sorted(scores, key=int)
    return high_scores[-1]



def personal_top_three(scores):
    if len(scores) >= 3:
        high_scores = sorted(scores, key=int, reverse = True)
        return high_scores[0:3]
    else: 
        high_scores = sorted(scores, key=int, reverse = True)
        return high_scores
 
   
