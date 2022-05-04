import json

def myfunction():
   
    
    
    marks=[]
    names=["ali","mohamad","samer"]
    for i in range (3):
             mark=0 
             nstudent=input("enter student name: "+str(names[i]))
             q1=input("question1 ?")
             q2=input("question2 ?")
             q3=input("question3 ?")
             q4=input("question4 ?")
             q5=input("question5 ?")
             q6=input("question6 ?")
             q7=input("question7 ?")
             q8=input("question8 ?")
             q9=input("question9 ?")
             q10=input("question10 ?")
             q11=input("question11 ?")
             q12=input("question12 ?")
             q13=input("question13 ?")
             q14=input("question14 ?")
             q15=input("question15 ?")
             q16=input("question16 ?")
             q17=input("question17 ?")
             q18=input("question18 ?")
             q19=input("question19 ?")
             q20=input("question20 ?")
        

             if q1=="a1":
                 mark+=1
             else:
                 mark+=0
             if q2=="a2":
                 mark+=1
             else:
                 mark+=0
             if q3=="a3":
                mark+=1
             else:
                mark+=0
             if q4=="a4":
                mark+=1
             else:
                mark+=0
             if q5=="a5":
                mark+=1
             else:
                mark+=0
             if q6=="a6":
                mark+=1
             else:
                mark+=0                                  
             if q7=="a7":
                mark+=1
             else:
                mark+=0
             if q8=="a8":
                mark+=1
             else:
                mark+=0
             if q9=="a9":
                mark+=1
             else:
                mark+=0
             if q10=="a10":
                mark+=1
             else:
                mark+=0   
             if q12=="a11":
                mark+=1
             else:
                mark+=0
             if q12=="a12":
                mark+=1
             else:
                mark+=0   
             if q13=="a13":
                mark+=1
             else:
                mark+=0
             if q14=="a14":
                mark+=1
             else:
                mark+=0
             if q15=="a15":
                mark+=1
             else:
                mark+=0
             if q16=="a16":
                mark+=1
             else:
                mark+=0
             if q17=="a17":
                mark+=1
             else:
                mark+=0
             if q18=="a18":
                mark+=1
             else:
                mark+=0
             if q19=="a19":
                mark+=1
             else:
                mark+=0
             if q20=="a20":
                mark+=1
             else:
                mark+=0   
                
             print("his mark is: " +str(mark))
             marks.append(mark)
            
    d={} 
    for i in range(3):
             
            name=names[i]
            mark=marks[i]       
            d[name]={"name":name,"mark":mark}
                  
              
    file=json.dumps(d)
    with open ("xyz.json","w") as f:
          f.write(file)
    with open("xyz.json","r") as f:
        content=json.loads(f.read())
    print(content)
    
             
                
    

                 
             
                
    

             
             
             
    
             


        
        
        
        
        
        
     
