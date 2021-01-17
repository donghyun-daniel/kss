from collections import defaultdict
from typing import Any

from kss.base import Stats, ID, Const

top_500 = [
    '가', '간', '갈', '갉', '감', '갔', '갖', '같', '갚', '개', '걔', '걘', '거', '건', '걷', '걸', '검', '겪', '곤', '골', '곪', '곱', '괴',
    '구', '군', '굵', '굶', '굼', '굽', '궤', '귑', '귓', '규', '균', '긁', '긋', '기', '길', '긺', '깊', '까', '깎', '깐', '깖', '깜', '깠',
    '깨', '깬', '깼', '꺼', '꺾', '껐', '껴', '꼈', '꼬', '꼽', '꽂', '꽤', '꾸', '꾼', '꿇', '꿈', '꿔', '꿨', '꿰', '뀌', '끈', '끊', '끌',
    '끎', '끓', '끔', '끼', '낀', '낌', '나', '낚', '난', '날', '낡', '남', '났', '낮', '내', '낸', '냄', '냅', '냈', '넓', '넘', '넣', '녹',
    '논', '놀', '놂', '높', '놓', '놔', '놨', '누', '눈', '눕', '눠', '늘', '늙', '늚', '늦', '닦', '단', '닫', '달', '닮', '닳', '담', '답',
    '닿', '대', '댄', '댐', '댔', '던', '덜', '덞', '덥', '덮', '데', '덴', '뎀', '뎄', '돈', '돋', '돌', '돕', '돼', '됐', '되', '된', '됨',
    '두', '둔', '둠', '뒀', '든', '듣', '들', '듦', '듬', '딛', '딪', '따', '딴', '땀', '땄', '땋', '땠', '떠', '떨', '떴', '떼', '뗀', '뗌',
    '뛰', '뜀', '뜨', '뜯', '뜸', '띄', '띈', '띔', '띠', '띤', '막', '만', '많', '말', '맑', '맒', '맞', '맡', '매', '맨', '맴', '맵', '맸',
    '맺', '먹', '멀', '멂', '메', '멘', '멨', '몬', '몰', '몲', '묵', '묶', '묻', '물', '묽', '묾', '뭍', '뭘', '민', '믿', '밀', '밂', '밈',
    '밉', '박', '받', '밝', '밟', '배', '밴', '뱀', '뱄', '뱉', '번', '벌', '벎', '벗', '베', '벤', '보', '볶', '본', '봄', '봤', '봬', '뵀',
    '뵈', '뵌', '분', '붇', '불', '붉', '붊', '붓', '붙', '비', '빈', '빌', '빎', '빔', '빚', '빤', '빨', '빪', '빻', '빼', '뺀', '뺌', '뺐',
    '뻗', '뻤', '뼜', '뿜', '삔', '삠', '사', '산', '살', '삵', '삶', '삼', '샀', '새', '샌', '샘', '샛', '샜', '서', '섞', '선', '섰', '세',
    '셈', '셌', '속', '솎', '솟', '숨', '쉬', '쉰', '쉼', '쉽', '시', '식', '싣', '싫', '싶', '싸', '싼', '쌈', '쌌', '쌓', '쌔', '쌨', '써',
    '썩', '썰', '썲', '썼', '쎄', '쏘', '쏜', '쏟', '쏨', '쏴', '쐈', '쑤', '쑨', '쓰', '쓴', '쓸', '쓺', '씀', '씌', '씐', '씹', '안', '앉',
    '않', '알', '앎', '앓', '암', '약', '얇', '얕', '얘', '얜', '언', '얹', '얻', '얼', '없', '엎', '엮', '연', '열', '엶', '옅', '옌', '옛',
    '오', '온', '옭', '옮', '옳', '옴', '와', '왔', '왜', '운', '울', '읊', '일', '읽', '잃', '입', '있', '잊', '자', '작', '잔', '잡', '잤',
    '잦', '재', '잰', '잼', '쟀', '쟤', '쟨', '적', '전', '절', '젊', '접', '젓', '져', '졌', '존', '졸', '졺', '좁', '좇', '좋', '주', '죽',
    '준', '줌', '줍', '줘', '줬', '쥐', '쥠', '지', '진', '질', '집', '짓', '짖', '짙', '짜', '짧', '짰', '째', '짼', '쨌', '쩐', '쩔', '쪄',
    '쪘', '쫀', '쬐', '쬠', '찌', '찍', '찐', '찜', '찝', '찢', '차', '찬', '참', '찼', '찾', '채', '챈', '챘', '쳐', '쳤', '추', '춘', '춤',
    '춥', '춰', '췄', '치', '친', '침', '캐', '캠', '캤', '커', '컸', '켜', '켠', '켬', '켰', '크', '큼', '키', '킨', '킴', '타', '탄', '탐',
    '탔', '터', '턺', '텁', '텨', '튀', '튄', '튐', '트', '튼', '틂', '틈', '파', '팔', '팜', '팠', '패', '팼', '퍼', '펌', '펐', '펴', '편',
    '폄', '폈', '푼', '품', '피', '핀', '핌', '하', '핥', '함', '해', '했', '헌', '휘', '희',
]

