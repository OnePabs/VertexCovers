########################################################
# to run:
# 1. activate conda environment 
# 2. cd to the src folder
# 3. run "python3 -m experiments.gui_experiment_approx"
########################################################


import tkinter as tk
from tkinter import messagebox
from experiments.general_experiment_approx import general_experiment_approx

# Set up the window
root = tk.Tk()
root.title("Simple Data Form")
root.geometry("900x600")

def submit_form():
    data_folder_path = data_folder_path_entry.get()
    results_folder_path = results_folder_path_entry.get()
    algorithm_name = algorithm_name_entry.get()
    if data_folder_path and results_folder_path and algorithm_name:
        general_experiment_approx(data_folder_path,results_folder_path,algorithm_name)
        messagebox.showinfo("Success", "End")

        # GUI delete data in user entry boxes
        # data_folder_path_entry.delete(0, tk.END)
        # results_folder_path_entry.delete(0, tk.END)
        # algorithm_name_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Fill all fields")

# Labels and Entry fields
tk.Label(root, text="data folder path:").pack(pady=(10,0))
data_folder_path_entry = tk.Entry(root)
data_folder_path_entry.pack()

tk.Label(root, text="results folder path:").pack(pady=(10,0))
results_folder_path_entry = tk.Entry(root)
results_folder_path_entry.pack()

tk.Label(root, text="algorithm:").pack(pady=(10,0))
algorithm_name_entry = tk.Entry(root)
algorithm_name_entry.pack()

# Submit Button
tk.Button(root, text="Submit", command=submit_form).pack(pady=20)

root.mainloop()
