# hackerrank.com/challenges/symmetric-difference/problem
m = int(input())
mset = set(map(int,input().split()))
n = int(input())
nset = set(map(int,input().split()))
dset = [*mset.difference(nset),*nset.difference(mset)]
[print(i)for i in sorted(dset)]


