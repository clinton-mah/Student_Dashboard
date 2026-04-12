import streamlit as st

st.title("Student Dashboard")

if "dic" not in st.session_state:
    st.session_state.dic = {} 
name = st.text_input("enter student name")
marks = st.number_input("enter student marks", min_value=0, max_value=100)

if st.button("add student"):
	if name:
		st.session_state.dic[name] = marks
		st.success(f"{name} added")
	else:
		st.error("enter a name")
dic = st.session_state.dic

st.write("current data: ",dic)
if len(dic)>0:
	lst = list(dic.values())

	ave = sum(lst)/len(lst)
	maximum = max(lst)
	minimum = min(lst)

	
	st.write("Average: ",ave)
	st.write("Minimum: ",minimum)
	st.write("Maximum: ",maximum)

	if ave >= 50:
		st.success("class outcome: Pass ")
	else:
		st.error("class outcome: fail ")

	top_student = max(dic, key=dic.get)
	st.write("top student: ", top_student)
