with open("input") as f:
    rules, updates = f.read().split("\n\n")

rules = rules.split("\n")
updates = updates.split("\n")

updates = [list(map(int, update.split(","))) for update in updates]

rules = [(int(rule.split("|")[0]), int(rule.split("|")[1])) for rule in rules]

def find_rules_for(x):
    r = []
    for rule in rules:
        if x == rule[0]:
            r.append(rule[1])
    return r

def get_invalid_pair(update):
    for i in range(len(update) - 1):
        for j in range(i + 1, len(update)):
            if (update[j], update[i]) in rules:
                return (i, j)
    return None

incorrectly_ordered_updates = [update for update in updates if get_invalid_pair(update) is not None]


for update in incorrectly_ordered_updates:
    while get_invalid_pair(update) is not None:
        i, j = get_invalid_pair(update)
        update[i], update[j] = update[j], update[i]

middle_page_numbers = [update[len(update) // 2] for update in incorrectly_ordered_updates]
print(sum(middle_page_numbers))