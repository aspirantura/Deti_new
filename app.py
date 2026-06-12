import streamlit as st

# ============================================================
# НАСТРОЙКА СТРАНИЦЫ
# ============================================================
st.set_page_config(
    page_title="Прогноз задержки ПМР у недоношенных (ЭКО)",
    layout="centered"
)

# ============================================================
# КАСТОМНЫЕ СТИЛИ
# ============================================================
st.markdown("""
<style>
    .main-header {
        text-align: center;
        padding: 1rem 0;
        border-bottom: 3px solid #4A90D9;
        margin-bottom: 2rem;
    }
    .main-header h1 {
        color: #2C3E50;
        font-size: 1.8rem;
    }
    .warning-box {
        background-color: #FFF3CD;
        border: 1px solid #FFECB5;
        border-left: 4px solid #FFC107;
        border-radius: 8px;
        padding: 1rem;
        margin-bottom: 1.5rem;
        font-size: 0.95rem;
        color: #664D03;
    }
    .result-box {
        padding: 1.5rem;
        border-radius: 12px;
        text-align: center;
        margin: 1.5rem 0;
        font-size: 1.1rem;
    }
    .result-high {
        background: linear-gradient(135deg, #FDEDEC, #F5B7B1);
        border: 2px solid #E74C3C;
        color: #922B21;
    }
    .result-moderate {
        background: linear-gradient(135deg, #FEF9E7, #F9E79F);
        border: 2px solid #F39C12;
        color: #7E5109;
    }
    .result-low {
        background: linear-gradient(135deg, #EAFAF1, #A9DFBF);
        border: 2px solid #27AE60;
        color: #1E8449;
    }
    .result-uncertain {
        background: linear-gradient(135deg, #F4F6F7, #D5DBDB);
        border: 2px solid #95A5A6;
        color: #515A5A;
    }
    .recommendations-card {
        background-color: #F8F9FA;
        padding: 1.2rem;
        border-radius: 10px;
        border-left: 4px solid #4A90D9;
        margin: 1rem 0;
        font-size: 0.9rem;
    }
    .recommendations-card-high {
        border-left-color: #E74C3C;
    }
    .recommendations-card-low {
        border-left-color: #27AE60;
    }
    .recommendations-card-uncertain {
        border-left-color: #F39C12;
    }
    .info-box {
        background-color: #E8F4FD;
        border: 1px solid #B8DAFF;
        border-radius: 8px;
        padding: 0.8rem;
        margin: 1rem 0;
        font-size: 0.85rem;
        color: #004085;
    }
</style>
""", unsafe_allow_html=True)

# ============================================================
# ЗАГОЛОВОК
# ============================================================
st.markdown("""
<div class="main-header">
    <h1>Прогноз формирования задержки психомоторного развития у недоношенных детей, зачатых методом ЭКО</h1>
</div>
""", unsafe_allow_html=True)

# ============================================================
# ВВОД ДАННЫХ
# ============================================================
st.markdown("### Введите данные ребёнка")

# --- Блок 1: Антропометрия ---
st.markdown("#### Антропометрические данные при рождении")

col1, col2, col3 = st.columns(3)

with col1:
    massa = st.selectbox(
        "Масса тела (г)",
        options=["Выберите...", "≤ 1500 г", "1501–2999 г", "≥ 3000 г"],
        index=0,
        help="Масса тела ребёнка при рождении"
    )

with col2:
    dlina = st.selectbox(
        "Длина тела (см)",
        options=["Выберите...", "≤ 43 см", "44 см", "≥ 45 см"],
        index=0,
        help="Длина тела ребёнка при рождении"
    )

with col3:
    okr_golovy = st.selectbox(
        "Окружность головы (см)",
        options=["Выберите...", "≤ 30 см", "31–32 см", "≥ 33 см"],
        index=0,
        help="Окружность головы ребёнка при рождении"
    )

st.markdown("")

# --- Блок 2: Заболевания неонатального периода ---
st.markdown("#### Заболевания неонатального периода")

col4, col5 = st.columns(2)

with col4:
    pnevmonia = st.radio(
        "Пневмония в неонатальном периоде",
        options=["Нет", "Да"],
        horizontal=True,
        help="Наличие пневмонии в неонатальном периоде"
    )
    
    anemiya = st.radio(
        "Ранняя анемия недоношенных",
        options=["Нет", "Да"],
        horizontal=True,
        help="Наличие ранней анемии недоношенных"
    )
    
    bld = st.radio(
        "Бронхолёгочная дисплазия (БЛД)",
        options=["Нет", "Да"],
        horizontal=True,
        help="Наличие бронхолёгочной дисплазии"
    )

with col5:
    ooo = st.radio(
        "Открытое овальное окно (ООО)",
        options=["Нет", "Да"],
        horizontal=True,
        help="Наличие открытого овального окна"
    )
    
    retinopatiya = st.radio(
        "Преретинопатия недоношенных",
        options=["Нет", "Да"],
        horizontal=True,
        help="Наличие преретинопатии недоношенных"
    )