da = [
    '간', '같', '걔', '거', '건', '검', '곤', '곱',
    '구', '군', '굵', '길', '깊', '깐', '깠',
    '깬', '깼', '껐', '꼈', '꾼', '꿨',
    '끼', '낀', '난', '낡', '났', '낮', '낸', '냈', '넓',
    '논', '높', '놨', '눈', '늙', '늦', '단', '답',
    '닿', '댄', '댔', '덥', '덴', '뎄', '돈', '돼', '됐', '되', '된',
    '둔', '뒀', '딴', '땄', '땠', '떴', '뗀',
    '띈', '띤', '많', '맑', '맨', '맵', '맸',
    '멀', '멘', '멨', '몬', '묽', '민',
    '밉', '밝', '밴', '뱄', '번', '벤', '본', '봤', '뵀',
    '뵌', '분', '붉', '비', '빈', '빤', '뺀', '뺐',
    '뻤', '뼜', '삔', '산', '샀', '샌', '샜', '선', '섰',
    '셌', '쉰', '쉼', '쉽', '시', '싶', '싼', '쌈', '쌌', '쌔', '쌨', '써',
    '썼', '쏜', '쐈', '쑨', '쓴',
    '않', '얇', '얕', '얘', '언', '없', '연', '옅',
    '옳', '왔', '운', '있', '작', '잔', '잤',
    '잦', '잰', '쟀', '쟤', '적', '전', '젊', '졌', '존', '좁', '좋',
    '준', '줍', '줬', '진', '짙', '짜', '짧', '짰', '짼', '쨌', '쩐',
    '쪘', '쫀', '찐', '차', '찬', '찼', '챈', '챘', '쳤', '춘',
    '춥', '췄', '친', '캤', '컸', '켠', '켰', '크', '킨', '탄',
    '탔', '튀', '튄', '트', '튼', '팠', '팼', '펐', '편',
    '폈', '푼', '핀', '했', '희',
]

yo = [
    '가', '감', '개', '걔', '걘', '괴',
    '까',
    '깨', '껴', '꿈', '꿔', '꿰',
    '끔', '낌', '나', '남', '내', '냄',
    '놂', '놔', '눠', '늚',
    '대', '댐', '데', '돼', '되', '됨',
    '둠', '듦', '듬', '따', '땀', '떠', '떼',
    '뜀', '뜸', '띔', '매',
    '메',
    '배', '베', '봬',
    '뵈', '빎', '빔', '빪', '뺌',
    '삠', '사', '삶', '삼', '새', '서', '세',
    '셈', '싸', '쌈', '쌔', '써',
    '썲', '쎄', '쏨', '쏴', '쓺', '씀',
    '앎', '암', '얘', '얜', '엶',
    '옮', '옴', '와', '왜', '자',
    '재', '잼', '쟤', '쟨', '젊', '져', '졺',
    '줌', '줘', '짜', '째', '쪄',
    '쬠', '찜', '차', '채', '쳐', '춤',
    '춰', '캐', '커', '켜', '켬', '킴', '타', '탐',
    '터', '텨', '튐', '틈', '팜', '패', '퍼', '펌', '펴',
    '폄', '품', '핌', '함', '해',
]

