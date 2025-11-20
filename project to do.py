import tkinter as tk
from tkinter import messagebox
#########Function to add a task tp the lsit
def add_task():
    ######Get the text from the input box
    task=task_input.get()
    ######Check if the added task is valid
    if task!="":
        ######Add a task to the container at the end
        task_container.insert(tk.END,task)
        ######Clear the input field
        task_input.delete(0,tk.END)
    else:
        ######Display feedback to the user
        messagebox.showwarning("Error","Please enter a valid task.")
        ##### Function to delete the selected task.
        def delete_task():
            try:
        ######Get the list index of the selected task and remove it
                selected_task_position = task_container.curselection()
                task_container.delete(selected_task_position)
            except:
        ####Otherwise display the feedback to the user
                messagebox.showwarning("Deletion Error","Please de-select and re-select the task")
        ####Function to clear all added task.
        def clear_all_tasks():
            task_container.delete(0,tk.END)
        #####Setting up the main window
        window=tk.Tk()
        window.title("To-Do List Project")
        ####This element is used to capture the user input.
        task_input = tk.Entry(window.width=35)
        #####It is placed on the top left of the window,with
        #####Both vertical and horizontal spacing of 10
        task_input.grid(row=0,column=0,padx=10,pady=10)
        ####Button that will trigger a function to store the input
        add_button = tk.Button(window,text="Add Task", width=20, command=add_task)
        ######Placing the button next to the "Input field"
        add_button.grid(row=0,column=1,padx=10,pad=10)
        #####A container to display all the added tasks
        #####By setting the select mode to single we only allow
        #####One task to be selectedx at any given time
        task=container = tk.Listbox(window, height=10,width=40,selectmode=tk.SINGLE)
        #####Placing this container below the "Input field"and"Add button"
        task_container.grid(row=1,column=0,padx=10,pady=10)
        #####button that will trigger a function to clear the task list
        clear_button = tk.Button(window,text="Clear List",w i d t h =20,command=clear_all_tasks)
        #####placing the button below the "Task Container".
        clear_button.grid(row=2,column=0,padx=10,pady=10)
        #####Button that will trigger a function to delete the task.
        delete_button = tk.Button(window, text="Delete Task",
        w i d t h =20,command=delete_task)
        #####Placing the button next to the"Clear List" button.
        delete_button.grid(row=2,coulmn=1,padx=10,pady=10)
        ####staring the tkinters event loop
        window.mainloop()
        
        
        
        
