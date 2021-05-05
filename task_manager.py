#The function to display statistics.
def display_statistics():
    #read the task overview file 
    f=open('task_overview.txt',  'r')
    all_lines = f.readlines()
    #display all the lines in the file 
    for line in all_lines:
        print(line)
    f.close()
    #read the user overview file 
    f=open('user_overview.txt',  'r')
    all_lines = f.readlines()
    
    #display all the lines from the file 
    for line in all_lines:
        print(line)
    f.close()
    
#The function to register a user.
def reg_user():
    login = False
    global files_name
    global files_pass
    username =True
    user = open('user.txt', 'a+')
    #while there is no username yet..
    while username:
        #get the new username from user 
        new_user = input("\nPLease enter a new name: ")
        #if the username exists, display message
        if new_user == files_name:
            print("Username already exists, Please try another Username. ")
        else:
            break

    #else, continue and confirm new user and password
    new_password = input("\nPLease enter a new password: ")
    con_new_user = input("\nPlease confirm your new name: ")
    con_new_password = input("\nPLease confrim your new password: ")
    if new_user == con_new_user and new_password == con_new_password:
        print("New user has been registered!")
        user.write("\n" + new_user + ", " + new_password)
        login == True
        user.close()

#To get todays date
import datetime        
now = datetime.datetime.today()

#The function to add tasks.
def add_task():
    with open('tasks.txt', 'a') as f:
        #now variable stores todays date/time
        import datetime
        now = datetime.datetime.today()
        #confirm details about the new task.
        assigned_user = input("Assigned to: ")
        task_title = input("Task title: ")
        task_description = input("Task Description: ")
        due_date = input("Due date: ")
        date_assigned = str(now.date())
        global task_complete
        task_complete = "No"
        print("Date assigned: ", now.date())
        print("Task Complete: ", task_complete)
        print("Task successfully added. ")
        #add the task to the task.txt(f) file.
        f.write('\n')
        f.write(assigned_user + "," + task_title + "," + task_description + "," + date_assigned + "," + due_date + "," + task_complete)
#The function to view all tasks.
def view_all():
    #read tasks.txt file
    with open('tasks.txt', 'r') as f:
        #variable stores all the lines in the file
        all_tasks = f.readlines()
        #for each line in the file
        #Display the tasks, in a user friendly way
        for line in all_tasks:
            strings = line.split(",")
            print("\nTask: {}".format(strings[1]))
            print("\nAssigned to: {}".format(strings[0]))
            print("\nDate Assigned: {}".format(strings[3]))
            print("\nDue Date: {}".format(strings[4]))
            print("\nTask complete: {}".format(strings[5]))
            print("\nTask Description: {}".format(strings[2]))
            
