#importing necessary libraries
import os
import streamlit as st
import time


#defining page title and icon
st.set_page_config(page_title = "shutdown.exe",page_icon = "📂")
st.title(":violet[SYS COMMANDS]")

#assigning buttons and variables
n = 10
t = st.number_input(":green[ENTER SECONDS]",0,3600)#assigning input
if t>0:
    n = t
e = st.button(":green[TEST]")
a = st.button(":red[SHUTDOWN]")
b = st.button(":blue[RESTART]")
c = st.button(":orange[STOP/CLEAR]")

#st.header(":grey[TIMER]")

#countdown
def uhd():
    p = 0
    for i in range(n):
        p+=1
        st.write(p)
        time.sleep(1)
        st.toast(p)
        if c:
            break

#stopping functions
def stop():
    return os.system("shutdown -a")
def shutdown():
    return os.system(f"shutdown /s /t {n}")
def shutdown_l():
    return os.system("shutdown -h +10")
def restart_l():
    return os.system("shutdown -r +10")
def restart():
    return os.system(f"shutdown /r /t {n}")

#logic
if c:
    stop()

if e:
    st.header(":green[#TESTING PHASE#]")
    st.header(":grey[TIMER]")
    st.warning(f"YOUR SYSTEM WILL SHUTDOWN WITHIN {n} SEC")
    st.toast(f"TESTING ENDS IN {n} SEC")
    uhd()

if a:
    st.warning(f"YOUR SYSTEM WILL SHUTDOWN WITHIN {n} SEC")
    st.header(":grey[TIMER]")
    st.toast(f"SHUTDOWN BEGINS IN {n} SEC")
    shutdown()
    uhd()
    if c:
        stop()
if b:
    st.warning(f"YOUR SYSTEM WILL RESTART WITHIN {n} SEC")
    st.header(":grey[TIMER]")
    st.toast(f"RESTART BEGINS IN {n} SEC")
    restart()
    uhd()
    if c:
        stop()

    
