import streamlit as st
import functions

'''
strong for run
streamlit run web.py
'''

todos = functions.get_todos()


def add_todo():
    todo = st.session_state['new_todo'] + '\n'

    todos.append(todo)
    functions.write_todos(todos)


st.title('My ToDo App')
st.subheader('This is my todo app')
st.write('My simple text')
for index, todo in enumerate(functions.get_todos()):
    checkbox = st.checkbox(todo[0:-1], key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        # delete to-do from session dict
        del st.session_state[todo]
        # rerun session page
        st.experimental_rerun()

st.text_input(label='_',
              label_visibility='hidden',
              placeholder='Input ToDo',
              on_change=add_todo,
              key='new_todo')

st.session_state
