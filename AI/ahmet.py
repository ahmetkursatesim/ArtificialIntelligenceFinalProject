import time;
import os;
import math;


class Report(object):
    count = 4000;
    users = [];

    def __init__(self, users_array, userindicator, food_report):
        self.report_id = Report.count
        Report.users = users_array
        self.userindicator = userindicator
        self.food_report = food_report
        Report.count += 1

    def printToFile(self):

        FoodReport = ""
        user = Report.users[self.userindicator]
        if user.gender == 'm':
            gender = "Male"
        else:
            gender = "Female"
        FoodReport += "\nREPORT" + "\n"
        FoodReport += "===========================================\n\n"
        FoodReport += "User Details\n"
        FoodReport += "===========================================\n"
        FoodReport += "Name           : " + user.customername + "\n"
        FoodReport += "Age            : " + str(user.age) + "\n"
        FoodReport += "Gender         : " + gender + "\n"
        FoodReport += "Height         : " + str(user.height) + "cm\n"
        FoodReport += "Weight         : " + str(user.weight) + "kg\n"
        FoodReport += "Weight Goal    : " + str(user.target_goal) + "kg\n"
        FoodReport += "Activity Level : " + str(user.levelactvity) + "\n\n"
        FoodReport += "Your BMI is " + str(
            "%.1f" % user.getBMI()) + " and your weight status is " + user.getBMIStatus() + "\n\n"
        FoodReport += "Calories Report\n"
        FoodReport += "===========================================\n"
        FoodReport += "Daily calories you need to maintain your current weight is " + str(
            "%d" % user.getDailyCalories()) + "\n"
        diff = user.getWeightDiff();
        d_cal_change = user.getCaloriesChange()
        if diff < 0:
            FoodReport += "Daily calories you need to lose weight (" + str("%.2f" % abs(diff)) + "kg/week) is " + str(
                "%d" % d_cal_change) + "\n"
        elif diff > 0:
            FoodReport += "Daily calories you need to gain weight (" + str("%.2f" % abs(diff)) + "kg/week) is " + str(
                "%d" % d_cal_change) + "\n"
        FoodReport += "\nSuggested meal\n"
        FoodReport += "===========================================\n"
        FoodReport += self.food_report + "\n"

        file_path = "reports.txt"
        file = open(file_path, "a")
        file.write(FoodReport);

        file_path = "user_reports/" + user.customername.replace(" ", "_") + "_diet_report.txt";
        file = open(file_path, "w")
        file.write(FoodReport)
        print("Full diet report successfully generated. Please check folder 'user_reports'.\n")


class User(object):
    count = 1000;

    def __init__(self, user_name, age, gender, height, weight, weight_goal, levelactvity):
        self.user_id = User.count
        self.customername = user_name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.target_goal = weight_goal
        self.levelactvity = levelactvity
        User.count += 1

    def printUserDetails(self):
        if self.gender == 'm':
            gender = "Male"
        else:
            gender = "Female"
        print( "Name: " + self.customername + "\n""Age            : " + str(self.age) + "\n""Gender         : " + gender + "\n""Height : " + str(self.height) + "cm\n"
               "WeightTube : " + str(self.weight) + "kg\n" "Weight Goal    : " + str(self.target_goal) + "kg\n""Activity Level : " + str(self.levelactvity) + "\n")

    def getBMI(self):

        height = self.height / 100
        return self.weight / (height * height)

    def getBMR(self):

        if self.gender == 'm':
            return math.ceil(66 + (13.7 * self.weight) + (5.0 * self.height) - (6.8 * self.age));
        elif self.gender == 'f':
            return math.ceil(655 + (9.6 * self.weight) + (1.8 * self.height) - (4.7 * self.age));
        else:
            return 0

    def getDailyCalories(self):
        bmr = self.getBMR()
        if self.levelactvity == 1:
            return math.ceil(bmr * 1.2)
        elif self.levelactvity == 2:
            return math.ceil(bmr * 1.375)
        elif self.levelactvity == 3:
            return math.ceil(bmr * 1.55)
        elif self.levelactvity == 4:
            return math.ceil(bmr * 1.725)
        elif self.levelactvity == 5:
            return math.ceil(bmr * 1.9)
        else:
            return 0

    def getBMIStatus(self):
        bodymi = self.getBMI()

        if bodymi < 18.5:
            return "Underweight"
        elif bodymi >= 18.5 and bodymi < 25.0:
            return "Normal"
        elif bodymi >= 25.0 and bodymi < 30.0:
            return "Overweight"
        else:
            return "Obese"

    def getCaloriesChange(self):

        w_diff = self.getWeightDiff()
        c_diff = w_diff * 1000
        d_calories = self.getDailyCalories()
        return d_calories + c_diff

    def getWeightDiff(self):
        return self.target_goal - self.weight


