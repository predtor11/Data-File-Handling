print("SET THE LOCATION OF FILE IN YOUR SYSTEM MANUALLY")
print("\n")
print("WELCOME TO DATA FILE HANDLING")

import os

def pri():
    print("\n")
    print("1 - CREATION OF TEXT FILE")
    print('2 - READING OF A TEXT FILE')
    print('3 - DELETION OF A TEXT FILE')
    print('4 - OPERATION PERFORMED ON THE TEXT')
    print("5 - EXIT")
    return("\n")

def ope():
    print("\n")
    print("1 - TOTAL NUMBER OF LINES")
    print("2 - TOTAL NUMBER OF WORDS")
    print("3 - TOTAL NUMBER OF CHARACTERS")
    print("4 - TOTAL NUMBER OF PARTICULAR CHARACTER")
    print("5 - TOTAL NUMBER OF VOWELS")
    print("6 - TOTAL NUMBER OF CONSONANTS")
    return("\n")

def inp():
    global b
    print("\n")
    print("'YES' FOR CONTINUE")
    print("'NO' FOR EXIT")
    print("\n")
    b = input("DO YOU WANT TO CONTINUE?? :\t")
    if b=="no" or b=="NO":
        print("THANKS FOR USING THE PROGRAM :):) ")


while True:
    
    print(pri())
    l=[]
    s=''.join(l)
    q = int(input("Enter your choice:\t"))
    
    #CREATION OF TEXT FILE
    
    if q==1:
        print("\n")
        u = input("Enter the Name of the File:\t")
        f = open("D:\XII\CS\Python Programs\MENU BASED\Main/%s.txt"%u,"w")
        q+=1
        print("\n")
        print("'YES' FOR WRITING")
        print("\n")
        print("'NO' FOR NOT WRITING")
        print("\n")
        v = input("Do You Want to Write?:\t")
        print("\n")
        
        if v=='YES' or v=='yes':
            n=int(input("Enter the Number of Lines:\t"))
            print("\n")
            
            for i in range(1,n+1):
                ch=input("ENTER THE STATEMENT %d :\t"%i)
                l.append(ch)
                
            for i in l:
                f.writelines(i)
                f.writelines("\n")
                continue
            print("FILE NAMED %s IS SUCCESFULLY CREATED :)"%u)
        else:
            inp()
            print("\n")
            
            if b=="YES" or b=="yes":
                continue
            else:
                break

                
    #READING OF A TEXT FILE
            
    elif q==2:
        print("\n")
        print("NOTE - ENTER THE NAME OF THE FILE THAT EXISTS.")
        print("\n")
        u=input("ENTER THE NAME OF THE FILE:\t")
        print("\n")
        j = os.path.exists("D:\XII\CS\Python Programs\MENU BASED\Main/%s.txt"%u)
        if j == True:
            f = open("D:\XII\CS\Python Programs\MENU BASED\Main/%s.txt"%u,"r")
            for l in f.readlines():
                print(l)
            f.close()
        else:
            print("\n")
            print("FILE DOES NOT EXISTS.")
        inp()
        if b=="YES" or b=="yes":
            continue
        else:
            break
        
    #DELETION OF A TEXT FILE
        
    elif q==3:
        print("\n")
        u=input("ENTER THE NAME OF THE FILE:\t")
        print("\n")
        j = os.path.exists("D:\XII\CS\Python Programs\MENU BASED\Main/%s.txt"%u)
        if j == True:
            os.getcwd()
            os.remove("D:\XII\CS\Python Programs\MENU BASED\Main/%s.txt"%u)
            print("\n")
            print("FILE NAMED %s IS SUCCESFULLY DELETED :)"%u)
        else:
            print("\n")
            print("FILE DOES NOT EXISTS.")
        inp()
        if b=="YES" or b=="yes":
            continue
        else:
            break

    #OPERATION PERFORMED ON THE TEXT
        
    elif q==4:
        print("\n")
        print("NOTE - ENTER THE NAME OF THE FILE THAT EXISTS.")
        u=input("ENTER THE NAME OF THE FILE:\t")
        print("\n")
        j = os.path.exists("D:\XII\CS\Python Programs\MENU BASED\Main/%s.txt"%u)
        if j == True:
            f = open("D:\XII\CS\Python Programs\MENU BASED\Main/%s.txt"%u,"r")
            k = []
            a = f.readlines()
            
            for i in a:
                k.append(i)
                z = ''.join(k)
            print(ope())
            print("\n")
            x = int(input("WHAT DO YOU WANT TO DO?:\t"))
            
            if x == 1:
                #NUMBER OF LINES
                print("\n")
                print("TOTAL NUMBER OF LINES:\t",len(k))
                inp()
                if b=="YES" or b=="yes":
                    continue
                else:
                    break
                
            elif x==2:
                #NUMBER OF WORDS
                w = 0
                for j in z.split():
                    w+=1
                print("\n")
                print("Number of Total Words:\t",w)
                inp()
                if b=="YES" or b=="yes":
                    continue
                else:
                    break
                #NUMBER OF CHARACTERS
            elif x==3:
                print("\n")
                print("Number of chracters:\t",len(z))
                inp()
                if b=="YES" or b=="yes":
                    continue
                else:
                    break

            elif x==4:
                #PARTICULAR CHARACTER COUNT
                print("\n")
                chr=input("Enter the Chracter you want to count:\t")
                print("\n")
                c=0
                for i in range(0,len(z)):
                    if z[i]==chr:
                        c=c+1
                print("\n")
                print("Total Number of Characters",chr,":\t",c)
                inp()
                if b=="YES" or b=="yes":
                    continue
                else:
                    break


            elif x==5:
                #NUMBER OF VOWELS
                v = 0
                for i in z:
                    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
                        v+=1
                print("\n")
                print("NUMBER OF VOWELS: ",v)
                inp()
                if b=="YES" or b=="yes":
                    continue
                else:
                    break


            elif x==6:
                #NUMBER OF CONSONANTS
                c = 0
                for i in z:
                    if i!='a' or i!='e' or i!='i' or i!='o' or i!='u' or i!='A' or i!='E' or i!='I' or i!='O' or i!='U':
                        c+=1
                print("\n")
                print("NUMBER OF CONSONANTS",c)
                inp()
                if b=="YES" or b=="yes":
                    continue
                else:
                    break
            elif x==7:
                #Character Replace
                a = f.read()
                


        
        else:
            print("FILE DOES NOT EXISTS")
            

    #EXIT
    elif q==5:
        print("\n")
        print("THANKS FOR USING THE PROGRAM :):) ")
        break



