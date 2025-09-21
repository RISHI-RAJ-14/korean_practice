import streamlit as st
import random

# Configure page
st.set_page_config(page_title="Korean Writing Practice", layout="wide")

# Beginner-level sentence patterns
beginner_sentences = [
    ("나는 학교에 갑니다.", "I go to school."),
    ("나는 밥을 먹습니다.", "I eat rice."),
    ("너는 책을 읽습니다.", "You read a book."),
    ("우리는 친구를 만납니다.", "We meet a friend."),
    ("그는 버스를 탑니다.", "He takes the bus."),
    ("그녀는 커피를 마십니다.", "She drinks coffee."),
    ("나는 집에서 쉽니다.", "I rest at home."),
    ("나는 사과를 삽니다.", "I buy an apple."),
]

# Intermediate-level sentence patterns
intermediate_sentences = [
    ("나는 매일 아침 여섯 시에 일어나서 운동을 합니다.", "I wake up at six every morning and exercise."),
    ("나는 학교에 간 후에 도서관에서 책을 읽습니다.", "After going to school, I read books in the library."),
    ("그녀는 친구와 함께 시장에 가서 과일을 삽니다.", "She goes to the market with a friend and buys fruit."),
    ("나는 저녁을 먹고 나서 숙제를 합니다.", "I do my homework after eating dinner."),
    ("그는 주말에 영화를 보거나 산책을 합니다.", "On weekends, he either watches movies or takes a walk."),
    ("우리는 공원에서 만나서 함께 공부했습니다.", "We met at the park and studied together."),
]

# Advanced-level sentence patterns
advanced_sentences = [
    ("나는 어렸을 때부터 한국어에 관심이 있었기 때문에 지금 열심히 공부하고 있습니다.", 
     "Since I have been interested in Korean since I was young, I am studying hard now."),
    ("비가 많이 왔음에도 불구하고 사람들은 축제에 참여했습니다.", 
     "Despite the heavy rain, people participated in the festival."),
    ("그녀는 대학을 졸업한 후 외국에서 일할 기회를 찾고 있습니다.", 
     "After graduating from university, she is looking for opportunities to work abroad."),
    ("나는 한국 문화와 역사를 더 깊이 이해하기 위해 책을 많이 읽습니다.", 
     "I read many books to gain a deeper understanding of Korean culture and history."),
    ("우리가 함께 노력한다면 어떤 어려움도 극복할 수 있을 것입니다.", 
     "If we work together, we will be able to overcome any difficulty."),
]

def generate_paragraph(sentence_pairs, max_words=100):
    """Generate paragraphs from sentence pairs until reaching ~max_words (English side)."""
    korean_sentences = []
    english_sentences = []
    total_words = 0

    while total_words < max_words:
        ko, en = random.choice(sentence_pairs)
        korean_sentences.append(ko)
        english_sentences.append(en)
        total_words += len(en.split())

    return " ".join(korean_sentences), " ".join(english_sentences)

# Streamlit UI
st.title("✍️ Korean Writing Practice Generator")
st.write("Choose a difficulty level and click **Generate** to get a ~100-word paragraph in Korean with its English version.")

# Difficulty selector
difficulty = st.radio("Select Difficulty Level:", ["Beginner", "Intermediate", "Advanced"], horizontal=True)

if st.button("Generate"):
    if difficulty == "Beginner":
        korean_para, english_para = generate_paragraph(beginner_sentences, 100)
    elif difficulty == "Intermediate":
        korean_para, english_para = generate_paragraph(intermediate_sentences, 100)
    else:
        korean_para, english_para = generate_paragraph(advanced_sentences, 100)

    # Use columns to stretch across screen
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🇰🇷 Korean Paragraph")
        st.write(korean_para)

    with col2:
        st.subheader("🇺🇸 English Paragraph")
        st.write(english_para)
