visitors=[120,150,90,200,170,130,160]
highest_traffic=max(visitors)
highest_day=visitors.index(highest_traffic)+1
print("Highest traffic",highest_traffic)
print("Day with highest traffic Day",highest_day)
lowest_traffic=min(visitors)
lowest_day=visitors.index(lowest_traffic)+1
print("Lowest traffic",lowest_traffic)
print("Day with lowest traffic Day",lowest_day)
