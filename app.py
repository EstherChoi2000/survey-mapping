import streamlit as st
from mapping import generate_output

st.set_page_config(page_title="설문 매핑 엔진", layout="centered")

st.title("📋 학회 출고 품목 매핑 엔진")
st.markdown("설문 원문을 붙여넣으면 엑셀 입력값(0/1)을 자동 생성합니다.")

# 입력창
survey_text = st.text_area(
    label="설문 원문 붙여넣기",
    height=400,
    placeholder="여기에 설문 원문을 붙여넣으세요..."
)

# 실행 버튼
if st.button("🚀 변환 시작"):
    if not survey_text.strip():
        st.warning("설문 원문을 입력해주세요.")
    else:
        output = generate_output(survey_text)
        lines = output.split("\n")

        st.success("✅ 변환 완료!")

        # 결과 표시
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 결과 미리보기")
            for i, line in enumerate(lines, start=1):
                val = line if line != "" else "　(빈칸)"
                st.text(f"{i:02d}행: {val}")

        with col2:
            st.markdown("### 복사용 결과")
            st.text_area(
                label="엑셀에 붙여넣기",
                value=output,
                height=400
            )

        # 파일 다운로드
        st.download_button(
            label="📥 output.txt 다운로드",
            data=output,
            file_name="output.txt",
            mime="text/plain"
        )