#The function to view my tasks(the user).
def view_mine():
    #read tasks.txt file
    with open('tasks.txt', 'r') as f:
        #variable stores all the lines in the file
        all_tasks = f.readlines()
        #for a = task/line number
        #j = the line/task 
        for a, j in enumerate(all_tasks):
            new_list = list(enumerate(all_tasks))
            the_line = j.split(",")
            #Display the lines/tasks.
            print("Task number :", a)
            print("\nTask: {}".format(the_line[1]))
            print("\nAssigned to: {}".format(the_line[0]))
            print("\nDate Assigned: {}".format(the_line[3]))
            print("\nDue Date: {}".format(the_line[4]))
            print("\nTask complete: {}".format(the_line[5]))
            print("\nTask Description: {}".format(the_line[2]))
            print()
        #user_wants, stores the users choice/number.
        user_wants = int(input("Enter the task number you would like to edit or Enter -1 to return to the main menu: "))
        #if users choice is -1 
        if user_wants == -1:
            #Display a menu for the admin user.
            menu = input("""Please select one of the following options:
r - register user
a - add task
va - view all tasks
vm - view my task
gr - generate reports
ds - display statistics
e - exit                 """)
            #from the menu the user may decide what must be done next,
            #call the functions, according to the users choice.
            if menu == "r":
                reg_user()
            if menu == "a":
                add_task()
            if menu == "va":
                view_all()
            if menu == "vm":
                view_mine()
            if menu == "gr":
                tasks_overview()
                user_overview()
                print("Tasks and users overview generated.")
            if menu == "ds":
                display_statistics()
            if menu == "e":
                print("Thank you! ")
        else:
            #else edit the task, according to which task number the user picks
            for task_to_edit in all_tasks:
                #task to edit holds the chosen task, to be edited..
                task_to_edit = all_tasks[user_wants].split(",")
            while True:
                #if the chosen task is Not complete yet..
                if task_to_edit[5].split() == "No":
                    #Display menu to allow the user to edit the task accordingly
                    print("""
Please select how you would like to edit the task(by letter):
- Mark as complete(c)
- Edit the task(e)
                          """)
                    #variable holds the users choice
                    edit = input("-")
                    #if the user chooses "d", the user may change the due date
                    if edit == "d":
                        change_date = input("New due date: ")
                        print("Due Date changed.")
                        task_to_edit[4] = change_date
                    #if the user chooses "u", the user may change the username assigned to that task.
                    elif edit == "u":
                        change_username = input("New assigned user: ")
                        print("New user assigned. ")
                        task_to_edit[0] = change_username
                #else if the task is already complete, display message
                if task_to_edit[5].split() == "Yes":
                    print("Task already complete.")
                    break
            #re-write the task, accordingly(as a new task) 
            all_tasks[user_wants] = task_to_edit
            var_1 = task_to_edit[0]
            var_2 = task_to_edit[1]
            var_3 = task_to_edit[2]
            var_4 = task_to_edit[3]
            var_5 = task_to_edit[4]
            var_6 = task_to_edit[5]
            new_task = ("{},{},{},{},{},{}".format(var_1, var_2, var_3, var_4, var_5, var_6))
            all_tasks[user_wants] = new_task
            #re-write the task to the file
            f=open('tasks.txt', 'a+')
            f.write(str(all_tasks))
            f.close()

#The function to generate the tasks overview.
def tasks_overview():
    #write the task_overview.txt file
    file=open('task_overview.txt', 'w')
    #to get todays date and time
    import datetime
    now = datetime.datetime.today()
    #read the tasks.txt file 
    with open('tasks.txt', 'r') as f:
        #variables stores all the lines in the file 
        all_tasks = f.readlines()
        count = 0
        complete = 0
        incomplete = 0
        overdue = 0
        #for each line in the file, add 1(count)
        for line in all_tasks:
            count += 1
        #split the line into words, at each comma ","
        strings = line.split(",")
        #write the total lines(tasks) to the task overview file 
        total_tasks = ("Total Tasks: {}".format(count))
        file.write(str(total_tasks))
        #for each line(task), if it is complete
        for line in all_tasks:
            #add 1, to the variable 'complete'
            if strings[5].strip() == "Yes":
                complete += 1
        #write the total completed tasks to the task overview file
        total_completed_tasks = ("\nTotal completed tasks: {}".format(complete))
        file.write(str(total_completed_tasks))
        
        #if the task is incomplete, add 1 to the variable 'incomplete'
        for line in all_tasks:
            if strings[5].strip() == "No":
                incomplete += 1
        #write the total incompleted tasks to the task overview file 
        total_incompleted_tasks = ("\nTotal incompleted tasks: {}".format(incomplete))
        file.write(str(total_incompleted_tasks))
        #for each line, split it into 'words'
        for line in all_tasks:
            line = line.rstrip()
            words = line.split(",")
            #variable stores the tasks date from the tasks.txt file, then if it is 'overdue' - add 1.
            users_due_date = datetime.datetime.strptime(words[4].strip(), '%d %b %Y')
            if now > users_due_date:
                overdue = overdue + 1
        #write the total amount of overdue tasks to the task overview file.
        total_tasks_overdue = ("\nTotal tasks overdue: {}".format(overdue))
        file.write(str(total_tasks_overdue))
        #variables holding, the percentage incompleted and percentage overdue
        perc_incomplete = incomplete * 100/len(all_tasks)
        perc_overdue = overdue * 100/len(all_tasks)
        perc_incomplete = int(perc_incomplete)
        perc_overdue = int(perc_overdue)
        #write the percentages to the task overview file
        percentage_tasks_incomplete = ("\nPercentage of tasks incomplete: {} %".format(perc_incomplete))
        percentage_tasks_overdue = ("\nPercentage of tasks overdue: {} %".format(perc_overdue))
        file.write(str(percentage_tasks_incomplete))
        file.write(str(percentage_tasks_overdue))
        file.close()
        
