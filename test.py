import sys
import tty
import termios

def read_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
        if ch == '\r':
            print("Carriage Return (CR): ASCII 13")
        elif ch == '\n':
            print("Line Feed (LF): ASCII 10")
        else:
            print(f"Other Key Pressed: {ord(ch)}")
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

if __name__ == "__main__":
    print("Press Enter key:")
    read_key()
