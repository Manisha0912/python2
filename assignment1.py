
# 2.Duplicates and uniques in an array

list1 = [1, 1, 4, 5, 6, 6]
freq = {} 

for i in list1:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
for i in freq:
    if freq[i] > 1:
        print(i, "Duplicate")
    else:
        print(i, "Unique")

        

# 4.Missing number in a list
# i-XOR
lis=[1,2,3,4,5,7]
n=7
res=0
for i in range(1,n+1):
    res=res^i
for i in lis:
    res=res^i
print(res)
# ii-natural number
list=[1,2,3,4,5,7]
sum=0
n=7
total=n*(n+1)//2
for i in list:
    sum=sum+i

missing =total-sum
print(missing)

# iii) nested for loop-
lit=[1,2,3,4,6,7,8]
n=8
def missingnum(lit,n):
    for i in range(lit,n):
        flag=false
        for j in lit:
            if j==i:
                found=Truebreak
            else:
                print("Missing Num:",i)    
                


#7.SUBSET-
arr1=[2,4,6,8,10]
arr2=[2,4,9]
def subset(arr1,arr2):
    for i in arr2:
        flag=False
        for j in arr1:
            if i==j:
                flag=True
                break
            else:
                return False
            return True    
print(subset(arr1,arr2))     

# a+b=Target
# O(logn^2)
def function():
    list2=[1,2,3,4]
    target=5
    flag=False
    for i in  range(len(list2)):
        for j in range(i+1,len(list2)):
                if list2[i]+list2[j]==target:
                     print(f"{list2[i]}+{list2[j]}={target}")
                     flag=True 
                    
    if not flag:
               print("No pairs found")                       
function()   


#  O(nlogn)  

def target():
    list5=[1,2,3,4,5]
    target=6
    
    high=len(list5)-1
    low=0

    while low < high:
        sum = list5[low] + list5[high]
        if sum == target:
            print("target found",list5[low],list5[high])
            return
        elif sum>target:
            high-=1
        else:
            low+=1
target()       
       

    


                 




     


