
def one_away(str1, str2):

  if len(str1)<len(str2):
    str1, str2 = swap_str(str1, str2)

  if len(str1)-len(str2)>1:
    return False
  
  is_one_way = True


  for j,s in enumerate(str2):
    if str1[j]!=str2[j]:

      #case 1 same length
      if (len(str1)==len(str2)):
        for k in range(j+1,len(str1)):
          if str1[k]!=str2[k]:
            is_one_way = False
            break
      #case 2 different lengths
      else:
        for k in range(j+1,len(str1)):
          if str1[k]!=str2[k-1]:
            is_one_way = False
            break
    
    

  return is_one_way

def swap_str(str1, str2):
  return str2, str1


str1 = "pale"
str2 = "ple"

print(str1,str2)
print(one_away(str1, str2))


str1 = "pale"
str2 = "bale"

print(str1,str2)
print(one_away(str1, str2))



str1 = "pale"
str2 = "pales"

print(str1,str2)
print(one_away(str1, str2))

str1 = "pale"
str2 = "bake"

print(str1,str2)
print(one_away(str1, str2))
