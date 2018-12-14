from final_plot import *


# def main():
#     print("Here are the commands you can order:")
#     print("--plot <year> (options: 2013, 2015, 2016, 2018.3, 2018.7)")
#     print("--plot all")
#     print("--exit")
#     print("--help")

#     user_input = input("Please give your order: ")

#     try:
#         year_input = user_input.split(" ")[1]
#         if year_input in ["2013", "2015", "2016", "2018.3", "2018.7"]:
#             	plot_shades_year('esteelauder_doublewear', year_input)
#             	main()

#         elif user_input.split(" ")[1] == 'all':
#             plot_shades('esteelauder_doublewear')
#             main()

#         else:
#             print("Invalid input, try again\n\n")
#             main()

#     except:
#         if user_input == "exit":
#             exit()

#         elif user_input == "help":
#             print("plot <year> (options: 2013, 2015, 2016, 2018.3, 2018.7): e.g. plot 2013, it will plot the shades published on 2013")
#             print(
#                 "plot all: it will plot the shades of each publish in the last five years")
#             print("exit: exit the program")
#             main()

#         else:
#             print("Invalid input, try again\n\n")
#             main()


def main():
    print("Here are the commands you can order:")
    print("--plot <year> (options: 2013, 2015, 2016, 2018.3, 2018.7)")
    print("--plot all")
    print("--exit")
    print("--help")

    user_input = input("Please give your order: ")

    while user_input != "exit":
        if user_input == 'plot all':
            plot_shades('esteelauder_doublewear')
        elif user_input == 'plot 2013':
            plot_shades_year('esteelauder_doublewear', "2013")
        elif user_input == 'plot 2015':
            plot_shades_year('esteelauder_doublewear', "2015")
        elif user_input == 'plot 2016':
            plot_shades_year('esteelauder_doublewear', "2016")
        elif user_input == 'plot 2018.3':
            plot_shades_year('esteelauder_doublewear', "2018.3")
        elif user_input == 'plot 2018.7':
            plot_shades_year('esteelauder_doublewear', "2018.7")
        elif user_input == 'help':
            print("plot <year> (options: 2013, 2015, 2016, 2018.3, 2018.7): e.g. plot 2013, it will plot the shades published on 2013")
            print("plot all: it will plot the shades of each publish in the last five years")
            print("exit: exit the program")
        else:
            print("Invalid input, try again")

        user_input = input("Please give your order: ")



main()
