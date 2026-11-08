parts = input().split()


def level(v):
    if v < -105:
        return    "zeif"
    elif v < -95:
        return    "orta"
    else:
        return    "yaxshi"


values = []
missing = 0
for p in parts:
    if p ==    "NA":
        missing = missing + 1
    else:
        values.append(float(p))

print("Olchme:", len(values))
print("Bosh:", missing)


print("Min:", min(values))
print("Max:", max(values))
print("Orta qiymet:", round(sum(values) / len(values), 1))


for v in values:
    print(v, "→", level(v))


counts = {"zeif": 0, "orta": 0, "yaxshi": 0}
for v in values:
    s = level(v)
    counts[s] = counts[s] + 1
print(counts)

share = round(counts["zəif"] / len(values) * 100, 1)
print("Zeif payı:", share, "%")
if share >= 30:
    print("Qerar: briqadani gonder")
elif share >= 10:
    print("Qerar: müşahidede saxla")
else:
    print("Qerar: stansiya normaldir")

current =   0
best =    0
for v in values:
    if level(v) ==   "zeif":
        current = current + 1
        if current > best:
            best =   current
    else:
        current = 0
print("En uzun zeif:", best)