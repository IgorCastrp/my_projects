import time, sys
indent = 0
indent_increasing = True

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1)  # Pause for 1/10 of a second.

        if indent_increasing:
            indent += 1
            if indent == 30:
                indent -= 1
                indent_increasing = False
        else:
            indent -= 1
            if indent == 0:
                indent += 1
                indent_increasing = True
except KeyboardInterrupt:
    sys.exit()