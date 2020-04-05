import math

#single
def stimulusPackage(income):

    if income <= 75099:
        return 1200

    elif income >= 99000:
        return 0

    else:   #75099 < income < 99000
        subtract = income - 75099
        division = math.floor(subtract / 100)
        output = 1195 - (division * 5)
        return output

#married
def marriedStimulus(coupleincome, n):  # 'n' is for number of kids you have

  if (coupleincome <= 150000):
      child = 500 * n
      return 2400 + child

  elif (coupleincome >= 198000):
    return 0

  else:   # 150000 < income < 198000
      subtract = coupleincome - 150000
      division = math.floor(subtract / 100)
      child = 500 * n
      output = 2395 - (division * 5) + child

      return output


def main():

    print("\nWelcome to the CV-19 Stimulus Calculator\n")
    print("This is a tool to help you determine how much stimulus money you will be receiving.\n")

    marital_status = input("Are you single or married?: ")

    while True:

        if (marital_status == "single"):
            answer = int(input("Please enter your income: "))
            print("You will receive a payment of $" + str(stimulusPackage(answer)))
            break

        elif (marital_status == "married"):
            answer = int(input("Please enter your joint income: "))
            children = int(input("Please enter how many children you have: "))
            print("You will receive a payment of $" + str(marriedStimulus(answer, children)))
            break

        else:
            print("Invalid value entered. Please try again.")
            marital_status = input("Are you single or married?: ")

main()
