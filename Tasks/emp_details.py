import json

while True:
    try:
        emp_data = [{"first_name": input("enter your first name : "),
                     "last_name": input("enter your last name : "),
                     "employe_id": "A2022:001",
                     "city": input("enter the city : "),
                     "experience": int(input("enter the experience in months : ")),
                     "ctc": int(input("enter your ctc : ")),
                     "age": int(input("enter the age : ")),
                     "contact_no": int(input("enter the contact number : "))
                     }]

        def write_json(emp_data,filename="sushmith.json"):

            with open(filename, "w") as f:
                    json.dump(emp_data, f,indent=4)

        write_json(emp_data)
        break

    except:
            print("check the input detail datatype and enter the correct datatype data")

# Choices function for user to select add
def Choices():

    print("manage employee system")
    print("add - add the new employee detail")
    print("exit  - exit from the process")

# filename
filename = "sushmith.json"

while True:

    # open the json file and store the datas in data variable
    with open(filename, "r") as file:
        data = json.load(file)

    # to get the last employee id in a list
    listemp = [int(data[-1]['employe_id'][6:])]

    Choices()
    # user need to select the option
    Choice = input("\nSelect a option\n: ")
    # add a new data to json file
    if Choice == "add":

        # to create a new employee id for new user
        emp_id = listemp[-1] + 1
        listemp.append("A2022" + ":" +str(emp_id))
        try:
            # getting all the input data from the user for new employee to add in json file
            emp_data = {"first_name": input("enter your first name : "),
                         "last_name": input("enter your last name : "),
                         "employe_id": listemp[-1],
                         "city": input("enter the city : "),
                         "experience": int(input("enter the experience : ")),
                         "ctc": int(input("enter your ctc : ")),
                         "age": int(input("enter the age : ")),
                         "contact_no": int(input("enter the contact number : "))
                         }

            # open the file and read the data and store in data variable
            with open(filename, "r") as file:
                data = json.load(file)

            # append the new employee data to data variable
            data.append(emp_data)

            # data variable had some datas , write the data to json file
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)

            print("new employee details added")
        except :
            print("check the input detail datatype and enter the correct datatype data")
        else:
            print("emp_id is not found.")

    elif Choice == "exit":
        break
