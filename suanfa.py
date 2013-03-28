q_sort=lambda l:l if len(l)<=1 else q_sort([x for x in l[1:] if x<l[0]])+[l[0]]+q_sort([x for x in l[1:] if x>=l[0]])
print q_sort([2,3,1,9,8,4,5])