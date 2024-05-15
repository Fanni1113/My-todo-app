import streamlit as st
import functions


def add_todo():
    todo = st.session_state["new_todo"] +'\n'
    todos.append(todo)
    functions.write_todos(todos)


todos = functions.get_todos()

st.title("My To-Do App")
st.subheader("This is my todo app :-)")
st.write("This app increases productivity!")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox: # same as if checkbox==True:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="",
              placeholder="Enter a to-do, e.g.:"
              "feed the cat, fatten the beast, etc.",
              on_change=add_todo, key="new_todo")