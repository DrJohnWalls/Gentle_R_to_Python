
import time
import argparse

def fizzbuzzboom(input_value, secret_key=524):
    """
    The fizzbuzzboom function takes numeric inputs and provides a result.
    """

    #Value Checking
    try:
        x = int(input_value)
        pass
    except ValueError:
        #Handle the exception
        print ("Please enter an integer")
        return

    if x == secret_key:
        delay = 0.5
        print("You have entered the self destruct code...")
        time.sleep(delay)
        print("All your files will be erased...")
        time.sleep(delay)
        print("You have 5 seconds to abort...")
        t = 5+1
        time.sleep(delay)
        while t > 1:
            t = t-1
            print(t)
            time.sleep(delay*2);
        print("[*] BOOM")
    elif x % 5==0 and x % 3==0:
        print("fizzbuzz")
    elif x % 5==0:
        print("buzz")
    elif x % 3==0:
        print("fizz")
    else:
        print(x)


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("number", default=15, type=float, help="submit an integer or float to fizzbuzzboom")
    parser.add_argument("-k", "--key", default=524, type=float, help="secret key to intitialize self destruct sequence")
    args = parser.parse_args()

    print("[*] Calculating the result...")
    fizzbuzzboom(args.number, args.key)
