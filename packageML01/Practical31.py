def disp(**arr):
    print(type(arr),arr)
    for k in arr.keys():
        print(k,"=",arr[k])
disp(a='Android',b='Python',c='Java')
disp()