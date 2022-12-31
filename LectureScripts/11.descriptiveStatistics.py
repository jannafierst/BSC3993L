from collections import Counter
from matplotlib import pyplot as plt

num_friends = [100, 40, 41, 49, 25, 2, 36, 5, 24, 78, 95, 96, 45, 43, 57, 56, 25, 28, 29, 82, 86, 84, 57, 29, 22, 24, 25, 27, 23, 20, 21, 20, 20, 20, 65, 62, 63, 64, 65, 78, 77, 77, 24, 29, 28, 19, 19, 18, 43, 45, 47, 30, 30, 40, 51]

friend_counts = Counter(num_friends)
xs = range(101)
ys = [friend_counts[x] for x in xs]
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("Histogram of Friend Counts")
plt.xlabel("# of friends")
plt.ylabel("# of people")
plt.show()

num_points = len(num_friends)

largest_value = max(num_friends)
smallest_value = min(num_friends)

sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]
second_smallest_value = sorted_values[1]
second_largest_value = sorted_values[-2]

def mean(x):
    return sum(x)/ len(x)

print(mean(num_friends))

def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n //2
    if n % 2 == 1:
        return sorted_v[midpoint]
    else:
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2

print(median(num_friends))

def quantile(x,p):
    p_index = int(p*len(x))
    return sorted(x)[p_index]

quantile(num_friends, 0.10)
quantile(num_friends, 0.25)
quantile(num_friends, 0.75)
quantile(num_friends, 0.90)

def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.iteritems()
                if count == max_count]

mode(num_friends)

def data_range(x):
    return max(x) - min(x)

print(data_range(num_friends))

def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return sum(deviations) / (n-1)

print(variance(num_friends))

print(mean(num_friends))
