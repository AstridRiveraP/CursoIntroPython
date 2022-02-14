import errno


def main():
    try:
        configuration = open("config.txt")
    except OSError as err:
        # except FileNotFoundError:

        if err.errno==2:
            print("Couldn't find the config.txt file!")
        # except PermissionError:

        elif err.errno==13:
            print("Found config.txt but couldn't read it")



if __name__=='__main__':
    main()