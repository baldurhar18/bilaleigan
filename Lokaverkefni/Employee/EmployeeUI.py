def front_Page():
    chocie = ''
    while chocie != 'q':
        print('{0:40}{1}'.format('Bílaleigan', 'Front page'))
        print('-'*50)
        print("{0:>26}".format('Hello'))
        print("Press - 1 for Cars \nPress - 2 for Customers \nPress q to Quit ")
        print('-'*50)
        print('{0:>18}{1:>18}'.format('Cars', 'Customers'))
        chocie = input("")


front_Page()
