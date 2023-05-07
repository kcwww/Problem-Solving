def solution(new_id):
    special = "~!@#$%^&*()=+[{]}:?,<>/"
    id_sizes = len(special)
    new_id = new_id.lower()
    for i in range(id_sizes):
        if special[i] in new_id:
            new_id = new_id.replace(special[i], '')

    while ('...' in new_id):  
        new_id = new_id.replace('...', '.')
    while ('..' in new_id):
        new_id = new_id.replace('..', '.')
    
    
    if len(new_id) > 0 and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) > 0 and new_id[-1] == '.':
        new_id = new_id[:-1]
    if new_id == '':
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[0:-1]
    elif len(new_id) <= 2:
        while (len (new_id) != 3):
            new_id = new_id + new_id[-1]
    return new_id