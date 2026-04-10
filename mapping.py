import re

BLANK_ROWS = {1, 8, 15, 23, 27, 37, 41, 44, 50, 52, 56, 59}

SYNONYMS = {
    "제품 브로셔": "제품브로셔",
    "BLX & TLX": "BLX&TLX",
    "BLC & BLX": "BLX & BLC",
    "Axiom PX 파노라마": "Axiom PX파노라마",
    "Axiom X3 파노라마": "Axiom X3파노라마",
    "Integral 파노라마": "integral 파노라마",
    "러버블/ 스푼/ 스포이드": "러버블/스푼/스포이드",
    "x4 더미_TL": "x4 더미 TL",
    "x4 더미_BLT": "x4 더미 BLT",
    "x4 더미_BLX": "x4 더미 BLX",
    "미니배너 (탁자거치)": "미니배너",
    "스탠딩배너": "스탠딩 배너",
    "Axiom X3 메가 모델": "Axiom X3 메가모델",
    "Axiom제품브로셔": "Axiom 제품브로셔",
    "회사소개서": "회사 소개서",
    "테이블 배너": "테이블배너",
}

ROW_DEFINITIONS = {
    2:  ("스트라우만", "임플란트 모형", "TL"),
    3:  ("스트라우만", "임플란트 모형", "BL"),
    4:  ("스트라우만", "임플란트 모형", "BLT"),
    5:  ("스트라우만", "임플란트 모형", "BLX"),
    6:  ("스트라우만", "임플란트 모형", "TLX"),
    7:  ("스트라우만", "임플란트 모형", "BLX & BLC"),
    9:  ("스트라우만", "서지컬 키트", "Full"),
    10: ("스트라우만", "서지컬 키트", "BLT"),
    11: ("스트라우만", "서지컬 키트", "BLX&TLX"),
    12: ("스트라우만", "서지컬 키트", "BLT 가이드키트"),
    13: ("스트라우만", "서지컬 키트", "BLX & TLX 가이드키트"),
    14: ("스트라우만", "서지컬 키트", "iGUIDE 키트"),
    16: ("스트라우만", "제품브로셔", "BLT"),
    17: ("스트라우만", "제품브로셔", "TL"),
    18: ("스트라우만", "제품브로셔", "BLX"),
    19: ("스트라우만", "제품브로셔", "TLX"),
    20: ("스트라우만", "제품브로셔", "BLC"),
    21: ("스트라우만", "제품브로셔", "Roxolid"),
    22: ("스트라우만", "제품브로셔", "SLActive"),
    24: ("스트라우만", "스탠딩 배너", "기업"),
    25: ("스트라우만", "스탠딩 배너", "SLActive"),
    26: ("스트라우만", "스탠딩 배너", "Roxolid"),
    28: ("스트라우만", None, "미니배너"),
    29: ("스트라우만", None, "테이블보"),
    30: ("스트라우만", None, "스탠바이미 모니터"),
    31: ("스트라우만", None, "캠퍼스 POP"),
    32: ("스트라우만", None, "카카오플친 POP"),
    33: ("스트라우만", None, "x4 더미 TL"),
    34: ("스트라우만", None, "x4 더미 BLT"),
    35: ("스트라우만", None, "x4 더미 BLX"),
    36: ("스트라우만", None, "방명록"),
    38: ("앤서지", "임플란트 모형", "Axiom BL PX/REG"),
    39: ("앤서지", "임플란트 모형", "Axiom X3"),
    40: ("앤서지", "임플란트 모형", "Axiom X3 메가모델"),
    42: ("앤서지", "서지컬 키트", "Axiom Surgical Kit"),
    43: ("앤서지", "서지컬 키트", "Integral Guide Kit"),
    45: ("앤서지", "제품브로셔", "Axiom 제품브로셔"),
    46: ("앤서지", "제품브로셔", "Axiom PX파노라마"),
    47: ("앤서지", "제품브로셔", "Axiom X3파노라마"),
    48: ("앤서지", "제품브로셔", "integral 파노라마"),
    49: ("앤서지", "제품브로셔", "회사 소개서"),
    51: ("앤서지", "기타", "테이블배너"),
    53: ("바이오머테리얼", "데모제품", "세라본"),
    54: ("바이오머테리얼", "데모제품", "제이슨 멤브레인"),
    55: ("바이오머테리얼", "데모제품", "엠도게인"),
    57: ("바이오머테리얼", "데모제품", "러버블/스푼/스포이드"),
    58: ("바이오머테리얼", "데모제품", "치아 모델"),
    60: ("바이오머테리얼", "제품브로셔", "세라본"),
    61: ("바이오머테리얼", "제품브로셔", "제이슨 멤브레인"),
    62: ("바이오머테리얼", "제품브로셔", "엠도게인"),
}


def normalize(text):
    for k, v in sorted (SYNONYMS. items(), key=lambda x:-len(x<a href="" class="citation-link" target="blank" style="vertical-align: super; font-size: 0.8em; margin-left:spx;">[0]</a>)):



def parse_sections(survey_text):
    BRAND_SECTIONS = {"스트라우만", "앤서지", "바이오머테리얼"}
    sections = {}
    current_brand = None
    current_key = None

    for raw_line in survey_text.splitlines():
        line = raw_line.strip()
        if not line:
            continue

        if line.endswith(":"):
            header = line[:-1].strip()
            if header in BRAND_SECTIONS:
                current_brand = header
                current_key = header
            else:
                current_key = f"{current_brand}_{header}" if current_brand else header

            if current_key not in sections:
                sections[current_key] = []
        else:
            if current_key is not None:
                sections[current_key].append(line)

    return sections


def exact_match(item, keyword):
    return item.strip().lower() == keyword.strip().lower()


def check_row(sections, brand, category, item_keyword):
    key = f"{brand}_{category}" if category else brand
    if key not in sections:
        return "0"
    for item in sections[key]:
        if exact_match(item, item_keyword):
            return "1"
    return "0"


def generate_output(survey_text):
    survey_text = normalize(survey_text)
    sections = parse_sections(survey_text)
    results = []
    for row in range(1, 63):
        if row in BLANK_ROWS:
            results.append("")
        elif row in ROW_DEFINITIONS:
            brand, category, item_keyword = ROW_DEFINITIONS[row]
            results.append(check_row(sections, brand, category, item_keyword))
        else:
            results.append("0")
    return "\n".join(results)


if __name__ == "__main__":
    with open("survey_input.txt", "r", encoding="utf-8") as f:
        survey = f.read()
    output = generate_output(survey)
    print(output)
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(output)
    print("output.txt saved")
