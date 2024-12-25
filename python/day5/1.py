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

def is_sorted_by_rules(update):
    for i in range(len(update) - 1):
        for j in range(i + 1, len(update)):
            if (update[j], update[i]) in rules:
                return False
    return True

correctly_ordered_updates = [update for update in updates if is_sorted_by_rules(update)]

middle_page_numbers = [update[len(update) // 2] for update in correctly_ordered_updates]

result = sum(middle_page_numbers)

print(result)