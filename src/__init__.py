try:
    from pytesseract.pytesseract import image_to_string
    from pytesseract.pytesseract import image_to_data
    from pytesseract.pytesseract import image_to_boxes
except ImportError:
    from pytesseract.pytesseract import image_to_data