st.markdown("")

# --- Блок 3: Акушерский анамнез ---
st.markdown("#### Акушерский анамнез")

mnogoplod = st.radio(
    "Многоплодная беременность",
    options=["Нет", "Да"],
    horizontal=True,
    help="Наличие многоплодной беременности"
)

# ============================================================
# РАСЧЁТ
# ============================================================
st.markdown("---")

if st.button("Рассчитать прогноз", type="primary", use_container_width=True):
    
    pk_sum = 0.0
    all_filled = True
    
    # --- 1. Масса при рождении ---
    if massa == "Выберите...":
        all_filled = False
    elif massa == "≤ 1500 г":
        pk_sum += 13.2
    elif massa == "≥ 3000 г":
        pk_sum += (-5.19)
    
    # --- 2. Длина тела ---
    if dlina == "Выберите...":
        all_filled = False
    elif dlina == "≤ 43 см":
        pk_sum += 10.19
    elif dlina == "≥ 45 см":
        pk_sum += (-3.33)
    
    # --- 3. Окружность головы ---
    if okr_golovy == "Выберите...":
        all_filled = False
    elif okr_golovy == "≤ 30 см":
        pk_sum += 10.64
    elif okr_golovy == "≥ 33 см":
        pk_sum += (-5.45)
    
    # --- 4. Пневмония ---
    if pnevmonia == "Да":
        pk_sum += 10.19
    else:
        pk_sum += (-0.50)
    
    # --- 5. Анемия ---
    if anemiya == "Да":
        pk_sum += 7.52
    else:
        pk_sum += (-2.77)
    
    # --- 6. БЛД ---
    if bld == "Да":
        pk_sum += 6.38
    else:
        pk_sum += (-0.76)
    
    # --- 7. ООО ---
    if ooo == "Да":
        pk_sum += 3.72
    else:
        pk_sum += (-6.05)
    
    # --- 8. Преретинопатия ---
    if retinopatiya == "Да":
        pk_sum += 3.65
    else:
        pk_sum += (-1.83)
    
    # --- 9. Недоношенность (автоматически) ---
    pk_sum += 2.41  # Преждевременные роды — всегда Да для недоношенных
    
    # --- 10. Многоплодность ---
    if mnogoplod == "Да":
        pk_sum += 2.41
    else:
        pk_sum += (-1.88)
    
    # --- Проверка заполненности ---
    if not all_filled:
        st.warning("Пожалуйста, заполните все поля антропометрических данных.")
    else:
        # ============================================================
        # РЕЗУЛЬТАТ
        # ============================================================
        
        # Определение категории
        if pk_sum >= 13:
            risk_class = "high"
            risk_label = "ВЫСОКИЙ РИСК"
            risk_text = f"Сумма прогностических коэффициентов = <b>{pk_sum:+.2f}</b> патов<br>Задержка ПМР к 1 году прогнозируется с вероятностью <b>95%</b>"
            css_class = "result-high"
        elif pk_sum >= 9:
            risk_class = "moderate"
            risk_label = "ПОВЫШЕННЫЙ РИСК"
            risk_text = f"Сумма прогностических коэффициентов = <b>{pk_sum:+.2f}</b> патов<br>Задержка ПМР к 1 году прогнозируется с вероятностью <b>90%</b>"
            css_class = "result-moderate"
        elif pk_sum <= -13:
            risk_class = "low"
            risk_label = "НИЗКИЙ РИСК"
            risk_text = f"Сумма прогностических коэффициентов = <b>{pk_sum:+.2f}</b> патов<br>Задержка ПМР к 1 году отрицается с вероятностью <b>95%</b>"
            css_class = "result-low"
        elif pk_sum <= -9:
            risk_class = "low"
            risk_label = "НИЗКИЙ РИСК"
            risk_text = f"Сумма прогностических коэффициентов = <b>{pk_sum:+.2f}</b> патов<br>Задержка ПМР к 1 году отрицается с вероятностью <b>90%</b>"
            css_class = "result-low"
        else:
            risk_class = "uncertain"
            risk_label = "ЗОНА НЕОПРЕДЕЛЁННОСТИ"
            risk_text = f"Сумма прогностических коэффициентов = <b>{pk_sum:+.2f}</b> патов<br>Прогноз неопределённый"
            css_class = "result-uncertain"
        
        st.markdown(f"""
        <div class="result-box {css_class}">
            <h2 style="margin:0 0 0.5rem 0;">{risk_label}</h2>
            <p style="margin:0;">{risk_text}</p>
        </div>
        """, unsafe_allow_html=True)
        
        
# ============================================================
# ПОДВАЛ С КОПИРАЙТОМ
# ============================================================
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #7F8C8D; font-size: 0.85rem; padding: 1.5rem 0 0.5rem 0;">
    <p style="margin: 0.5rem 0;">© 2025 Каширская Е.И., Проватар Н.П.</p>
    <p style="margin: 0.5rem 0; font-size: 0.8rem;">Все права защищены.</p>
</div>
""", unsafe_allow_html=True)
