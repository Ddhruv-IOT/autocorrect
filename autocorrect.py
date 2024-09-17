# import tkinter as tk
# from tkinter import ttk
# import collections
# import textdistance

# # dictionary = ['apple', 'banana', 'cherry', 'grape', 'orange', 'pear', 'pineapple']

# with open('big.txt', 'r') as file:
#     dictionary = file.read().split()
# # Load a dictionary of words with their frequencies from a file
# def load_dictionary():
    
#     return collections.Counter(dictionary)

# WORDS = load_dictionary()

# # Calculate edit distance using a DP approach
# def edit_distance(word1, word2):
#     m, n = len(word1), len(word2)
#     dp = [[0] * (n + 1) for _ in range(m + 1)]
    
#     for i in range(m + 1):
#         for j in range(n + 1):
#             if i == 0:
#                 dp[i][j] = j
#             elif j == 0:
#                 dp[i][j] = i
#             elif word1[i - 1] == word2[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1]
#             else:
#                 dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    
#     return dp[m][n]

# # Suggest using edit distance
# def suggest_using_edit_distance(word):
#     candidates = [(edit_distance(word, w), w) for w in WORDS]
#     candidates.sort()
#     return [w for _, w in candidates[:1]]

# # Suggest using textdistance library
# def suggest_using_textdistance(word):
#     # dictionary = ['apple', 'banana', 'cherry', 'grape', 'orange', 'pear', 'pineapple']
#     similarities = [(w, textdistance.levenshtein.normalized_similarity(word, w)) for w in dictionary]
#     nearest_words = [word for word, similarity in sorted(similarities, key=lambda x: x[1], reverse=True) if similarity > 0.5]
#     return nearest_words

# # Initialize variables
# last_word = ""
# original_word = ""
# correction_applied = False
# ignore_list = []

# # Update input with suggestion
# def update_input_with_suggestion():
#     global last_word, original_word, correction_applied

#     user_input = text_widget.get("1.0", tk.END).strip()
#     words_in_input = user_input.split()

#     if not words_in_input:
#         return

#     last_word = words_in_input[-1]

#     if last_word in ignore_list or correction_applied:
#         return

#     suggestion = suggest_using_edit_distance(last_word)[0]
#     print(suggestion)
    
#     if suggestion and suggestion != last_word:
#         original_word = last_word
#         words_in_input[-1] = suggestion
#         corrected_text = ' '.join(words_in_input)

#         text_widget.delete("1.0", tk.END)
#         text_widget.insert(tk.END, corrected_text)

#         text_widget.tag_configure('green', foreground='green')
#         start_idx = f"1.{len(user_input) - len(last_word)}"
#         end_idx = f"1.{len(corrected_text)}"
#         text_widget.tag_add('green', start_idx, end_idx)
        
#         correction_applied = True

# # Revert correction on backspace
# def handle_backspace(event):
#     global original_word, correction_applied

#     if correction_applied:
#         user_input = text_widget.get("1.0", tk.END).strip().split()
#         if user_input:
#             user_input[-1] = original_word
#             text_widget.delete("1.0", tk.END)
#             text_widget.insert(tk.END, ' '.join(user_input))

#             ignore_list.append(original_word)
#             correction_applied = False

# # Update suggestion table
# def update_suggestion_table():
#     user_input = text_widget.get("1.0", tk.END).strip().split()
#     if not user_input:
#         for item in table.get_children():
#             table.delete(item)
#         return

#     last_word = user_input[-1]
#     nearest_words_edit_distance = suggest_using_edit_distance(last_word)
#     nearest_words_textdistance = suggest_using_textdistance(last_word)

#     for item in table.get_children():
#         table.delete(item)

#     for word1, word2 in zip(nearest_words_edit_distance, nearest_words_textdistance):
#         table.insert("", "end", values=(word1, word2))

# # Handle space key and update both text and table
# def handle_space(event):
#     update_input_with_suggestion()
#     update_suggestion_table()

# # GUI setup
# app = tk.Tk()
# app.title("Auto Correct Tool")
# app.geometry("400x300")

# text_widget = tk.Text(app, width=30, height=2, font=("Helvetica", 14))
# text_widget.pack(pady=10)

# text_widget.bind("<space>", handle_space)
# text_widget.bind("<BackSpace>", handle_backspace)
# text_widget.bind("<KeyRelease>", lambda event: update_suggestion_table())

# # Table for showing the results
# table = ttk.Treeview(app, columns=("Edit Distance", "Textdistance"), show="headings", height=5)
# table.heading("Edit Distance", text="Edit Distance")
# table.heading("Textdistance", text="Textdistance")
# table.pack(pady=10)

