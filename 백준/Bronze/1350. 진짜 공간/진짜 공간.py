N = int(input())
file_size = list(map(int, input().split()))
cluster_size = int(input())

cluster_num=0
for i in file_size:
    if i < cluster_size:
        if i == 0:
            cluster_num += 0
        else:
            cluster_num += 1
    else:
        cluster_num += (i//cluster_size)
        if i%cluster_size > 0:
            cluster_num += 1
print(cluster_num*cluster_size)