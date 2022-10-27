import streamlit as st
import time
from streamlit_js_eval import streamlit_js_eval, copy_to_clipboard, create_share_link, get_geolocation

for i in range(10):
    location = get_geolocation(component_key = str(i) )
    st.write(location)
    time.sleep(2)