class Food(object):
    count = 5000

    def __init__(self, food_type, name, amount, calories):
        self.food_id = Food.count
        self.food_type = food_type
        self.name = name
        self.amount = amount
        self.calories = calories
        Food.count += 1


def main():
    print("\n""<---------------------------------->\n""                                  \n""Welcome to Smart Diet System   \n""                                  \n"
          "<------------------------------------>\n"
          "      'If you want to healhty body '      \n");

    print("Loading apps...")
    time.sleep(0.5);
    LoadingApps()


def LoadingApps():
    Customername = input("\nHello there. What is your name ? : ")
    calculate = input(
        "Hi " + Customername + ",\nTo calculate your daily calories ?  y/n ");
    if calculate.lower() == 'y':
        calinput = True;
        while (calinput):
            Customerage = input("Your age: ")
            if Customerage.isdigit():
                Customerage = int(Customerage)
                break
            else:
                print("\n>> Invalid input\n")
        while (calinput):
            Customergender = input("Your gender (m or f): ")
            if Customergender == 'f' or Customergender == 'm':
                break
            else:
                print("\n>> Invalid input\n")
        while (calinput):
            Customerheight = input("Your height? ")
            if Customerheight.replace(".", "").isdigit():
                Customerheight = float(Customerheight);
                break;
            else:
                print("\n>> Invalid input\n")
        while (calinput):
            Customerweight = input("Your weight: ")
            if Customerweight.replace(".", "").isdigit():
                Customerweight = float(Customerweight);
                break;
            else:
                print("\n>> Invalid input\n");
        while (calinput):
            target_goal = input \
                ("Your weight goal after a week Enter your target weight: ")
            if target_goal.replace(".", "").isdigit():
                target_goal = float(target_goal)
                if abs(target_goal - Customerweight) > 0.91:
                    print("\n>> out of range weight goal (max:+0.91kg  min -0.91kg )\n")
                else:
                    break;
            else:
                print("\n>> Invalid input\n")
        while (calinput):
            levelact = int(input("\nYour activity level:\n" +
                                 "* - Sedentary \n" +
                                 "** - Lightly active \n" +
                                 "***- Moderately active (\n" +
                                 "**** - Very active \n"
                                 "***** - Extra active\n"))
            if levelact >= 1 and levelact <= 5:
                break;
            else:
                print("\n>> Invalid input")

        customers.append(User(Customername, Customerage, Customergender.lower(), Customerheight, Customerweight, target_goal,levelact))
        indicator_users = len(customers) - 1

        print("Generate  Report\n")
        time.sleep(0.8)

        print("User Information \n""<------------------------------------->")

        customers[indicator_users].printUserDetails()

        print("Your BMI :: " + str("%.1f" % customers[indicator_users].getBMI()) + "  weight status ::" + customers
        [indicator_users].getBMIStatus() + "\n\n"" Report  Calories\n""<--------------------------------------->");

        d_calories = customers[indicator_users].getDailyCalories()
        print("need to maintain current weight is " + str("%d" % d_calories));

        weight_differences = customers[indicator_users].getWeightDiff()
        d_cal_change = customers[indicator_users].getCaloriesChange()
        if weight_differences < 0:

            print("Need to lose weight (" + str("%.3f" % abs(weight_differences)) + "kg/week) is " + str("%d" % d_cal_change))
        elif weight_differences > 0:

            print("Need to gain weight (" + str("%.3f" % abs(weight_differences)) + "kg/week) is " + str("%d" % d_cal_change))

        calories_Foods = d_cal_change / 3
        food_report = getRecommendedFood(calories_Foods)

        print("\n" "decide Food\n""<---------------------------------->\n" +food_report)



        r = Report(customers, indicator_users, food_report);
        r.printToFile()

    decision = input("Thank you\nStart over? y/n ")
    if decision.lower() == 'y':
        main()
    else:
        print("Exitting")
        time.sleep(0.5)
        return 0


