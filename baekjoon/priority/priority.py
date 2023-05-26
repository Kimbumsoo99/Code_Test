import heapq as hq

pq = []
hq.heappush(pq, 6)
hq.heappush(pq, 12)
hq.heappush(pq, 0)
hq.heappush(pq, -5)
hq.heappush(pq, 8)
#print(pq)
#while pq:
    #print(pq[0])
    #print(hq.heappop(pq))

s = set()
s.add(123) # add로 값 넣기 가능
s.add(123) # 중복은 삽입 X
s.add(789)
s.add(456)
print(s)
print(len(s))
print(s.pop()) # 랜덤
s.remove(789)
print(s)
s.clear()
print(s)