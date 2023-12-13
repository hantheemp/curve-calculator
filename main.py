import pandas as pd

while True:
    try:

        file_path = input("Enter the .csv file's path:")

        df = pd.read_csv(file_path + ".csv")

        index = int(input("Enter the columns index for calculation with starting from 0 : "))

        df = df.iloc[:, index]

        totalPoints = 0

        count = 0

        for i in df:
            if (i != 0):
                totalPoints += int(i)
                count += 1

        result = totalPoints / count

        print(result)

        break

    except ValueError:

        print("Enter a valid value!")

    except FileNotFoundError:

        print("There is no file named " + file_path + " in the given directory!")  