def getRecommendedFood(cal):
    T_Food = ""


    m_Differences = 9999999
    for i in range(0, len(breakfast)):
        totalCal = 0
        for j in range(0, len(breakfast[i])):
            if (i == 0 and j == 0) or breakfast[i][j]:
                totalCal += float(foods[breakfast[i][j]].calories)
        if abs(totalCal - cal) < m_Differences:
            m_Differences = abs(totalCal - cal)
            breakfastset = i
            breakfastsetCal = totalCal

    T_Food += "Breakfast:\n"
    for j in range(0, len(breakfast[breakfastset])):
        T_Food += "\n"
        if (breakfastset == 0 and j == 0) or breakfast[breakfastset][j]:
            T_Food += "  Food Name " + str(j + 1) + "  : " + foods[breakfast[breakfastset][j]].name + "\n"
            T_Food += "  Amount       : " + foods[breakfast[breakfastset][j]].amount + "\n"
            T_Food += "  Calories     : " + foods[breakfast[breakfastset][j]].calories + "\n"
    T_Food += "  Total of Breakfast Calories : " + str("%.2f" % (breakfastsetCal)) + "\n\n"


    m_Differences = 9999999;
    for i in range(0, len(lunch)):
        totalCal = 0;
        for j in range(0, len(lunch[i])):
            if (i == 0 and j == 0) or lunch[i][j]:
                totalCal += float(foods[lunch[i][j]].calories)
        if abs(totalCal - cal) < m_Differences:
            m_Differences = abs(totalCal - cal)
            lunchset = i
            lunchsetcal = totalCal

    T_Food += "Lunch:\n";
    for j in range(0, len(lunch[lunchset])):
        T_Food += "\n"
        if (lunchset == 0 and j == 0) or lunch[lunchset][j]:
            T_Food += "  Food Name " + str(j + 1) + "  : " + foods[lunch[lunchset][j]].name + "\n"
            T_Food += "  Amount       : " + foods[lunch[lunchset][j]].amount + "\n"
            T_Food += "  Calories     : " + foods[lunch[lunchset][j]].calories + "\n"
    T_Food += "  Total of  Lunch Calories : " + str("%.1f" % (lunchsetcal)) + "\n\n"


    m_Differences = 9999999;
    for i in range(0, len(dinner)):
        totalCal = 0
        for j in range(0, len(dinner[i])):
            if (i == 0 and j == 0) or dinner[i][j]:
                totalCal += float(foods[dinner[i][j]].calories)
        if abs(totalCal - cal) < m_Differences:
            m_Differences = abs(totalCal - cal)
            dinnerset = i
            dinnersetcal = totalCal

    T_Food += "Dinner:\n";
    for j in range(0, len(dinner[dinnerset])):
        T_Food += "\n"
        if (dinnerset == 0 and j == 0) or dinner[dinnerset][j]:
            T_Food += "  Food Name " + str(j + 1) + "  : " + foods[dinner[dinnerset][j]].name + "\n"
            T_Food += "  Amount       : " + foods[dinner[dinnerset][j]].amount + "\n"
            T_Food += "  Calories     : " + foods[dinner[dinnerset][j]].calories + "\n"
    T_Food += "  Total of Dinner Calories : " + str("%.1f" % (dinnersetcal)) + "\n"
    totalMealCal = math.ceil(breakfastsetCal + lunchsetcal + dinnersetcal)
    T_Food += "=============================\n"
    T_Food += "Total of Calories : " + str(totalMealCal) + "\n"
    T_Food += "============================="
    return T_Food


customers= []
foods = []
breakfast = [[0 for a in range(3)] for b in range(8)]
lunch = [[0 for a in range(3)] for b in range(8)]
dinner = [[0 for a in range(3)] for b in range(8)]

reports_file_path = "reports.txt"
foods_file_path = "foods.txt"

if not os.path.exists(reports_file_path):
    print("File '" + reports_file_path + "' not exists")

if not os.path.exists(foods_file_path):
    print("File '" + foods_file_path + "' not exists")
else:
    fileFood = open(foods_file_path, "r")
    linesFood = fileFood.read().splitlines()
    count = 0
    breakfastcal = 0
    launchcal = 0
    dinnercal = 0
    for y in range(0, int(len(linesFood) / 5)):
        y *= 5;

        foods.append(Food(linesFood[y], linesFood[y + 1], linesFood[y + 2], linesFood[y + 3]))

        lastCharacter = foods[count].food_type[len(foods[count].food_type) - 1]
        if y / 5 == int(len(linesFood) / 5) - 1:
            n_last_character = "9"
        else:
            n_last_character = linesFood[y + 5][len(linesFood[y + 5]) - 1]

        if "breakfast" in foods[count].food_type:
            breakfast[int(lastCharacter) - 1][breakfastcal] = count
            if int(n_last_character) > int(lastCharacter):
                breakfastcal = 0
            else:
                breakfastcal += 1
        elif "lunch" in foods[count].food_type:
            lunch[int(lastCharacter) - 1][launchcal] = count
            if int(n_last_character) > int(lastCharacter):
                launchcal = 0
            else:
                launchcal += 1
        else:
            dinner[int(lastCharacter) - 1][dinnercal] = count
            if int(n_last_character) > int(lastCharacter):
                dinnercal = 0
            else:
                dinnercal += 1
        count += 1

main()
