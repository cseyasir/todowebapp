import streamlit as st
import function
def add_todo():
    todo=st.session_state["new_todo"]
    todos=function.add(todo)
todos=function.get_todos()
st.title("My todos web app ")
st.subheader("This is my todos app.Developed using python")

for index ,todo in enumerate(todos):
    check_box= st.checkbox(todo,key=todo)
    if check_box:
        todos.pop(index)
        function.write_todos(todos)
        st.experimental_rerun()
st.text_input("",placeholder="Add new todo..",
              on_change=add_todo,
              key="new_todo")

st.button("Add")