jyo = [
    '가', '갉', '갔', '갖', '같', '갚', '개', '걔', '걷', '걸', '검', '겪', '골', '곪', '곱', '괴',
    '굵', '굶', '굼', '굽', '긁', '긋', '길', '깊', '깎', '깠',
    '깨', '깼', '꺾', '껐', '꼈', '꼽', '꽂', '꾸', '꿇', '꿨', '꿰', '뀌', '끊', '끌',
    '끓', '끼', '낚', '날', '낡', '남', '났', '낮', '내', '냈', '넓', '넘', '넣', '녹',
    '놀', '높', '놓', '놨', '누', '눕', '늙', '늦', '닦', '닫', '달', '닮', '닳', '답',
    '닿', '대', '댔', '덜', '덥', '덮', '데', '뎄', '돋', '돌', '돕', '돼', '됐', '되',
    '두', '뒀', '듣', '들', '딛', '딪', '따', '땄', '땋', '땠', '떨', '떴', '떼',
    '뛰', '뜨', '뜯', '띄', '띠', '막', '많', '말', '맑', '맞', '맡', '매', '맵', '맸',
    '맺', '먹', '멀', '메', '멨', '몰', '묵', '묶', '묻', '묽', '뭍', '믿', '밀',
    '밉', '박', '받', '밝', '밟', '배', '뱄', '뱉', '벌', '벗', '베', '보', '볶', '봤', '봬', '뵀',
    '뵈', '붇', '불', '붉', '붓', '붙', '비', '빌', '빚', '빨', '빻', '빼', '뺐',
    '뻗', '뻤', '뼜', '사', '살', '삵', '샀', '새', '샌', '샛', '샜', '서', '섞', '섰', '세',
    '셌', '속', '솎', '솟', '숨', '쉬', '쉽', '시', '식', '싣', '싫', '싶', '싸', '쌌', '쌓', '쌔', '쌨', '써',
    '썩', '썰', '썼', '쎄', '쏘', '쏟', '쏴', '쐈', '쑤', '쓰', '쓸', '씌', '씹', '앉',
    '않', '알', '앓', '약', '얇', '얕', '얘', '얹', '얻', '얼', '없', '엎', '엮', '열', '옅', '옛',
    '오', '온', '옭', '옮', '옳', '와', '왔', '울', '읊', '일', '읽', '잃', '입', '있', '잊', '자', '작', '잡', '잤',
    '잦', '재', '잰', '쟀', '쟤', '적', '절', '젊', '접', '젓', '졌', '졸', '좁', '좇', '좋', '주', '죽',
    '줍', '줬', '쥐', '지', '질', '집', '짓', '짖', '짙', '짜', '짧', '짰', '째', '쨌', '쩔',
    '쪘', '쬐', '찌', '찍', '찐', '찝', '찢', '차', '찼', '찾', '채', '챘', '쳐', '쳤', '추',
    '춥', '춰', '췄', '치', '캐', '캤', '커', '컸', '켜', '켠', '켰', '크', '키', '타',
    '탔', '터', '튀', '트', '파', '팔', '팠', '패', '팼', '펐', '펴',
    '폈', '피', '하', '핥', '했', '휘', '희',
]

before = {
    # 조사
    "이", "가", "에서", "은", "는", "을", "를", "도", "에", "게", "께", "한테", "로", "써",
    "와", "과", "랑", "까지", "부터", "뿐", "만", "따라", "토록", "도록", "든지", "던지", "란",
    "만큼", "만치", "때",

    # 부사
    "너무", "잘", "못", "빨리", "매우", "몹시", "별로", "아까", "내일", "일찍", "금방",
    "이미", "이리", "저리", "아니", "과연", "설마", "제발", "정말", "결코", "가득", "히",

    # 대명사
    "나", "저", "우리", "저희", "너", "너희", "당신", "그대", "그", "그녀", "분", "놈", "거", "것",
    "여기", "저기", "쪽", "곳", "님"
}


def create_dict(d, default: Any = 0):
    return defaultdict(lambda: default, d)


