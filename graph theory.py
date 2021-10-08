def mat2list(l:list):
    "convert matrix to ad_list"
    result=[]
    for i,n in enumerate(l):
        for i_2 in range(len(l)):
            if n[i_2]==1:
                result.append((i,i_2))
    return result

a=[[0,0,0,1,0],[0,0,0,0,1],[1,0,0,1,0],[1,1,1,0,0],[1,0,0,0,0]]

print(mat2list(a))


def list2mat(l:list):
    dim=max([max(i) for i in l])+1
    result=[[0]*dim for i in range(dim)]
    for key,val in enumerate(l):
        result[val[0]][val[1]]=1
    return result


def mat2dic(l:list):
    result={}
    for key ,val in enumerate(l):
        l=[]
        for key_2,val_2 in enumerate(val):
            if val_2==1:
                l.append(key_2)
        result[key]=l
    return result


print(mat2dic(a))

def dic2mat(d:dict):
    dim=max(d.keys())+1
    result=[[0]*dim for i in range(dim)]
    for i,(k,v) in enumerate(d.items()):
        for k_2,v_2 in enumerate(v):
            result[k][v_2]=1
    return result