# # Clear button
# clear_button = tk.Button(app, text="Clear", command=lambda: text_widget.delete("1.0", tk.END), bg="black", fg="white", font=("Helvetica", 12))
# clear_button.pack(pady=10)

# app.mainloop()


import tkinter as tk
from tkinter import ttk
import collections
import textdistance

with open('big.txt', 'r') as file:
    dictionary = file.read().split()

def load_dictionary():
    return collections.Counter(dictionary)

WORDS = load_dictionary()

def edit_distance(word1, word2):
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    
    return dp[m][n]

def suggest_using_edit_distance(word):
    candidates = [(edit_distance(word, w), w) for w in WORDS]
    candidates.sort()
    return [w for _, w in candidates[:1]]

def suggest_using_textdistance(word):
    similarities = [(w, textdistance.levenshtein.normalized_similarity(word, w)) for w in dictionary]
    nearest_words = [word for word, similarity in sorted(similarities, key=lambda x: x[1], reverse=True) if similarity > 0.5]
    return nearest_words

last_word = ""
original_word = ""
correction_applied = False
ignore_list = [" ", "", '']

# def update_input_with_suggestion():
#     global last_word, original_word, correction_applied

#     user_input = text_widget.get("1.0", tk.END).strip()
#     words_in_input = user_input.split()

#     # if not words_in_input:
#     #     return

#     last_word = words_in_input[-1]

#     if last_word in ignore_list:
#         return

#     suggestion = suggest_using_textdistance(last_word)[0]
#     print(last_word, suggestion)
    
#     if suggestion:
#         original_word = last_word
#         words_in_input[-1] = suggestion
#         corrected_text = ' '.join(words_in_input)

#         text_widget.delete("1.0", tk.END)
#         text_widget.insert(tk.END, corrected_text)

#         text_widget.tag_configure('green', foreground='green')
#         start_idx = f"1.{len(user_input) - len(last_word)}"
#         end_idx = f"1.{len(corrected_text)}"
#         text_widget.tag_add('green', start_idx, end_idx)
        
#         correction_applied = True

def update_input_with_suggestion():
    global last_word, original_word, correction_applied

    user_input = text_widget.get("1.0", tk.END).strip()
    words_in_input = user_input.split()

    if not words_in_input:
        return

    last_word = words_in_input[-1]

    # if last_word in ignore_list or correction_applied:
    #     return

    suggestion = suggest_using_textdistance(last_word)[0]
    
    if suggestion and suggestion != last_word:
        original_word = last_word
        words_in_input[-1] = suggestion
        corrected_text = ' '.join(words_in_input)

        text_widget.delete("1.0", tk.END)
        text_widget.insert(tk.END, corrected_text)

        text_widget.tag_configure('green', foreground='green')
        start_idx = f"1.{len(user_input) - len(last_word)}"
        end_idx = f"1.{len(corrected_text)}"
        text_widget.tag_add('green', start_idx, end_idx)
        
        correction_applied = True


def handle_backspace(event):
    global original_word, correction_applied

    if correction_applied:
        user_input = text_widget.get("1.0", tk.END).strip().split()
        if user_input:
            user_input[-1] = original_word
            text_widget.delete("1.0", tk.END)
            text_widget.insert(tk.END, ' '.join(user_input))

            ignore_list.append(original_word)
            correction_applied = False

def update_suggestion_table():
    user_input = text_widget.get("1.0", tk.END).strip().split()
    if not user_input:
        for item in table.get_children():
            table.delete(item)
        return

    last_word = user_input[-1]
    nearest_words_edit_distance = suggest_using_edit_distance(last_word)
    nearest_words_textdistance = suggest_using_textdistance(last_word)

    for item in table.get_children():
        table.delete(item)

    for word1, word2 in zip(nearest_words_edit_distance, nearest_words_textdistance):
        table.insert("", "end", values=(word1, word2))

def handle_space(event):
    app.after(50, update_input_with_suggestion)
    app.after(100, update_suggestion_table)

app = tk.Tk()
app.title("Auto Correct Tool")
app.geometry("400x300")

text_widget = tk.Text(app, width=50, height=4, font=("Helvetica", 14))
text_widget.pack(pady=10)

text_widget.bind("<space>", handle_space)
text_widget.bind("<BackSpace>", handle_backspace)
text_widget.bind("<KeyRelease>", lambda event: update_suggestion_table())

table = ttk.Treeview(app, columns=("Edit Distance", "Textdistance"), show="headings", height=5)
table.heading("Edit Distance", text="Edit Distance")
table.heading("Textdistance", text="Textdistance")
table.pack(pady=10)

clear_button = tk.Button(app, text="Clear", command=lambda: text_widget.delete("1.0", tk.END), bg="black", fg="white", font=("Helvetica", 12))
clear_button.pack(pady=10)

app.mainloop()
