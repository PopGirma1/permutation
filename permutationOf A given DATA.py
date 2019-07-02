def permutation(Ourgroup):
    length=len(Ourgroup)
    if length <= 1:
        yield Ourgroup
    else:
        for n in range(0,length):
             for end in permutation( Ourgroup[:n] + Ourgroup[n+1:] ):
                 yield [ Ourgroup[n] ] + end
l=input(" enter value you want to check the order the value you entered in ")
Ourgroup=list(l)
count=0
for x in permutation(Ourgroup):
    count=count+1
    print (x)
print(" the number of order of you given data is ",count)
