import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Energy Hackathon Dashboard", layout="wide")

st.title("🔋 CodeXEnergy Hackathon Dashboard")
st.markdown("Bu, `api_template/app.py` mantığına dayanarak oluşturulmuş basit bir Streamlit kontrol paneli (dashboard) şablonudur. Smart Grid veri setini kullanır.")

# Bu dosyadan verisetinin göreceli(relative) yolunu belirt
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "datasets", "4_smart_grid", "smart_grid_dataset.csv")

@st.cache_data
def load_data():
    # Başlangıçta verisetini yükle
    try:
        df = pd.read_csv(DATA_PATH)
        return df
    except Exception as e:
        st.error(f"Failed to load dataset: {e}")
        return pd.DataFrame()

df = load_data()

if not df.empty:
    st.subheader("Veri Seti Önizleme")
    # Kullanıcının limit belirleyebileceği bir alan (API'deki limit ve skip mantığına benzer)
    limit = st.slider("Gösterilecek satır sayısı", min_value=5, max_value=100, value=10)
    st.dataframe(df.head(limit))

    st.subheader("Özet İstatistikler (Summary)")
    # API'deki /data/summary ucuna benzer şekilde istatistikleri göster
    st.write(df.describe())
else:
    st.warning("Veri seti yüklenemediği için gösterilecek veri yok.")
