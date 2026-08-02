import streamlit as st

# Set the page layout and browser tab settings for the app
st.set_page_config(page_title='Codner web service', page_icon=':capital_abcd:', layout='wide', initial_sidebar_state='expanded')

st.markdown(
    """
    <style>
    :root {
        color-scheme: dark;
    }
    .stApp {
        background: linear-gradient(135deg, #050505 0%, #111111 45%, #1f1f1f 100%);
        color: #f5f5f5;
    }
    .stSidebar {
        background: linear-gradient(180deg, #0a0a0a 0%, #171717 100%);
        border-right: 1px solid #444;
    }
    .st-emotion-cache-1y4p8pa, .st-emotion-cache-1v0mbdj, .st-emotion-cache-1wmy9hl {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.1);
        backdrop-filter: blur(8px);
    }
    h1, h2, h3, h4, h5, h6, p, div, span {
        color: #f5f5f5;
    }
    .stTextInput > div > div > input, .stTextArea > div > div > textarea {
        background-color: #111;
        color: #fff;
        border: 1px solid #666;
    }
    .stButton > button {
        background: linear-gradient(90deg, #ffffff 0%, #d1d1d1 100%);
        color: #000;
        border: none;
        font-weight: 700;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #f0f0f0 0%, #aaaaaa 100%);
        color: #000;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Create empty values for the form fields if they do not already exist
# This helps the app remember the user's input while they use the app
if 'business_name' not in st.session_state:
    st.session_state.business_name = ''
if 'business_description' not in st.session_state:
    st.session_state.business_description = ''
if 'business_address' not in st.session_state:
    st.session_state.business_address = ''
if 'business_phone' not in st.session_state:
    st.session_state.business_phone = ''
if 'business_email' not in st.session_state:
    st.session_state.business_email = ''

# Sidebar content: title and description of the web service
st.sidebar.title('codner web service')
st.sidebar.markdown('# THIS IS A WEB SERVICE FOR SMALL BUSINESSES')
st.sidebar.markdown('## This web service is designed to help small businesses create websites for their business')

# Sidebar form inputs for the business details
business_name = st.sidebar.text_input('Enter your business name', value=st.session_state.business_name)
business_description = st.sidebar.text_input('Enter your business description', value=st.session_state.business_description)
business_address = st.sidebar.text_input('Enter your business address', value=st.session_state.business_address)
business_phone = st.sidebar.text_input('Enter your business phone number', value=st.session_state.business_phone)
business_email = st.sidebar.text_input('Enter your business email', value=st.session_state.business_email)

# When the user clicks Submit, save the values into session state
if st.sidebar.button('Submit'):
    st.session_state.business_name = business_name
    st.session_state.business_description = business_description
    st.session_state.business_address = business_address
    st.session_state.business_phone = business_phone
    st.session_state.business_email = business_email
    st.sidebar.success('Business details saved!')

# my logo
st.markdown(
    """
    <div style="display:flex; align-items:center; justify-content:center; margin-bottom:10px;">
        <div style="font-size:54px; font-weight:bold; color:#2563eb; font-family:Georgia, serif;">
            C
        </div>
        <div style="margin-left:8px; font-size:22px; font-weight:700; color:#111827; letter-spacing:1px;">
            CODNER
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# Create two main columns so the page has a left and right section
column1, column2 = st.columns([1.2, 1], gap='small')

# Left column: intro text and business details preview
with column1:
    st.subheader('Web service for small businesses')
    st.markdown('I build simple, modern websites that help local businesses look professional online and connect with customers easily.')

    st.subheader('Your business details')

    # Show the saved business information if any values were entered
    if st.session_state.business_name or st.session_state.business_description or st.session_state.business_address or st.session_state.business_phone or st.session_state.business_email:
        st.write(f"**Business name:** {st.session_state.business_name}")
        st.write(f"**Description:** {st.session_state.business_description}")

        st.markdown('### Contact Information')
        st.write(f"**Address:** {st.session_state.business_address}")
        st.write(f"**Phone:** {st.session_state.business_phone}")
        if st.session_state.business_email:
            st.markdown(
                f"**Email:** <a href='mailto:{st.session_state.business_email}'>{st.session_state.business_email}</a>",
                unsafe_allow_html=True,
            )
        else:
            st.write('**Email:**')
    else:
        st.info('Submit the form in the sidebar to see your business information here.')

# Right column: project gallery preview
with column2:
    st.subheader('Project Gallery')
    st.caption('Sample website sections designed to feel polished and realistic.')

    # List of gallery items with project-style descriptions
    gallery_items = [
        ('Modern Homepage', 'https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=800&q=80', 'A clean landing page with bold branding and clear calls to action.'),
        ('About Section', 'https://images.unsplash.com/photo-1516321318423-f06f85e504b3?auto=format&fit=crop&w=800&q=80', 'A professional story section that builds trust with visitors.'),
        ('Services Layout', 'https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=800&q=80', 'A polished service card layout for showing offers clearly.'),
        ('Contact Form', 'https://images.unsplash.com/photo-1516321497487-e288fb19713f?auto=format&fit=crop&w=800&q=80', 'A simple contact area made for customer enquiries.'),
    ]

    # Display the gallery items in a compact, card-like format
    for i in range(0, len(gallery_items), 2):
        left_col, right_col = st.columns(2, gap='small')

        with left_col:
            title, image, description = gallery_items[i]
            st.markdown(f"### {title}")
            st.image(image, use_container_width=True)
            st.caption(description)

        if i + 1 < len(gallery_items):
            with right_col:
                title, image, description = gallery_items[i + 1]
                st.markdown(f"### {title}")
                st.image(image, use_container_width=True)
                st.caption(description)
    





    

               
        








