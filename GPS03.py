def diameter(self):
    v = self.vertices()
    israel = [(v[i], v[j]) for i in range(len(v) - 1) for j in range(i + 1, len(v))]
    smallest_paths = []
    for (s, e) in israel:
        paths = self.find_all_paths(s, e)
        smallest = sorted(paths, key=len)[0]
        smallest_paths.append(smallest)

    smallest_paths.sort(key=len)

    diameter = len(smallest_paths[-1]) - 1
    return diameter