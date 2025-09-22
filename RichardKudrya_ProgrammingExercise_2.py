# Description:
# This program will scan for 30 different words/phrases that are most common in spam emails/messages
# and will display the results of the message including the spam score, likelihood it is a spam, and the
# words/phrases that were detected.

import re
import sys

KEYWORDS = [
    "free", "only today", "limited time", "click here", "winner", "congratulations",
    "earn money", "make money fast", "no catch", "guaranteed", "risk-free",
    "buy now", "special promotion", "urgent", "limited offer", "100% free",
    "lapply now", "once in a lifetime", "miracle", "hidden charges", "offer expires",
    "cash bonus", "credit card", "urgent response needed", "loan", "earn extra cash",
    "act immediately", "no fees", "cure", "no hidden costs"
]

def compile_patterns(keywords):

    patterns = []
    for kw in keywords:
        esc = re.escape(kw)
        pattern = r'\b' + esc + r'\b'
        patterns.append(re.compile(pattern, flags=re.IGNORECASE))
    return patterns

# Scans the message for each keyword/phrase and adds one point to the spam score.
def score_message(message, patterns, keywords):
    counts = {k: 0 for k in keywords}
    for pat, kw in zip(patterns, keywords):
        matches = pat.findall(message)
        if matches:
            counts[kw] = len(matches)
    score = sum(counts.values())
    return score, counts

# Returns the likelihood of spam according to the score
def interpret_score(score, total_keywords=len(KEYWORDS)):
    if score == 0:
        return "Very unlikely"
    pct = score / total_keywords
    if pct <= 0.1:
        return "Unlikely"
    elif pct <= 0.3:
        return "Possible"
    elif pct <= 0.6:
        return "Likely"
    else:
        return "Very likely"

def print_results(score, interpretation, counts):
    print("\n-Spam Scan Results-")
    print(f"Spam score: {score}")
    print(f"Likelihood: {interpretation}\n")
    triggered = {k:v for k,v in counts.items() if v>0}
    if not triggered:
        print("No spammy words or phrases have been found.")
    else:
        print("Words/phrases that caused the message to be a spam:")
        for k,v in sorted(triggered.items(), key=lambda x: -x[1]):
            print(f" - {k!r}: {v} occurrence{'s' if v>1 else ''}")

def main():
    print("30 Word/Phrase Spam Detector\nEnter your message. (Press Enter Twice).")
    lines = []
    try:
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
    except EOFError:
        pass
    message = "\n".join(lines)
    if not message.strip():
        print("No message was detected.")
        sys.exit(0)
    patterns = compile_patterns(KEYWORDS)
    score, counts = score_message(message, patterns, KEYWORDS)
    interpretation = interpret_score(score)
    print_results(score, interpretation, counts)

if __name__ == "__main__":
    main()
