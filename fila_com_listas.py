# Não use listas como fila
# FIFO - First in First Out
#   0    1    2
# ['A', 'B', 'C']
queue = []
queue.append('A')
print(queue)
queue.append('B')
print(queue)
queue.append('C')
print(queue)
print(queue.pop(0))
print(queue)
print(queue.pop(0))
print(queue)
print(queue.pop(0))
print(queue)
