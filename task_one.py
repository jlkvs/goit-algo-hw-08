import heapq

def min_cost_to_connect_cables(cables):
    if len(cables) <= 1:
        return 0

    heapq.heapify(cables)

    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)

        combined_length = first + second
        total_cost += combined_length

        heapq.heappush(cables, combined_length)

    return total_cost

cables = [4, 5, 21, 8]
print("Мінімальна вартість об'єднання:", min_cost_to_connect_cables(cables))
