import streamlit as st
import re
import json

# Cấu hình trang
st.set_page_config(page_title="🎨 Artist Prompt Builder", page_icon="🎨", layout="centered")

# CSS để căn giữa và giới hạn chiều ngang
st.markdown(
    """
    <style>
    .main {
        max-width: 800px;
        margin: auto;
        padding: 30px;
        background-color: #ffffff;
        border-radius: 15px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Hàm xử lý
def clean_option(option: str) -> str:
    """Xoá chú thích trong ngoặc đơn"""
    return re.sub(r"\s*\(.*?\)", "", option).strip()

def select_with_other(label, options):
    """Dropdown có thêm 'None' và 'Khác' cho phép nhập text"""
    choice = st.selectbox(label, ["None"] + options + ["Khác"])
    if choice == "Khác":
        return st.text_input(f"Nhập {label}")
    elif choice == "None":
        return None
    else:
        return clean_option(choice)

# Tiêu đề
st.title("🎨 Artist Prompt Builder")
st.write("Chọn tuỳ chọn hoặc nhập 'Khác'. Nếu chọn 'None', trường đó sẽ không xuất hiện trong JSON.")

# 📌 Chủ đề / Đối tượng
subject = st.text_input("📌 Chủ đề / Đối tượng", "Tuxedo cat")

# 🎨 Style
style = select_with_other("🎨 Style (Phong cách)", [
    "Playrix Game style (casual mobile)",
    "Minimalism (Tối giản)", "Cubism (Lập thể)", "Pop Art (Nghệ thuật đại chúng)",
    "Digital Painting (Hội họa kỹ thuật số)", "Concept Art (Mỹ thuật ý tưởng)", 
    "Line Art (Tranh nét)", "Watercolor (Màu nước)", "Oil Painting (Sơn dầu)", 
    "Pencil Sketch (Phác họa chì)", "3D Rendering (Kết xuất 3D)", 
    "Pixel Art (Nghệ thuật pixel)", "Anime Style (Phong cách Anime)", 
    "Comic / Manga Style (Phong cách truyện tranh)"
])

# ✏️ Stroke và 🌗 Shading
stroke = st.radio("✏️ Stroke (viền)", ["None", "yes", "no"], index=1)
shading = st.radio("🌗 Shading (đổ bóng)", ["None", "yes", "no"], index=2)

# 💡 Lighting
lighting = select_with_other("💡 Lighting (Ánh sáng)", [
    "Soft Light (Ánh sáng dịu)", "Natural Light (Ánh sáng tự nhiên)", "Studio Light (Ánh sáng phòng thu)",
    "Backlight (Ngược sáng)", "Rim Light (Ánh sáng viền)", "Hard Light (Ánh sáng gắt)",
    "Low Key Lighting (Ánh sáng tối / tương phản mạnh)", "High Key Lighting (Ánh sáng sáng / ít bóng đổ)",
    "Neon Lighting (Ánh sáng neon)"
])

# 🎭 Mood
mood = select_with_other("🎭 Mood (Bầu không khí)", [
    "Dramatic (Kịch tính)", "Mysterious (Huyền bí)", "Romantic (Lãng mạn)", 
    "Peaceful (Thanh bình)", "Dark (U ám)", "Bright (Tươi sáng)", 
    "Epic (Hoành tráng)", "Horror (Kinh dị)", "Dreamlike (Như mơ)", 
    "Surreal (Siêu thực)", "Melancholic (U sầu)", "Energetic (Tràn đầy năng lượng)",
    "Joyful (Vui tươi)", "Nostalgic (Hoài niệm)", "Futuristic (Tương lai)"
])

# 📷 Camera Angle
camera_angle = select_with_other("📷 Camera Angle (Góc máy ảnh)", [
    "Eye Level (Ngang tầm mắt)", "High Angle (Góc cao nhìn xuống)", "Low Angle (Góc thấp nhìn lên)",
    "Bird’s Eye View (Nhìn từ trên cao)", "Worm’s Eye View (Nhìn từ dưới đất)", 
    "Dutch Angle (Góc nghiêng lệch)", "Close-up (Cận cảnh)", "Medium Shot (Trung cảnh)", 
    "Long Shot (Toàn cảnh)", "POV (Góc nhìn nhân vật)", "Wide Angle (Góc rộng)",
    "Tilted Angle (Góc máy nghiêng)", "Panoramic (Toàn cảnh 360 độ)"
])

# 🔍 Camera Focus
camera_focus = select_with_other("🔍 Camera Focus (Lấy nét)", [
    "Sharp Focus (Nét căng)", "Soft Focus (Nét mờ dịu)", "Macro Focus (Lấy nét siêu gần)",
    "Bokeh Effect (Hiệu ứng bokeh – hậu cảnh mờ)", "Selective Focus (Chọn lọc vùng nét)",
    "Motion Blur (Nhòe chuyển động)", "Depth Focus (Lấy nét theo độ sâu)"
])

# 📏 Depth of Field
depth_of_field = select_with_other("📏 Depth of Field (Độ sâu trường ảnh)", [
    "Shallow Depth of Field (Trường ảnh nông – hậu cảnh mờ nhiều)",
    "Deep Depth of Field (Trường ảnh sâu – tất cả chi tiết rõ nét)",
    "Tilt-Shift (Giả lập mô hình thu nhỏ)",
    "Cinematic DOF (Trường ảnh kiểu điện ảnh)"
])

# 📐 Composition
composition = select_with_other("📐 Composition (Bố cục)", [
    "Rule of Thirds (Quy tắc một phần ba)", "Golden Ratio (Tỷ lệ vàng)", "Symmetry (Đối xứng)",
    "Leading Lines (Đường dẫn thị giác)", "Negative Space (Khoảng trống)", "Isometric"
])

# 🧩 Surface Texture
surface_texture = select_with_other("🧩 Texture (Chất liệu bề mặt)", [
    "Smooth (Mịn)", "Rough (Thô)", "Glossy (Bóng)", "Matte (Mờ)", 
    "Metallic (Kim loại)", "Organic (Tự nhiên)"
])

# 🚫 Không bị ám vàng
no_yellow = st.radio("🚫 Không bị ám vàng", ["yes", "no"], index=1)

# 🖼️ Image Ratio / Transparent BG / Number of Images
ratio = st.selectbox("🖼️ Image Ratio", ["None", "1:1", "9:16", "16:9", "3:4"])
transparent_background = st.radio("🔲 Transparent Background", ["yes", "no"], index=1)
n = st.slider("📦 Số lượng ảnh tạo", 1, 5, 1)

# Nút xuất prompt
if st.button("🚀 Xuất Prompt"):
    output = {
        "Subject": subject,
        "Style": style if style else None,
        "Stroke": stroke if stroke != "None" else None,
        "Shading": shading if shading != "None" else None,
        "Lighting": lighting if lighting else None,
        "Mood": mood if mood else None,
        "Camera": {
            "Angle": camera_angle if camera_angle else None,
            "Focus": camera_focus if camera_focus else None,
            "Depth of Field": depth_of_field if depth_of_field else None
        },
        "Other Parameters": {
            "Composition": composition if composition else None,
            "Texture": surface_texture if surface_texture else None,
            "No Yellow Tint": no_yellow,
            "Ratio": ratio if ratio != "None" else None,
            "Transparent Background": transparent_background,
            "Number of Images": str(n)
        }
    }

    # Hàm xoá key None
    def remove_none(d):
        if isinstance(d, dict):
            return {k: remove_none(v) for k, v in d.items() if v is not None}
        return d

    clean_output = remove_none(output)

    st.subheader("✨ Prompt đã tạo (JSON)")
    st.code(json.dumps(clean_output, indent=4, ensure_ascii=False), language="json")
    st.success("Copy JSON này để sử dụng!")
