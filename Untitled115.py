#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import messagebox, filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def load_data():
    filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if filepath:
        try:
            df = pd.read_csv(filepath)
            analyze_data(df)
        except Exception as e:
            
            messagebox.showerror("Error", f"Failed to load file:\n{e}")

def analyze_data(df):
    print("\nData Summary:")
    print(df.describe())

    plot_window = tk.Toplevel(root)
    plot_window.title("Employment Data Analysis")

    fig1, ax1 = plt.subplots(figsize=(6, 4))
    sns.lineplot(data=df, x='Year', y='Employment Rate', hue='Country', ax=ax1)
    ax1.set_title('Employment Rate Over Years')
    canvas1 = FigureCanvasTkAgg(fig1, master=plot_window)
    canvas1.draw()
    canvas1.get_tk_widget().pack()

    fig2, ax2 = plt.subplots(figsize=(6, 4))
    sns.lineplot(data=df, x='Year', y='Unemployment Rate', hue='Country', ax=ax2)
    ax2.set_title('Unemployment Rate Over Years')
    canvas2 = FigureCanvasTkAgg(fig2, master=plot_window)
    canvas2.draw()
    canvas2.get_tk_widget().pack()

    fig3, ax3 = plt.subplots(figsize=(6, 4))
    avg_rate = df.groupby('Country')['Employment Rate'].mean().sort_values(ascending=False)
    sns.barplot(x=avg_rate.values, y=avg_rate.index, ax=ax3, palette='Blues_d')
    ax3.set_title('Average Employment Rate by Country')
    canvas3 = FigureCanvasTkAgg(fig3, master=plot_window)
    canvas3.draw()
    canvas3.get_tk_widget().pack()

root = tk.Tk()
root.title("Employment Data Analyzer")
root.geometry("400x200")

label = tk.Label(root, text="Employment Data Analyzer", font=("Arial", 16))
label.pack(pady=10)

btn = tk.Button(root, text="Load CSV and Analyze", command=load_data, font=("Arial", 12))
btn.pack(pady=20)
root.mainloop()


# In[ ]:




