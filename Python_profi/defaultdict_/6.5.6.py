from collections import defaultdict


def best_sender(messages, senders):
    result = defaultdict(int)
    for i, message in enumerate(messages):
        result[senders[i]] += len(message.split())
    max_value = max(result.values())
    return max([k for k, v in result.items() if v == max_value])


messages = ['Hi, Linda', 'Hi, Sam', 'How are you doing?']
senders = ['Sam Fisher', 'Linda', 'Sam Fisher']

print(best_sender(messages, senders))

messages = ['How is Stepik for everyone', 'Stepik is useful for practice']
senders = ['Bob', 'Charlie']

print(best_sender(messages, senders))

messages = ['bu bu da', 'bu bu da', 'bu bu da', 'bu bu da', 'bu bu da', 'bu bu net']
senders = ['dima', 'anri', 'timur', 'timur', 'anri', 'dima']

print(best_sender(messages, senders))

# beauty
# def best_sender(messages, senders):
#     result = defaultdict(int)
#     for sender, message in zip(senders, messages):
#         result[sender] += len(message.split())
#     return max(result, key=lambda p: (result[p], p))
