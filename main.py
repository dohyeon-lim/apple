import streamlit as st
from PIL import Image, ImageOps, ImageEnhance
import io

st.set_page_config(page_title="나만의 캐릭터 편집기", layout="centered")

st.title("🎨 이미지 편집기 (웹 버전)")
st.write("이미지를 올리고 원하는 효과를 적용해 보세요!")

# 1. 파일 업로드 기능
uploaded_file = st.file_uploader("편집할 이미지를 선택하세요 (png, jpg, jpeg)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # 이미지 불러오기
    image = Image.open(uploaded_file).convert("RGB")

    st.subheader("원본 이미지")
    st.image(image, use_column_width=True)

    st.divider()
    st.subheader("편집 도구")

    # 2. 편집 옵션 선택 (사이드바 또는 버튼)
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("흑백 변환"):
            image = ImageOps.grayscale(image)
            st.session_state['mode'] = 'gray'

    with col2:
        if st.button("좌우 반전"):
            image = ImageOps.mirror(image)

    with col3:
        if st.button("색상 반전"):
            image = ImageOps.invert(image)

    # 3. 밝기 조절 슬라이더
    brightness = st.slider("밝기 조절", 0.5, 2.0, 1.0)
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(brightness)

    # 4. 최종 결과물 표시
    st.divider()
    st.subheader("편집 결과")
    st.image(image, use_column_width=True)

    # 5. 결과물 다운로드 버튼
    buf = io.BytesIO()
    image.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label="편집된 이미지 다운로드",
        data=byte_im,
        file_name="edited_image.png",
        mime="image/png"
    )

else:
    st.info("이미지 파일을 업로드하면 편집 도구가 나타납니다.")