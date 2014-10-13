#coding=utf8

def cumulative_sum(listx):
        list_sum = []
        for i in range(len(listx)):
            if i == 0:
                    list_sum.append(listx[i])
            else:
                    list_sum.append(list_sum[i-1]+listx[i])
        return list_sum
if __name__ == '__main__':
        print cumulative_sum([2,3,10,200])
