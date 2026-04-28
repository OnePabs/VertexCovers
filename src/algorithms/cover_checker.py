import pandas as pd
import time
import tkinter as tk
from tkinter import messagebox


def check_if_cover(edges_path, cover_path):
    # get edges pandas dataframe
    edges_df = pd.read_csv(edges_path, dtype=pd.StringDtype(), index_col=False)
    # get cover set
    cover_df = pd.read_csv(cover_path, dtype=pd.StringDtype(), index_col=False)
    cover_set = set(cover_df['nodes'])
    # check that each edge is in the cover 
    for edge in edges_df.itertuples():
        if edge.node1 not in cover_set and edge.node2 not in cover_set:
            return False
    return True

# Set up the window
root = tk.Tk()
root.title("Check if It really is a Cover")
root.geometry("900x600")

def submit_form():
    edges_path = edges_path_entry.get()
    cover_path = cover_path_entry.get()
    if edges_path and cover_path:
        if edges_path.startswith('\''):
            edges_path = edges_path[1:-1] # removes first AND last symbol
        if cover_path.startswith('\''):
            cover_path = cover_path[1:-1]
        start_time = time.perf_counter()
        is_cover = check_if_cover(edges_path,cover_path)
        end_time = time.perf_counter()
        runtime = end_time - start_time
        if is_cover:
            messagebox.showinfo("Success", "It is a cover. Runtime: " + str(runtime))
        else:
            messagebox.showinfo("Success", "It is NOT a cover. Runtime: " + str(runtime))
    else:
        messagebox.showerror("Error", "Fill all fields")

# Labels and Entry fields
tk.Label(root, text="edges file path (including name):").pack(pady=(10,0))
edges_path_entry = tk.Entry(root)
edges_path_entry.pack()

tk.Label(root, text="cover file path and name:").pack(pady=(10,0))
cover_path_entry = tk.Entry(root)
cover_path_entry.pack()


# Submit Button
tk.Button(root, text="Submit", command=submit_form).pack(pady=20)

root.mainloop()

