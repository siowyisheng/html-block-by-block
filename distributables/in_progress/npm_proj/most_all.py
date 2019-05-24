with open('pop_packages.txt','r') as f:
    lines = f.readlines()

pagerank = set()
hits = set()
depended_on = set()
HITSRANK_MARKER = 'HITS RANK'
PAGERANK_MARKER = 'PAGERANK'
DEPENDED_ON_MARKER = 'DEPENDED-ON'
current = HITSRANK_MARKER
marker_to_set = {HITSRANK_MARKER:hits,PAGERANK_MARKER:pagerank,DEPENDED_ON_MARKER:depended_on}
for line in lines:
    split = line.split()
    if len(split) == 0:
        continue
    interesting = split[0]
    if interesting == PAGERANK_MARKER:
        current = PAGERANK_MARKER
    elif interesting == DEPENDED_ON_MARKER:
        current = DEPENDED_ON_MARKER
    else:
        marker_to_set[current].add(interesting)

pops = pagerank & hits & depended_on
pops = '\n'.join(list(pops))

with open('out.txt','w') as f:
    f.write(pops)
