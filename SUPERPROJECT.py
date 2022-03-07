# try:
#     a = 12
#     b = 0
#     c = a/b
#     print(c)
# except ValueError:
#     print("o dimma")
# except ZeroDivisionError:
#     print('Cant do this')    

def tester():
    try:
        bestieNum = int(input('Please input your bestie number:  '))
        specialNum = int(input('Special number please: '))
        average_nom = bestieNum/specialNum

        def bestieName():

            bestie = input('What is your bestfriend name: ')
            if bestie.isdigit():
                print('Your bestfriend is a number?!! Really?')
                bestieName()

            elif bestie.isalpha():
                print(f'My best friend name is {bestie.title()}. This is our mutual average no : {average_nom}')  
            else:
                print('Please input yur best frirnd name correctly')
                bestieName()
        bestieName()        


    
    except ValueError:
        print('Incorrect Value!!! Plese input the right value')
        tester()


    except ZeroDivisionError:
        print('Please check your values, you have a scary number 0: ')

tester()


    
            
