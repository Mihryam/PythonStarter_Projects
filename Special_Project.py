ry:
    bestieNum = int(input('Please input your bestie number:  '))
    bestie = input('What is your bestfriend name: ')
    specialNum = int(input('Special number please: '))
    average_nom = bestieNum/specialNum
      
    
    if bestie.isdigit():
        print('Your bestfriend is a number?!! Really?')
    elif bestie.isalpha():
        print(f'My best friend name is {bestie.title()}. This is our mutual average no : {average_nom}')  (
    
    print('Yoy dont want your betie to know that you cant spell. Do you?')          
    
except ValueError:
    print('Incorrect Value!!! Plese input the right value')
except ZeroDivisionError:
    print('Please check your values, you have a scary number 0: ')



a
    
            
