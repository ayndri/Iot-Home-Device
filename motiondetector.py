from gpio import *
from time import *

def main():
	pinMode(0, IN)
	pinMode(1, OUT)
	pinMode(2, OUT)
	pinMode(3, OUT)
	
	while True:
		value = digitalRead(0)
		if value == 1023:
			customWrite(1, 2)
			customWrite(2, 1)
			customWrite(3, 1)
		else:
			customWrite(1, 0)
			customWrite(2, 0)
			customWrite(3, 0)
		delay(100)

if __name__ == "__main__":
	main()