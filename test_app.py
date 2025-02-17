from streamlit_qr_generator import generate_qr_code

def test_qr_code_generation():
    # Test with basic parameters
    data = "Test QR Code"
    box_size = 10
    border = 4
    fill_color = "black"
    back_color = "white"
    
    qr_image, error = generate_qr_code(data, box_size, border, fill_color, back_color)
    
    assert error is None
    assert qr_image is not None
    assert hasattr(qr_image, 'save')  # Check if it's a PIL Image object

def test_empty_data():
    # Test with empty data
    qr_image, error = generate_qr_code("", 10, 4, "black", "white")
    
    assert qr_image is not None  # Should use "Preview" as default text
    assert error is None

def test_invalid_parameters():
    # Test with invalid parameters
    qr_image, error = generate_qr_code("Test", -1, -1, "black", "white")
    
    assert qr_image is not None  # Should handle negative values
    assert error is None  # Should correct invalid values 