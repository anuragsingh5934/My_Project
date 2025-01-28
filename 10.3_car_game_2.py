command = ''
started = ''
while True:

    command = input('>' ).lower()

    if command == 'start':
     if started:
          print("already started")
     else:
       print("Your car has been started successfully")
     started = True

         

    elif command == 'stop':
     if not started:
          print("already stopped")
     else:
         print("car stopped")
     started = False


    elif command == 'help':
         print("""
start - to start car
stop - to stop car
quit - exit from game """)
         

    elif command == 'quit':
     print("thank you for visiting")
     break
    
    else:
         print("This is not valid key.")