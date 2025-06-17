def reward_function(text):
    rhyme_score = sum(1 for line in text.splitlines(
    ) if line.strip().endswith(("ay", "ee", "ow", "ight", "oon")))
    length_score = len(text.split())
    return rhyme_score + 0.1 * length_score


def rerank_results(search_results):
    docs = search_results["documents"][0]
    scored_docs = sorted(docs, key=reward_function, reverse=True)
    return scored_docs
