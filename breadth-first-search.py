from collections import deque

graph = {
    'you': [
        'alice', 'bob', 'claire'
    ],
    'bob': [
        'anuj', 'peggy'
    ],
    'alice': [
        'peggy'
    ],
    'claire': [
        'thom', 'johnny'
    ],
    'anuj': [], 'peggy': [],
    'thom': [], 'johny': []
}


def person_is_seller(person):
    return True if person == 'thom' else False


def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            print(person)
            if person_is_seller(person):
                print(person + ' is a mango seller!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


search('you')
