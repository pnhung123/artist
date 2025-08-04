import streamlit as st
import re

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
st.write("Chọn tuỳ chọn hoặc nhập 'Khác'. Nếu chọn 'None', trường đó sẽ không xuất hiện trong prompt.")

# 📌 Chủ đề / Đối tượng
subject = st.text_input("📌 Chủ đề / Đối tượng", "Tuxedo cat")

# 🎨 Style
style = select_with_other("🎨 Style (Phong cách)", [
    "2D Playrix (casual mobile)",
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

# 📐 Composition (thêm Isometric)
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
    parts = []
    if subject: parts.append(f"Subject: {subject}")
    if style: parts.append(f"Style: {style}")
    if stroke != "None": parts.append(f"Stroke: {stroke}")
    if shading != "None": parts.append(f"Shading: {shading}")
    if lighting: parts.append(f"Lighting: {lighting}")
    if mood: parts.append(f"Mood: {mood}")

    camera_parts = []
    if camera_angle: camera_parts.append(f"- Angle: {camera_angle}")
    if camera_focus: camera_parts.append(f"- Focus: {camera_focus}")
    if depth_of_field: camera_parts.append(f"- Depth of Field: {depth_of_field}")
    if camera_parts:
        parts.append("Camera:\n" + "\n".join(camera_parts))

    other_parts = []
    if composition: other_parts.append(f"- Composition: {composition}")
    if surface_texture: other_parts.append(f"- Texture: {surface_texture}")
    other_parts.append(f"- No Yellow Tint: {no_yellow}")
    if ratio != "None": other_parts.append(f"- Ratio: {ratio}")
    other_parts.append(f"- Transparent Background: {transparent_background}")
    other_parts.append(f"- Number of Images: {n}")
    if other_parts:
        parts.append("Other Parameters:\n" + "\n".join(other_parts))

    prompt = "\n\n".join(parts)

    st.subheader("✨ Prompt đã tạo")
    st.code(prompt, language="yaml")
    st.success("Copy prompt này để sử dụng!")
