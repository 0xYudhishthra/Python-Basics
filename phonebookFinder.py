phonebook = {}
entries=int(input())
for n in range(entries):
    name,num=input().strip().split(" ")
    name, num = [str(name),int(num)]
    phonebook[name] = num
    
for name in phonebook:
 try:
  search=str(input())
  if search in phonebook:
    output = ("{}={}".format(search,phonebook[search]))
    print (output)
  else:
    print ("Not found")
 except:
    break



    
