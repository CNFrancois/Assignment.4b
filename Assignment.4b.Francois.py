import time
print('Hello my name is Francois I shall be your waiter this evening\nWhat would you like to drink this evening?')
drink=input()
if drink == 'nothing':
    time.sleep(5)
    print('**Five minutes later**\n')
    print('\nThe entrées for tonight are as follows')
    a='\noption a: spring rolls, deep fried roll skin wrapped with minched \nvegetables and clear noodles, served with a sweet sauce'
    b='\noption b: spicy beef salad, grilled sliced beef with red onions, \ntomatoes, mushroom, cilantro and roasted chilli lime dressing'
    c='\noption c: crying tiger, grilled marinated steak, sliced in thai \nstyle served with spicy house sauce and stiky rice on the side'
    d='\noption d: drunken noodles, stir-fried flat noodles with ground \nchichen, egg, onions, bell peppers, \nand basil in our hot and spicy house sauce'
    print(a,'\n',b,'\n',c,'\n',d)
    print('\nAre you ready to order?')
    ready=input()
    if ready == 'yes':
        print('\nWhat option would you care for this evening, would you care for a, b, c, or d?\n or would you care to hear the menu again?')
        print('a, b, c, or d?')
        option=input()
        time.sleep(5)
        print('\n**15 minutes later**')
        print('\nWaiter returns with','option ',option)
        time.sleep(5)
        print('\n**30 minutes later**')
        print('\n**Placing bill on table**')
        time.sleep(5)
        print('\n**collects payment**')
        time.sleep(5)
        print('\n**returns with receipt**')
        print('\nThank you very much, please enjoy the rest of your evening')
    else:
                print('\nI will be back in a few minutes')
                time.sleep(5)
                print(a,'\n',b,'\n',c,'\n',d)
                print('\nAre you ready?')
                ready=input()
                if ready == 'yes':
                    print('\nWhat option would you care for this evening, would you care for a, b, c, or d?\n or would you care to hear the menu again?')
                    print('a, b, c, or d?')
                    option=input()
                    time.sleep(5)
                    print('\n**15 minutes later**')
                    print('\nWaiter returns with','option ',option)
                    time.sleep(5)
                    print('\n**30 minutes later**')
                    print('\n**Placing bill on table**')
                    time.sleep(5)
                    print('\n**collects payment**')
                    time.sleep(5)
                    print('\n**returns with receipt**')
                    print('\nThank you very much, please enjoy the rest of your evening')

                else:
                    print('\nWaiter does not come back')
else:
    time.sleep(5)
    print('**Five minutes later**\n')
    print('**',drink,'has been brought over to the table')
    print('\nThe entrées for tonight are as follows')
    a='\noption a: spring rolls, deep fried roll skin wrapped with minched \nvegetables and clear noodles, served with a sweet sauce'
    b='\noption b: spicy beef salad, grilled sliced beef with red onions, \ntomatoes, mushroom, cilantro and roasted chilli lime dressing'
    c='\noption c: crying tiger, grilled marinated steak, sliced in thai \nstyle served with spicy house sauce and stiky rice on the side'
    d='\noption d: drunken noodles, stir-fried flat noodles with ground \nchichen, egg, onions, bell peppers, \nand basil in our hot and spicy house sauce'
    print(a,'\n',b,'\n',c,'\n',d)
    print('\nAre you ready to order?')
    ready=input()
    if ready == 'yes':
        print('\nWhat option would you care for this evening, would you care for a, b, c, or d?\n or would you care to hear the menu again?')
        print('a, b, c, or d?')
        option=input()
        time.sleep(5)
        print('\n**15 minutes later**')
        print('\nWaiter returns with','option ',option)
        time.sleep(5)
        print('\n**30 minutes later**')
        print('\n**Placing bill on table**')
        time.sleep(5)
        print('\n**collects payment**')
        time.sleep(5)
        print('\n**returns with receipt**')
        print('\nThank you very much, please enjoy the rest of your evening')
    else:
                print('\nI will be back in a few minutes')
                time.sleep(5)
                print(a,'\n',b,'\n',c,'\n',d)
                print('\nAre you ready?')
                ready=input()
                if ready == 'yes':
                    print('\nWhat option would you care for this evening, would you care for a, b, c, or d?\n or would you care to hear the menu again?')
                    print('a, b, c, or d?')
                    option=input()
                    time.sleep(5)
                    print('\n**15 minutes later**')
                    print('\nWaiter returns with','option ',option)
                    time.sleep(5)
                    print('\n**30 minutes later**')
                    print('\n**Placing bill on table**')
                    time.sleep(5)
                    print('\n**collects payment**')
                    time.sleep(5)
                    print('\n**returns with receipt**')
                    print('\nThank you very much, please enjoy the rest of your evening')

                else:
                    print('\nWaiter does not come back')
