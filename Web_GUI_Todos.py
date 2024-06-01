import streamlit as st
import functions as fun

todos = fun.get_todos()

st.title("My Todo App")
st.subheader("This is my Todo app")
st.write("This is to learn WebGUI App")


def New_Todo():
    new_todo = st.session_state["Add_Todo"] + "\n"
    todos.append(new_todo)
    fun.write_todos(todos)


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        fun.write_todos(todos)
        st.rerun()

st.text_input(label="", placeholder="Enter Todo",
              key='Add_Todo', on_change=New_Todo)






