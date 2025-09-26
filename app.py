import streamlit as st
from streamlit_lottie import st_lottie
import requests
from Pages.demo import main

# --- Page Config ---
st.set_page_config(page_title="Recommendation System", page_icon="🛒", layout="wide")

# --- Global Background (gradient + professional look) ---
page_bg = """
<style>
   /* Main app background */
[data-testid="stAppViewContainer"]{
    background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 25%, #fbc2eb 50%, #a18cd1 75%, #fbc2eb 100%);
    background-size: cover;
    background-attachment: fixed;
}

    /* Transparent header */
    [data-testid="stHeader"] {
        background: rgba(0,0,0,0);
    }

    /* Transparent tabs */
    [data-baseweb="tab-list"] {
        background: rgba(255,255,255,0.0);
    }
    [data-baseweb="tab"] {
        background: rgba(255,255,255,0.2);
        border-radius: 10px;
        margin-right: 5px;
        padding: 5px 10px;
        transition: 0.3s;
    }
    [data-baseweb="tab"]:hover {
        background: rgba(255,255,255,0.35);
    }

    /* Font styling */
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Segoe UI', sans-serif;
        color: #03396c;
    }
    p {
        font-family: 'Segoe UI', sans-serif;
        color: #03396c;
    }

    /* Card style for sections */
    .stImage img {
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)
st.markdown(page_bg, unsafe_allow_html=True)

# --- Hide Sidebar completely ---
st.markdown("""
<style>
    section[data-testid="stSidebar"] {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)

# --- Helper for Lottie animations ---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Optional Lottie animation
shopping_anim = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_4vlqvyzj.json")

# --- Tabs ---
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home", "✨ Recommendation", "ℹ️ About", "📞 Contact"])

# ================= HOME TAB =================
with tab1:
    st.markdown("<h1 style='text-align: center;'>🛒 Smart Product Recommendation System</h1>", unsafe_allow_html=True)

    # Welcome Text
    st.markdown("<h3 style='text-align: center;'>Welcome!</h3>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center;'>"
        "Discover products tailored to your preferences.<br>"
        "Select a <b>Category</b>, <b>Brand</b>, or enter a <b>Product Name</b> to get smart recommendations."
        "</p>",
        unsafe_allow_html=True
    )

    # Main Image
    col_left, col_center, col_right = st.columns([1,1,3])
    with col_right:
        st.image("assets/Image/Shopping.jpg", caption="3D Cartoon Shopping", width=400)

    if st.button("🚀 Start Exploring"):
        st.success("Go to the **Recommendation** tab to explore personalized results!")

    # Lottie animation
    if shopping_anim:
        st_lottie(shopping_anim, height=300, key="shop")

    # Featured Categories
    st.markdown("### 🌟 Featured Categories")
    featured_products = {
        "Laptop": "assets/Image/Laptop1.jpg",
        "Mobile": "assets/Image/mobile1.jpg",
        "Headphones": "assets/Image/headphones.jpg",
        "Smart TV": "assets/Image/Smart Tv.jpg"
    }

    cols = st.columns(len(featured_products))
    for col, (name, img_url) in zip(cols, featured_products.items()):
        with col:
            st.image(img_url, caption=name, width=250)

    # Stats Section
    st.markdown("### 📊 Platform Highlights")
    colA, colB, colC = st.columns(3)
    colA.metric("Products Available", "1,200+")
    colB.metric("Happy Customers", "3,450+")
    colC.metric("Brands Covered", "150+")

    # Professional Banner
    st.markdown("""
    <div style="margin-top:30px; text-align:center; padding:20px;
                 background:linear-gradient(90deg,#43cea2,#185a9d);
                 color:white; border-radius:12px; font-size:18px;">
        🎉 Exclusive Offer: Flat 20% OFF on Electronics | 🚚 Free Shipping Above ₹999
    </div>
    """, unsafe_allow_html=True)

# ================= RECOMMENDATION TAB =================
with tab2:
    st.title("✨ Get Your Recommendations")
    main()

# ================= ABOUT TAB =================
with tab3:
    st.title("ℹ️ About")

    st.markdown("""
    **Smart Product Recommendation System** is a demo platform built with Streamlit that helps users discover products tailored to their preferences.  

    **Key Features:**
    - **Personalized Recommendations:** Get product suggestions based on selected categories, brands, or specific products.  
    - **Easy Navigation:** User-friendly interface with multiple tabs for Home, Recommendations, About, and Contact.  
    - **Featured Categories & Offers:** Quickly explore popular product categories and exclusive discounts.  
    - **Analytics & Insights:** View platform highlights such as total products, brands covered, and happy customers.  

    This system demonstrates how data science and AI techniques can enhance the shopping experience by providing smart, relevant product recommendations.
    """)

    st.markdown("**Built With:** Streamlit, Python, Pandas, and Lottie animations for enhanced user experience.")

# ================= CONTACT TAB =================
with tab4:
    st.title("📞 Contact Us")
    st.write("Email: support@example.com")
