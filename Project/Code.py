## The admin password is admin.
#We are using databases in the form of csv files, so we import pandas libraries.

import pandas as pd


def passwordcheck(a,b):
        df = pd.read_csv('DataBase.csv', index_col ='Name')
        cell = df.loc[a, "Registration no."]
        if b==cell:
            return True
        else:
            return False
    

def numtosub(a):
    if a==1:
        return ('English')
    elif a==2:
        return ('Calculus')
    elif a==3:
        return ('Physics')
    elif a==4:
        return ('ICT')
    elif a==5:
        return ('PF')
    elif a==6:
        return ('OHT 1')
    elif a==7:
        return ('OHT 2')
    elif a==8:
        return ('Finals')


def gpacal(a):
        if a<=100 and a>=85:
                return 'A+'
        elif a>=80:
                return 'A'
        elif a>=75:
                return 'B+'
        elif a>=70:
                return 'B'
        elif a>=65:
                return 'C+'
        elif a>=60:
                return 'C'
        elif a>=55:
                return 'D'
        elif a>=35:
                return 'E'
        else:
                return 'F'

        
while True:
 print('\nWelcome to the Student Progress Portal')
 print('\nAre you a student or faculty?(reply with 1 or 2):')
 open = int(input())
 if open==1:
  print('\nPlease give your full name:')
  temp3 = input()
  print('\nPlease give your registration number:')
  passw = int(input())

 #a function to check the password (by matching name with reg no.)
        
  tempo = passwordcheck(temp3,passw)
  if tempo:
    df = pd.read_csv('DataBase.csv', index_col ='Name')
    print(df.loc[temp3])
    inn = input('Do you want to do anything else?\n(Give yes or no)')
    if inn!='yes':
           print('You have reached the end of the program.\nPlease restart the program.')
           break 
              
          
  else:
    print('\nYou have given wrong name or registration number.')
    

 else:
  print('Please give your admin password:')
  password = input()
  if password=='admin':
   print('\nWhat would you like to do? (reply with 1 or 2):')
   print('1. Read data\n2. Write data')
   temp1 = int(input())
  
   if temp1==1:
    print('\nWhat do you want to read? (reply with 1, 2 or 3):')
    print('1. Student Profile\n2. Exam Record\n3. Full Database')
    temp2 = int(input())
    if temp2==1:
        print('\nPlease give your full name:')
        temp3 = input()
        print('\nPlease give your registration number:')
        passw = int(input())

        #a function to check the password (by matching name with reg no.)
        
        tempo = passwordcheck(temp3,passw)
        if tempo:
            df = pd.read_csv('DataBase.csv', index_col ='Name')
            print(df.loc[temp3])
            inn = input('Do you want to do anything else?\n(Give yes or no)')
            if inn!='yes':
               print('You have reached the end of the program.\nPlease restart the program.')
               break          
            
        else:
            print('\nYou have given wrong name or registration number.')

    elif temp2==2:
           print('\nWhich Exam result do you want to see? (answer from 1 to 8)')
           print('1. English Composition')
           print('2. Calculus')
           print('3. Applied Physics')
           print('4. ICT')
           print('5. Programming Fundamentals')
           print('6. OHT 1')
           print('7. OHT 2')
           print('8. Finals')
           temp3 = int(input())
           sub = numtosub(temp3)
           df = pd.read_csv('DataBase.csv', index_col ='Name')
           print('Do you want to sort according to marks (sorted by registration no. by default)\nAnswer yes or no.')
           temp4 = input()
           if temp4=='yes':
               df_sorted = df.sort_values(by=sub,ascending=False)
               print(df_sorted[sub])
               inn = input('Do you want to do anything else?\n(Give yes or no)')
               if inn!='yes':
                   print('You have reached the end of the program.\nPlease restart the program.')
                   break
               
           else:
               print(df[sub])
               inn = input('Do you want to do anything else?\n(Give yes or no)')
               if inn!='yes':
                   print('You have reached the end of the program.\nPlease restart the program.')
                   break
             

    elif temp2==3:
            print('\nShould the data be ordered according to Total Marks?(answer 1 or 2)')
            print('1. Yes\n2. No')
            order = int(input())
            if order == 2:
              print()
              df = pd.read_csv('DataBase.csv', index_col ='Name')

              #We use df.to_string method so that whole database is shown instead of first and last 5 columns.
            
              print(df.to_string())
              inn = input('Do you want to do anything else?\n(Give yes or no)')
              if inn!='yes':
                 print('You have reached the end of the program.\nPlease restart the program.')
                 break
            else:
              print()
              df = pd.read_csv('DataBase.csv', index_col ='Name')
              df_sorted = df.sort_values(by='Percentage',ascending=False)
              print(df_sorted.to_string())
              inn = input('Do you want to do anything else?\n(Give yes or no)')
              if inn!='yes':
                  print('You have reached the end of the program.\nPlease restart the program.')
                  break 


   elif temp1==2:
       print('What do you want to write?\nAnswer 1 or 2')
       print('\n1. Alter an existing entry\n2. Enter a new entry')
       temp2 = int(input())
       if temp2==1:
           while True:    
              print('Write the name of the student whose entry you wish to alter:\n')
              temp3 = input()
              print('Which entry do you want to modify? (Answer from 1 to 8):')
              print('1. English Composition')
              print('2. Calculus')
              print('3. Applied Physics')
              print('4. ICT')
              print('5. Programming Fundamentals')
              print('6. OHT 1')
              print('7. OHT 2')
              print('8. Finals')
              temp4 = int(input())
              sub = numtosub(temp4)
              df = pd.read_csv('DataBase.csv', index_col ='Name')
              cell = df.loc[temp3, sub]
              print('\nThe existing value for',sub,'is:',cell)
              print('\nDo you wish to change it? (answer yes or no)')
              ans = input()
              if ans=='yes':
                   inp = eval(input('Give a new value:'))
                   df.loc[temp3, sub] = inp
                   df.to_csv('DataBase.csv')
                   print('The new entries are:')
                   print(df.loc[temp3])
                   temp5 = input('Do you wish to change some other entries? (answer with yes or no)\n')
                   if temp5!='yes':
                            print('\nYou have reached the end of program.\nPlease restart the program')
                            break
                                   
              else:
                      temp5 = input('Do you wish to change some other entries? (answer with yes or no)\n')
                      if temp5!='yes':
                         print('\nYou have reached the end of program.\nPlease restart the program')
                         break
           break
                       
       elif temp2==2:
               while True:
                       print('\nGive the name of the student:')
                       temp3 = input()
                       print('\nGive the Registration no:')
                       temp4 = int(input())
                       print('\nGive the marks of the following subjects:')
                       eng = int(input('English Composition:'))
                       calc = int(input('Calculus:'))
                       ap = int(input('Applied Physics:'))
                       ict = int(input('ICT:'))
                       pf = int(input('Programming Fundamentals:'))
                       oht1 = input('OHT 1 (Give the percentage):')+'%'
                       oht2 = input('OHT 2 (Give the percentage):')+'%'
                       finals = input('Finals (Give the percentage):')+'%'
                       total = eng+calc+ap+ict+pf
                       per = total/5
                       perc = str(total/5)+'%'
                       gpa = gpacal(per)
                       df = pd.read_csv('DataBase.csv', index_col ='Name')
                       df.loc[temp3] = [temp4,eng,calc,ap,ict,pf,oht1,oht2,finals,total,perc,gpa]
                       print('The following record is added.\n',df.loc[temp3])
                       df_sorted = df.sort_values(by='Registration no.',ascending=True)
                       df_sorted.to_csv('DataBase.csv')
                       print('\nDo you want to add more records? (reply with yes or no):')
                       temp5 = input()
                       if temp5!='yes':
                               break
               print('You have reached the end of the program.\nPlease restart the program.')
               break


