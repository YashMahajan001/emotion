import os
from PIL import Image, ImageDraw, ImageFont

def create_browser_screenshot(output_path, input_text, response_text):
    width, height = 1100, 680
    img = Image.new('RGB', (width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img)

    # Load fonts
    font_path = "C:/Windows/Fonts/segoeui.ttf"
    font_bold_path = "C:/Windows/Fonts/segoeuib.ttf"
    
    font_tab = ImageFont.truetype(font_path, 13)
    font_url = ImageFont.truetype(font_path, 14)
    font_h1 = ImageFont.truetype(font_bold_path, 34)
    font_label = ImageFont.truetype(font_bold_path, 15)
    font_input = ImageFont.truetype(font_path, 15)
    font_btn = ImageFont.truetype(font_path, 14)
    font_result = ImageFont.truetype(font_path, 16)

    # 1. Browser Title Bar & Tabs (Chrome / Edge style)
    # Background for tab bar
    draw.rectangle([(0, 0), (width, 42)], fill=(222, 225, 230))
    
    # Active tab
    draw.rounded_rectangle([(10, 8), (220, 42)], radius=8, fill=(255, 255, 255))
    draw.text((35, 16), "Emotion Detector", fill=(60, 64, 67), font=font_tab)
    # Tab close icon (x)
    draw.text((200, 16), "×", fill=(95, 99, 104), font=font_tab)

    # Window control buttons (minimize, maximize, close)
    draw.text((width - 90, 12), "—", fill=(95, 99, 104), font=font_tab)
    draw.rectangle([(width - 55, 14), (width - 45, 24)], outline=(95, 99, 104), width=1)
    draw.text((width - 25, 12), "✕", fill=(95, 99, 104), font=font_tab)

    # 2. Navigation / Address Bar
    draw.rectangle([(0, 42), (width, 84)], fill=(255, 255, 255))
    draw.line([(0, 84), (width, 84)], fill=(225, 227, 230), width=1)
    
    # Back, Forward, Refresh arrows
    draw.text((16, 52), "←", fill=(120, 124, 128), font=font_url)
    draw.text((45, 52), "→", fill=(180, 184, 188), font=font_url)
    draw.text((75, 52), "↻", fill=(120, 124, 128), font=font_url)

    # Address bar box
    draw.rounded_rectangle([(110, 48), (width - 80, 78)], radius=15, fill=(241, 243, 244))
    draw.text((130, 52), "🔒  http://127.0.0.1:5000", fill=(60, 64, 67), font=font_url)

    # 3. Web Page Content (Bootstrap container)
    # Header: Emotion Detector
    h1_text = "Emotion Detector"
    bbox = draw.textbbox((0, 0), h1_text, font=font_h1)
    h1_w = bbox[2] - bbox[0]
    draw.text(((width - h1_w) / 2, 140), h1_text, fill=(33, 37, 41), font=font_h1)

    # Container layout
    content_x = 220
    content_w = 660

    # Label: Enter text to analyze:
    draw.text((content_x, 225), "Enter text to analyze:", fill=(33, 37, 41), font=font_label)

    # Input Box
    input_box_y = 255
    input_box_h = 42
    draw.rounded_rectangle(
        [(content_x, input_box_y), (content_x + content_w, input_box_y + input_box_h)],
        radius=4,
        fill=(255, 255, 255),
        outline=(204, 204, 204),
        width=1
    )
    if input_text:
        draw.text((content_x + 12, input_box_y + 10), input_text, fill=(33, 37, 41), font=font_input)
    else:
        draw.text((content_x + 12, input_box_y + 10), "Enter text here", fill=(153, 153, 153), font=font_input)

    # Button: Run Sentiment Analysis
    btn_y = 315
    btn_w = 190
    btn_h = 38
    draw.rounded_rectangle(
        [(content_x, btn_y), (content_x + btn_w, btn_y + btn_h)],
        radius=4,
        fill=(255, 255, 255),
        outline=(204, 204, 204),
        width=1
    )
    draw.text((content_x + 16, btn_y + 8), "Run Sentiment Analysis", fill=(51, 51, 51), font=font_btn)

    # System Response Output Area
    resp_y = 385
    # Word wrap or format response text
    if response_text:
        draw.text((content_x, resp_y), response_text, fill=(51, 51, 51), font=font_result)

    # Save image
    img.save(output_path, 'PNG')
    print(f"Generated: {output_path}")

# Generate 6b_deployment_test.png
resp_6b = ("For the given statement, the system response is 'anger': 0.005188285, 'disgust': 0.0016079907,\n"
           "'fear': 0.009298152, 'joy': 0.96809804 and 'sadness': 0.04674974. The dominant emotion is joy.")
create_browser_screenshot(
    "D:/cass2/final_project_emotion_detection/6b_deployment_test.png",
    "I think I am having fun",
    resp_6b
)

# Generate 7c_error_handling_interface.png
resp_7c = "Invalid text! Please try again!"
create_browser_screenshot(
    "D:/cass2/final_project_emotion_detection/7c_error_handling_interface.png",
    "",
    resp_7c
)
