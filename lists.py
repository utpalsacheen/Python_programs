# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print 
# remove 6
# append 9
# append 1
# sort 
# print
# pop
# reverse
# print

n = int(raw_input().strip())

L = []

for t in range(n):
   args = raw_input().strip().split(" ")
   if args[0] == 'print':
      print L
   elif len(args) == 3:
      getattr(L, args[0])(int(args[1]), int(args[2]))
   elif len(args) == 2:
      getattr(L, args[0])(int(args[1]))
   else:
      getattr(L, args[0])()
