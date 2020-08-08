tel = {'jatheen' : 75, 'shilpa' : 83, 'ishaan' : 11, 'nishka' : 13}
family = list(tel.keys())
print(family)
tel['sacheen'] = 80
tel['utpal'] = 85

sorted_fam = sorted(tel.keys())
print(sorted_fam)

for k, v in tel.items():
    print(k,v)

del tel['sacheen']
tel['rahul'] = 81

is_he = 'sacheen' in tel
print(is_he)

urva = dict(ramesh=70,ramani=65)
print(urva)

n = int(raw_input().strip())
students = {}
for line in range(n):
    line_info = raw_input().split(" ")
    scores = map(float, line_info[1:])
    students[line_info[0]] = sum(scores)/float(len(scores))

print "%.2f" % students[raw_input()]