# Pattern Mapping Table for Sentence Splitter
Table = create_dict({
    Stats.DA:
    # EC, EF 주의 !!
        create_dict({
            "갔": ID.PREV,
            "간": ID.PREV,
            "겠": ID.PREV,
            "겼": ID.PREV,
            "같": ID.PREV,
            "놨": ID.PREV,
            "녔": ID.PREV,
            "니": ID.PREV,
            "논": ID.PREV,
            "낸": ID.PREV,
            "냈": ID.PREV,
            "뒀": ID.PREV,
            "때": ID.PREV,
            "랐": ID.PREV,
            "럽": ID.PREV,
            "렵": ID.PREV,
            "렸": ID.PREV,
            "뤘": ID.PREV,
            "몄": ID.PREV,
            "밌": ID.PREV,
            "볐": ID.PREV,
            "볍": ID.PREV,
            "봤": ID.PREV,
            "섰": ID.PREV,
            "샜": ID.PREV,
            "셨": ID.PREV,
            "싼": ID.PREV,
            "싸": ID.PREV,
            "않": ID.PREV,
            "았": ID.PREV,
            "없": ID.PREV,
            "었": ID.PREV,
            "였": ID.PREV,
            "온": ID.PREV,
            "웠": ID.PREV,
            "이": ID.PREV,
            "인": ID.PREV,
            "있": ID.PREV,
            "진": ID.PREV,
            "졌": ID.PREV,
            "쳤": ID.PREV,
            "췄": ID.PREV,
            "챘": ID.PREV,
            "켰": ID.PREV,
            "켠": ID.PREV,
            "팠": ID.PREV,
            "펐": ID.PREV,
            "폈": ID.PREV,
            "했": ID.PREV,
            "혔": ID.PREV,
            "한": ID.NEXT,
            "가": ID.NEXT,
            "고": ID.NEXT | ID.NEXT2,
            "는": ID.NEXT | ID.NEXT2,
            "라": ID.NEXT,
            "시": ID.NEXT,
            "등": ID.NEXT,
            "던": ID.NEXT,
            "든": ID.NEXT,
            "지": ID.NEXT1 | ID.NEXT2,
            "를": ID.NEXT,
            "운": ID.NEXT,  # ~ 다운
            "만": ID.NEXT,
            "며": ID.NEXT | ID.NEXT2,
            "면": ID.NEXT | ID.NEXT1 | ID.NEXT2,
            "서": ID.NEXT2,
            "싶": ID.PREV | ID.NEXT,
            "죠": ID.NEXT,
            "죵": ID.NEXT,
            "쥬": ID.NEXT,
            "하": ID.NEXT1,
            "해": ID.NEXT1,
            "도": ID.NEXT2,
            "": ID.NONE
        }),
    Stats.YO:
        create_dict({
            "겨": ID.PREV,
            "거": ID.PREV,
            "구": ID.PREV,
            "군": ID.PREV,
            "걸": ID.PREV,
            "까": ID.PREV,
            "께": ID.PREV,
            "껴": ID.PREV,
            "네": ID.PREV,
            "나": ID.PREV,
            "니": ID.PREV,
            "데": ID.PREV,
            "든": ID.PREV,
            "려": ID.PREV,
            "서": ID.PREV,
            "세": ID.PREV,
            "아": ID.PREV,
            "어": ID.PREV,
            "워": ID.PREV,
            "에": ID.PREV,
            "예": ID.PREV,
            "을": ID.PREV,
            "져": ID.PREV,
            "줘": ID.PREV,
            "지": ID.PREV,
            "춰": ID.PREV,
            "해": ID.PREV,
            "고": ID.NEXT2,
            "는": ID.NEXT,
            "라": ID.NEXT1,
            "등": ID.NEXT,
            "를": ID.NEXT,
            "즘": ID.NEXT,
            "소": ID.NEXT,
            "며": ID.NEXT2,
            "면": ID.PREV | ID.NEXT2,
            "하": ID.NEXT1,
            "": ID.NONE
        }),
    Stats.JYO:
        create_dict({
            "거": ID.PREV,
            "가": ID.PREV,
            "갔": ID.PREV,
            "겠": ID.PREV,
            "같": ID.PREV,
            "놨": ID.PREV,
            "녔": ID.PREV,
            "냈": ID.PREV,
            "니": ID.PREV,
            "뒀": ID.PREV,
            "았": ID.PREV,
            "르": ID.PREV,
            "랐": ID.PREV,
            "럽": ID.PREV,
            "렵": ID.PREV,
            "렸": ID.PREV,
            "맞": ID.PREV,
            "몄": ID.PREV,
            "밌": ID.PREV,
            "볐": ID.PREV,
            "볍": ID.PREV,
            "봤": ID.PREV,
            "서": ID.PREV,
            "섰": ID.PREV,
            "셨": ID.PREV,
            "샜": ID.PREV,
            "않": ID.PREV,
            "없": ID.PREV,
            "었": ID.PREV,
            "였": ID.PREV,
            "이": ID.PREV,
            "졌": ID.PREV,
            "쳤": ID.PREV,
            "챘": ID.PREV,
            "켰": ID.PREV,
            "팠": ID.PREV,
            "폈": ID.PREV,
            "하": ID.PREV,
            "했": ID.PREV,
            "혔": ID.PREV,
            "고": ID.PREV | ID.NEXT2,
            "는": ID.NEXT,
            "등": ID.NEXT,
            "라": ID.NEXT1,
            "를": ID.NEXT,
            "며": ID.NEXT2,
            "면": ID.PREV | ID.NEXT2,
            "": ID.NONE,
        }),
    Stats.SB:
    # https://www.yeoju.go.kr/history/jsp/Theme/Save_View.jsp?BC_ID=d0400
        create_dict({
            "것": ID.PREV,
            "가": ID.PREV,
            "까": ID.PREV,
            "거": ID.PREV,
            "게": ID.PREV,
            "걸": ID.PREV,
            "껄": ID.PREV,
            "나": ID.PREV,
            "니": ID.PREV,
            "네": ID.PREV,
            "다": ID.PREV,
            "쎄": ID.PREV,
            "래": ID.PREV,
            "데": ID.PREV,
            "지": ID.PREV,
            "든": ID.PREV,
            "덩": ID.PREV,
            "등": ID.PREV,
            "랴": ID.PREV,
            "마": ID.PREV,
            "봐": ID.PREV,
            "서": ID.PREV,
            "아": ID.PREV,
            "어": ID.PREV,
            "오": ID.PREV,
            "요": ID.PREV,
            "을": ID.PREV,
            "자": ID.PREV,
            "죠": ID.PREV,
            "고": ID.NEXT2,
            "는": ID.NEXT,
            "라": ID.PREV | ID.NEXT,
            "며": ID.NEXT2,
            "면": ID.NEXT2,
            "하": ID.NEXT1,
            "": ID.NONE
        }),
    Stats.COMMON:
        create_dict({
            "ㄱ": ID.CONT,
            "ㄴ": ID.CONT,
            "ㄷ": ID.CONT,
            "ㄹ": ID.CONT,
            "ㅁ": ID.CONT,
            "ㅂ": ID.CONT,
            "ㅅ": ID.CONT,
            "ㅇ": ID.CONT,
            "ㅈ": ID.CONT,
            "ㅊ": ID.CONT,
            "ㅋ": ID.CONT,
            "ㅌ": ID.CONT,
            "ㅍ": ID.CONT,
            "ㅎ": ID.CONT,
            "ㅏ": ID.CONT,
            "ㅑ": ID.CONT,
            "ㅓ": ID.CONT,
            "ㅕ": ID.CONT,
            "ㅗ": ID.CONT,
            "ㅛ": ID.CONT,
            "ㅜ": ID.CONT,
            "ㅠ": ID.CONT,
            "ㅡ": ID.CONT,
            "ㅣ": ID.CONT,
            "^": ID.CONT,
            ";": ID.CONT,
            ".": ID.CONT,
            "?": ID.CONT,
            "!": ID.CONT,
            "~": ID.CONT,
            "…": ID.CONT,
            ",": ID.CONT,
            "": ID.NONE,
        })
},
    default=create_dict({})
)

post_processing_da = list(set([f"{x} {_}다 " for _ in da for x in before]))
post_processing_yo = list(set([f"{x} {_}요 " for _ in yo for x in before]))
post_processing_jyo = list(set([f"{x} {_}죠 " for _ in jyo for x in before]))
