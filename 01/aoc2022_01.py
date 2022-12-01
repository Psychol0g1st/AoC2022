def max_calory(calories):
    print("The maximum caloris: ", max(calories))

def top_3_calories_sum(calories):
    top3 = sorted(calories)[-3:]
    print("The sum of top 3 calory: " + str(sum(top3)))



def main():
    with open('input.txt') as file:
        lines = file.read()
        calories = [0]
        index = 0
        for s in lines.split('\n'):
            if s != '':
                calory = int(s)
                calories[index] += calory
            else:
                index += 1
                calories.append(0)
        print(calories)
    ####################################
    max_calory(calories)
    top_3_calories_sum(calories)

if(__name__ == "__main__"):
    main()