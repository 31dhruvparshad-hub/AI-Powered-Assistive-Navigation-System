import streamlit as st
from PIL import Image
from ultralytics import YOLO
import pandas as pd

# -------------------------
# PAGE CONFIG
# -------------------------

st.set_page_config(
    page_title="AI-Powered Assistive Navigation System",
    page_icon="🚀",
    layout="wide"
)

# -------------------------
# CUSTOM CSS
# -------------------------

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

.hero {
    padding: 2rem;
    border-radius: 20px;
    background: linear-gradient(90deg, #0f172a, #1e293b);
    text-align: center;
    color: white;
    margin-bottom: 20px;
}

.feature-box {
    padding: 15px;
    border-radius: 15px;
    background-color: #1E293B;
    text-align: center;
}

.footer {
    text-align: center;
    color: gray;
    margin-top: 30px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------
# HERO SECTION
# -------------------------

try:
    st.image("assets/cover_page.png", use_container_width=True)
except:
    pass

st.markdown("""
<div class="hero">
<h1>🚀 AI-Powered Assistive Navigation System</h1>
<h4>
Real-Time Obstacle Detection • Spatial Awareness • Navigation Guidance
</h4>
</div>
""", unsafe_allow_html=True)

# -------------------------
# LOAD MODEL
# -------------------------

@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")

model = load_model()

# -------------------------
# SIDEBAR
# -------------------------

st.sidebar.title("📌 Project Overview")

st.sidebar.markdown("""
### Features

✅ YOLOv8 Object Detection

✅ Obstacle Analysis

✅ Navigation Recommendations

✅ Real-Time Processing

✅ Confidence Monitoring

---

### Tech Stack

- Python
- YOLOv8
- OpenCV
- PyTorch
- Streamlit
""")

# -------------------------
# TABS
# -------------------------

tab1, tab2, tab3 = st.tabs(
    [
        "📸 Detection",
        "📊 Analytics",
        "ℹ️ About"
    ]
)

# ====================================================
# TAB 1
# ====================================================

with tab1:

    st.subheader("Upload an Image")

    uploaded_file = st.file_uploader(
        "Choose an image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file:

        image = Image.open(uploaded_file)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Original Image")
            st.image(
                image,
                use_container_width=True
            )

        with st.spinner("Running YOLO Detection..."):

            results = model(image)

            annotated_image = results[0].plot()

        with col2:
            st.subheader("Detection Results")
            st.image(
                annotated_image,
                use_container_width=True
            )

        detected_objects = []

        data = []

        for box in results[0].boxes:

            cls = int(box.cls[0])
            conf = float(box.conf[0])

            name = model.names[cls]

            detected_objects.append(name)

            data.append({
                "Object": name,
                "Confidence": f"{conf:.2%}"
            })

        st.divider()

        # Metrics
        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Objects Detected",
                len(detected_objects)
            )

        with col2:
            st.metric(
                "Model",
                "YOLOv8m"
            )

        with col3:
            st.metric(
                "Status",
                "Active"
            )

        st.divider()

        st.subheader("📋 Detection Summary")

        df = pd.DataFrame(data)

        st.dataframe(
            df,
            use_container_width=True
        )

        st.divider()

        st.subheader("🧭 Navigation Recommendation")

        if "person" in detected_objects:

            st.error(
                "⚠️ Person detected ahead. Maintain distance."
            )

        elif "chair" in detected_objects:

            st.warning(
                "🪑 Chair detected. Potential obstacle ahead."
            )

        elif "car" in detected_objects:

            st.error(
                "🚗 Vehicle detected. Proceed with caution."
            )

        elif "truck" in detected_objects:

            st.error(
                "🚚 Truck detected nearby."
            )

        elif "bus" in detected_objects:

            st.error(
                "🚌 Bus detected nearby."
            )

        else:

            st.success(
                "✅ Path appears clear."
            )

# ====================================================
# TAB 2
# ====================================================

with tab2:

    st.subheader("📊 Detection Analytics")

    st.info(
        "Upload an image in the Detection tab to view analytics."
    )

    st.markdown("""

### Current System Capabilities

- Object Detection
- Spatial Awareness
- Obstacle Analysis
- Navigation Guidance
- Confidence Monitoring

### Planned Enhancements

- Real-Time Video Processing
- Depth Estimation (MiDaS)
- Multi-Object Tracking
- Route Planning
- Edge Deployment

""")

# ====================================================
# TAB 3
# ====================================================

with tab3:

    st.subheader("ℹ️ About The Project")

    st.markdown("""

### AI-Powered Assistive Navigation System

This project combines:

- YOLOv8 Object Detection
- Spatial Localization
- Proximity Estimation
- Danger Zone Analysis
- Intelligent Navigation Guidance

to provide real-time obstacle awareness and navigation support.

---

### Project Workflow

Camera Feed

⬇️

YOLOv8 Detection

⬇️

Obstacle Analysis

⬇️

Navigation Decision Engine

⬇️

Guidance Generation

---

### Author

Dhruv Parshad

""")

# -------------------------
# FOOTER
# -------------------------

st.markdown("---")

st.markdown(
    """
    <div class='footer'>
    Built with ❤️ using YOLOv8, Streamlit, OpenCV and PyTorch
    </div>
    """,
    unsafe_allow_html=True
)
