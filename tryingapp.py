import streamlit as st

def main():
    st.title("ShopFloorPlanner")

    menu = ["Generate"]

    choice = st.sidebar.selectbox("Choose an option", menu)

    if choice == "Generate":
        st.subheader("Upload")
        json_filename = st.file_uploader("Generate your shop floor plan here", type=["json"], accept_multiple_files = True)
        if json_filename is not None:
            st.write("You uploaded:", type(json_filename))

     
        
if __name__ == "__main__":
    main()