#The function to generate the user overview.
def user_overview():
    #write the user overview file
    ufile=open('user_overview.txt', 'w')
    userscount = 0
    users_tasks = 0
    overdue = 0
    #read the user.txt file 
    with open ('user.txt', 'r') as user_file:
        #for each line count the users(line)
        for users in user_file:
            userscount=userscount + 1
        #write the total users that are registered to the user overview file 
        total_users_registered = ("Total Users Registered: {}".format(userscount))
        ufile.write(str(total_users_registered))    
    count2 = 0
    user_complete = 0
    user_incomplete = 0
    users_count = 0
    #read the tasks.txt file 
    with open('tasks.txt', 'r') as f:
        #variable holding the lines of the tasks.txt file 
        all_tasks = f.readlines()
        #count each line of the tasks.txt file 
        for line in all_tasks:
            count2 += 1
        #write the total tasks generated and tracked to the user overview file 
        total_tasks_g_t = ("\nTotal Tasks generated and tracked: {}".format(count2))
        ufile.write(str(total_tasks_g_t))
    #for each user(line), count users  
    for i in all_tasks:
        users_count= users_count + 1
        #an empty dictionary, to be used  
        di = dict()
    #split each line in the file at the comma into 'words'
    for line in all_tasks:
        line = line.rstrip()
        words = line.split(",")
        #to get just the username of that task
        words = words[0]
        #add the usernames to the dictionary with a value to it.
        di[words] = di.get(words,0) + 1
    #write the total tasks assigned to a user heading 
    tt_assigned_to_user =("\nTotal tasks assigned to user: ".format())
    ufile.write(str(tt_assigned_to_user))
    #for the key(name) and value(number) in the dictionary 'di' 
    for k,v in di.items():
        #write the number of tasks assigned to each user, to the user overview file  
        k_v = ("\n {}-{}".format(k, v))
        ufile.write(str(k_v))
    #write the percentage of tasks assigned to user heading     
    perc_tot_as_user = ("\nPercentage of total number of tasks assigned to user: ".format())
    ufile.write(str(perc_tot_as_user))
    #for the key and value,
    #the percentage = the amount of tasks assigned to that user*100/ divide by the amount of tasks overall
    for k,v in di.items():
        perc = v*100/users_count
        #write the percenatge assigned to each user, to the user overview file 
        k_perc = ("\n {} - {} %".format(k, perc))
        ufile.write(str(k_perc))
    #read the tasks.txt file 
    f = open('tasks.txt', 'r') 
    all_tasks = f.readlines()
    di = dict()
    user_complete = 0
    user_incomplete = 0
    users_tasks = 0
    users_count = 0
    #count the number of users 
    for i in all_tasks:
        users_count= users_count + 1
    #split and add users to the dictionary 
    for line in all_tasks:
        line = line.rstrip()
        words = line.split(",")
        words = words[0]
        di[words] = di.get(words,0) + 1
    #for each line, split into words = string 
    for line in all_tasks:
        strings = line.split(",")
        #if the user is in that line again, +1
        if strings[0] == strings[0] in line:
            users_tasks = users_tasks + 1
    #if the task is complete, add 1 to the variable 'user_complete'        
    for line in all_tasks:
        if strings[5].strip() == "Yes":
            user_complete = user_complete + 1
        #if the task is not complete add 1 to the variable 'user_incomplete'
        if strings[5].strip() == "No":
            user_incomplete = user_incomplete + 1
    #get the percentages of the users complete and incomplete tasks
    perc_complete = user_complete * 100/users_tasks
    perc_complete = int(perc_complete)
    perc_incomplete = user_incomplete * 100/users_tasks
    perc_incomplete = int(perc_incomplete)
    
    #write the percentages to the user overview file 
    percentage_of_completed_tasks = ("\nPercentage of completed tasks by ".format())
    ufile.write(str(percentage_of_completed_tasks))
    #for each key, write the percentage of that users complete tasks, to the user overview file 
    for k,v in di.items():
        k_perc = ("\n {} - {} %".format(k, str(perc_complete)))
        ufile.write(str(k_perc))
    #for each key, write the percentage of that users incomplete tasks, to the user overview file    
    percentage_incompleted_tasks = ("\nPercentage of incompleted tasks by ".format())
    ufile.write(str(percentage_incompleted_tasks))
    for k,v in di.items():
        k_perc_inc = ("\n {} - {} %").format(k, str(perc_incomplete))
        ufile.write(str(k_perc_inc))
        
    #get the due date of each users tasks, if it is 'overdue' +1
    if strings[0] in line:
        users_due_date = datetime.datetime.strptime(strings[4].strip(), '%d %b %Y')
        if users_due_date < now:
            overdue + 1
    #write the total amount of tasks to the user overview file 
    total_tasks_overdue = ("\nTotal tasks overdue: {}".format(overdue))
    ufile.write(str(total_tasks_overdue))
    for k,v in di.items():
        k_overdue = ("\n {} - {}".format(k, overdue))
        ufile.write(str(k_overdue))
    #calculating the percentages of the users incomplete and overdue tasks
    user_perc_incomplete = user_incomplete * 100/users_tasks
    user_perc_overdue = overdue * 100/users_tasks
    user_perc_incomplete = int(user_perc_incomplete)
    user_perc_overdue = int(user_perc_overdue)
    
    #write the percentages to the user overview file 
    percentage_of_tasks_incomplete = ("\nPercentage of tasks incomplete: {} %".format(str(user_perc_incomplete)))
    ufile.write(str(percentage_of_tasks_incomplete))
    percenatge_of_tasks_overdue = ("\nPercenatge of tasks overdue: {} %".format(str(user_perc_incomplete)))
    ufile.write(str(percenatge_of_tasks_overdue))
    ufile.close()
