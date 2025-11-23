import streamlit as st

st.set_page_config(page_title="مدير المهام", page_icon="📝")
st.title("📝 تطبيق إدارة المهام (Python Only)")
st.write("هذا التطبيق يعمل بالكامل باستخدام بايثون فقط!")

if 'tasks' not in st.session_state:
    st.session_state.tasks = []

def add_task():
    task = st.session_state.new_task_input
    if task:
        st.session_state.tasks.append(task)
        st.session_state.new_task_input = ""

def delete_task(index):
    st.session_state.tasks.pop(index)

st.text_input("أدخل مهمة جديدة:", key="new_task_input", on_change=add_task)
st.button("إضافة", on_click=add_task)

st.markdown("---") 

if len(st.session_state.tasks) > 0:
    for i, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([0.8, 0.2]) 

        with col1:
            st.info(task)

        with col2:
            st.button("❌ حذف", key=f"delete_{i}", on_click=delete_task, args=(i,))
else:
    st.success("🎉 لا توجد مهام، استمتع بيومك!")

