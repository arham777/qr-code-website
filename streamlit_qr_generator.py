import streamlit as st
import qrcode
from PIL import Image
import io

# Set page configuration
st.set_page_config(
    page_title="Professional QR Code Generator",
    page_icon="🔲",
    layout="centered"
)

# Streamlit CSS for professional styling and animations
st.markdown("""
    <style>
        body {
            background-color: #1e1e2f;
            color: #e4e4eb;
            font-family: 'Arial', sans-serif;
        }
        
        .stApp {
            background: #2b2b3d;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
        }
        
        h1, h2, h3, h4, h5, h6 {
            color: #ffffff;
        }
        
        .stTextArea textarea {
            background-color: #3b3b4f;
            color: #e4e4eb;
            border: 1px solid #4e4e6e;
            border-radius: 10px;
        }
        
        .stSlider > div > div > div > input {
            color: #e4e4eb;
        }
        
        .st-expander {
            background-color: #3b3b4f;
            border: 1px solid #4e4e6e;
            border-radius: 10px;
        }
        
        .stButton > button {
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 10px;
            padding: 10px 20px;
            transition: all 0.3s ease;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
        }
        
        .stButton > button:hover {
            background-color: #45a049;
            box-shadow: 0 6px 16px rgba(0, 0, 0, 0.4);
            transform: translateY(-2px);
        }
        
        .stDownloadButton > button {
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 10px;
            padding: 10px 20px;
            transition: all 0.3s ease;
            cursor: pointer;
        }
        
        .stDownloadButton > button:hover {
            background-color: #0056b3;
            transform: translateY(-2px);
        }
        
        .stImage {
            border: 2px solid #4CAF50;
            border-radius: 15px;
            padding: 10px;
            background-color: white;
            max-width: 300px !important;
            margin: 0 auto;
            display: block;
        }
        
        .footer {
            text-align: center;
            color: #888888;
            padding: 20px;
        }

        .preview-container {
            padding: 15px;
            border-radius: 10px;
            background-color: #3b3b4f;
            margin: 20px 0;
            max-width: 300px;
            margin: 20px auto;
        }

        /* Center all images */
        img {
            display: block;
            margin: 0 auto;
        }
    </style>
""", unsafe_allow_html=True)

def generate_qr_code(data, box_size, border, fill_color, back_color):
    try:
        # Ensure minimum size and border values
        box_size = max(1, box_size)
        border = max(0, border)
        
        # If no data provided, use a sample text for preview
        if not data:
            data = "Preview"
        
        qr = qrcode.QRCode(
            version=1,  # Fixed version for consistent size
            error_correction=qrcode.constants.ERROR_CORRECT_M,  # Medium error correction
            box_size=box_size,
            border=border
        )
        qr.add_data(data)
        qr.make(fit=True)
        
        qr_image = qr.make_image(
            fill_color=fill_color,
            back_color=back_color
        )

        # Resize image if it's too large
        width, height = qr_image.size
        max_size = 300  # Maximum size in pixels
        if width > max_size:
            ratio = max_size / width
            new_size = (max_size, int(height * ratio))
            qr_image = qr_image.resize(new_size, Image.Resampling.LANCZOS)
            
        return qr_image, None
    except Exception as e:
        return None, str(e)

# Header Section
st.title("🔲 Professional QR Code Generator")
st.markdown("Effortlessly create custom QR codes with a sleek and modern UI.")

# Input Section
with st.container():
    data = st.text_area(
        "Enter text or URL",
        placeholder="Enter the content for your QR code here...",
        help="Type or paste the text/URL you want to convert into a QR code"
    )
    
    # Customization Options
    st.markdown("### Customize Your QR Code")
    
    # Preview container
    preview_container = st.empty()
    
    col1, col2 = st.columns(2)
    with col1:
        box_size = st.slider(
            "QR Code Size",
            min_value=1,
            max_value=12,  # Reduced maximum size
            value=6,  # Smaller default value
            help="Adjust the size of QR code modules (1-12 pixels per module)"
        )
        fill_color = st.color_picker(
            "QR Code Color",
            "#000000",
            help="Choose the color of QR code patterns"
        )
    with col2:
        border = st.slider(
            "Border Size",
            min_value=0,
            max_value=4,  # Reduced maximum border
            value=2,  # Smaller default value
            help="Adjust the quiet zone around the QR code (0-4 modules)"
        )
        back_color = st.color_picker(
            "Background Color",
            "#FFFFFF",
            help="Choose the background color"
        )

    # Live Preview
    qr_image, error = generate_qr_code(data, box_size, border, fill_color, back_color)
    if qr_image and not error:
        img_buffer = io.BytesIO()
        qr_image.save(img_buffer, format="PNG")
        img_buffer.seek(0)
        preview_container.markdown("""
            <div class="preview-container">
                <h4 style="color: #e4e4eb; margin-bottom: 10px;">Live Preview</h4>
            </div>
        """, unsafe_allow_html=True)
        preview_container.image(img_buffer, caption="QR Code Preview", use_column_width=False, width=250)

# Generate Final QR Code
if st.button("Generate Final QR Code"):
    if data:
        with st.spinner("Creating your QR code..."):
            qr_image, error = generate_qr_code(data, box_size, border, fill_color, back_color)
            
            if error:
                st.error(f"Error generating QR code: {error}")
            else:
                img_buffer = io.BytesIO()
                qr_image.save(img_buffer, format="PNG")
                img_buffer.seek(0)
                
                # Display final QR code with rounded corners
                st.image(img_buffer, caption="Your Professional QR Code", use_column_width=False, width=250)
                
                # Download Button
                st.download_button(
                    label="Download QR Code",
                    data=img_buffer,
                    file_name="qr_code.png",
                    mime="image/png"
                )
    else:
        st.error("Please enter some text or URL to generate a QR code!")

# Footer
st.markdown("<div class='footer'>Made with ❤️ by Muhammad Arham Athar</div>", unsafe_allow_html=True)