#after defining all functions that will be used..
#open the files 
user = open('user.txt', 'r+')
tasks = open('tasks.txt', 'r+') 
#variable to check whether the user logged in successfully 
login = False
global menu
task_complete = "No"
#while the login has not yet been done(successfully)
#two variables which will store the username and password that has been enterd by the user 
while login == False:
    name = str(input("Enter your username: "))
    password = str(input("Enter your password: "))
    
    #for each line in the 'user.txt' file
    for line in user:
        files_name,files_pass = line.split(', ')                               #the name and password in the user.txt file is declared when splitting the line at the comma
        files_pass = files_pass.strip()
        #if the name&password in the file are the same as the name&password entered by the user, Then login is successful.
        if name == files_name and password == files_pass:               
            login = True

    #if the opposite occurs and login is unsuccessful, message is displayed
    if login == False:
        print("You have entered an Incorrect username or password, Please Try again.")
    user.seek(0)
user.close()
#Display a menu for the admin user.
if name == "admin":
    print("Please select one of the following options:")
    print("r - register user" )
    print("a - add task")
    print("va - view all tasks")
    print("vm - view my task")
    print("gr - generate reports")
    print("ds - display statistics")
    print("e - exit")
    #Display a menu for a user thats not admin.
else:
    print("Please select one of the following options:")
    print("r - register user" )
    print("a - add task")
    print("va - view all tasks")
    print("vm - view my task")
    print("e - exit")
#variable stores users choice.
task1 = input("please select a option: ")

#if the 'd' is entered(Display statistics)
if task1 == "ds":
    #check if the 'admin' user is logged in
    if name == "admin":
        login = False
    #if admin is logged in..
    if login == False:
        #Display all statistics to user 
        tasks_overview()
        user_overview()
        display_statistics()

#If the 'r' is entered(register user)
if task1 == "r":
    #check if the 'admin' user is logged in
    if name == "admin":
        login = False
    #if admin is logged in..
    if login == False:
        reg_user()
    if login == True:
        print("User not allowed to register new user.")

#if user wants to add task
if task1 == "a":
    add_task()

#If the user wants to view all the tasks
if task1 == "va":
    view_all()

#if the user wants to view 'my tasks'.
if task1 == "vm":
    view_mine()

if task1 == "gr":
    tasks_overview()
    user_overview()
    print("Tasks and users overview generated.")

#if the user wants to exit,Diplay message 
if task1 == "e":
    print("Thank you! ")

#Close the user.txt file                        
user.close()
        
