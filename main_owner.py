import pickle 
import yaml
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu
import streamlit as st

auth_file = 'streamlitpasswords/auth.yaml'
with open(auth_file) as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
status = False
st.session_state["name"], st.session_state["authentication_status"], st.session_state["username"] = authenticator.login('Login', 'main')
status =  st.session_state["authentication_status"]
if status == False or status == None:
    if st.checkbox('New User', value= False):
        try:
            if authenticator.register_user('Register user', preauthorization=False):
                st.success('User registered successfully')
                with open(auth_file) as file:
                    config = yaml.load(file, Loader=yaml.SafeLoader)
                config['credentials'] = authenticator.credentials
                with open(auth_file, "w") as f:
                    yaml.dump(config, f)
        except Exception as e:
            st.error(e)

if st.session_state["authentication_status"]:
    with st.sidebar:
        selected_menu = option_menu(
            menu_title="Flamingo Owner",  
            options=["Home", "My Cars", "Bookings", 'Settings', 'Support'],  
            icons=["house", "bezier2", "lightning", 'bookmark', 'envelope'],  
            menu_icon="cast", 
            default_index=0,  
        )
    

elif st.session_state["authentication_status"] == False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] == None:
    st.warning('Please enter your username and password')



#authenticator.logout('Logout', 'main')