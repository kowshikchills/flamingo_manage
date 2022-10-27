
import yaml
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu
import streamlit as st

auth_file = 'streamlitpasswords/drive_auth.yaml'
with open(auth_file) as file:
    config = yaml.load(file, Loader=yaml.SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
st.session_state["name"], st.session_state["authentication_status"], st.session_state["username"] = authenticator.login('Login', 'main')
if st.session_state["authentication_status"]:
    with st.sidebar:
        selected_menu = option_menu(
            menu_title="Flamingo Driver",  
            options=["Ride",'Bills','Report Issue'],  
            icons=["house", "bookmark", 'bookmark'],  
            menu_icon="cast", 
            default_index=0,  
        )
    if selected_menu == 'Ride':

        st.subheader('Ride Start')
        start_reading = st.number_input('Speedometer Reading')
        number_of_passengers = st.number_input('Passenger Count')
        col1,col2,col3,col4,col5 = st.columns(5)
        st.subheader('Add Images')
        picture1 = col1.camera_input("Car Front")
        picture2 = col2.camera_input("Car Left")
        picture3 = col3.camera_input("Car Right")
        picture4 = col4.camera_input("Car back")
        pictureD = col5.camera_input("Dashboard")
        if picture1:
            col1.image(picture1)
        if picture2:
            col2.image(picture2)
        if picture3:
            col3.image(picture3)
        if picture4:
            col4.image(picture4)
        if pictureD:
            col5.image(pictureD)
    
        

elif st.session_state["authentication_status"] == False:
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] == None:
    st.warning('Please enter your username and password')

#authenticator.logout('Logout', 'main')