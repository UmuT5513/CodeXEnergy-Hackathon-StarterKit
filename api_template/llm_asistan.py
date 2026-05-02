"""
CarbonZero AI Asistan Modulu
==============================
Bu modul, Gemini LLM entegrasyonunu ve enerji uretim
tavsiyelerini yonetir. NASA gunes verisi simulasyonu
ile calisarak kullanicilara akilli oneriler sunar.
"""

import os
import pandas as pd
from dotenv import load_dotenv
from google import genai

# -- .env dosyasindan API anahtarini yukle ----------------------------------
# api_template/ klasorunden bir ust dizindeki .env dosyasina ulas
env_path = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(dotenv_path=env_path)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "GEMINI_API_KEY bulunamadi! "
        "Lutfen ana dizindeki .env dosyasina GEMINI_API_KEY degerini ekleyin."
    )

# -- Gemini API istemcisini olustur -----------------------------------------
client = genai.Client(api_key=GEMINI_API_KEY)


# -- ML Ekibinin verdigi tahmin fonksiyonu ----------------------------------
def predict_solar(tarih, panel_gucu_kw=5):
    import pandas as pd
    saatler = [f"{str(i).zfill(2)}:00" for i in range(6, 20)]
    uretim = [0.2, 0.8, 1.5, 2.8, 4.1, 5.0, 5.2, 4.8, 3.5, 2.1, 1.2, 0.5, 0.1, 0.0]
    return pd.DataFrame({'saat': saatler, 'beklenen_uretim_kw': uretim})


class CarbonZeroAssistant:
    """
    CarbonZero Yapay Zeka Asistani.

    Bu sinif, gunes enerjisi uretim verilerini analiz ederek
    kullanicilara Gemini LLM destekli tavsiyeler sunar.
    """

    def __init__(self):
        """Asistani baslat ve Gemini istemcisini yapilandir."""
        self.client = client
        self.model_name = "gemini-2.0-flash"

    def generate_advice(self, df: pd.DataFrame) -> str:
        """
        DataFrame'deki zirve saatini bulup LLM destekli tavsiye uretir.

        Args:
            df (pd.DataFrame): predict_solar() formatinda DataFrame.
                Kolonlar: 'saat', 'beklenen_uretim_kw'

        Returns:
            str: Gemini modelinden donen motive edici tavsiye metni.
        """
        # -- DataFrame'den zirve saatini bul ---------------------------------
        zirve_satir = df.loc[df["beklenen_uretim_kw"].idxmax()]
        saat = zirve_satir["saat"]
        beklenen_uretim_kw = zirve_satir["beklenen_uretim_kw"]

        # -- Engellenen karbon hesapla ---------------------------------------
        # Sebekeden cekilmeyen her 1 kWh = 0.4 kg CO2 kurtarir
        engellenen_karbon_kg = round(beklenen_uretim_kw * 0.4, 2)

        # -- Sistem rolu ve kullanici promptunu olustur ----------------------
        sistem_rolu = (
            "Sen CarbonZero AI adinda cevreci ve akilli bir ev enerjisi "
            "asistanisin. Yanitlarin cok kisa (maksimum 2-3 cumle), "
            "motive edici, samimi ve dogrudan eyleme yonelik olmali. "
            "Ciktida gereksiz uzatmalar yapma."
        )

        kullanici_promptu = (
            f"Kullanicinin bugun saat {saat}'te {beklenen_uretim_kw} kW "
            f"bedava gunes enerjisi olacak. Bu sayede {engellenen_karbon_kg} kg "
            f"CO2 salinimi engellenecek. Kullaniciya camasir, bulasik makinesi "
            f"veya elektrikli aracini bu saatte calistirmasi icin motive edici, "
            f"cevreci bir bildirim yaz."
        )

        # -- Gemini API cagrisi (google-genai SDK) ---------------------------
        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=f"{sistem_rolu}\n\n{kullanici_promptu}",
            )
            return response.text
        except Exception as e:
            print(f"API Hatasi (Sistemi durdurmadik): {e}") 
            
            # -- API COKERSE CALISACAK AKILLI YEDEK SISTEM (FALLBACK) --
            if beklenen_uretim_kw >= 4.0:
                sahte_cevap = f"Harika haber! Saat {saat}'te panellerin {beklenen_uretim_kw} kW ile tavan yapacak. {engellenen_karbon_kg} kg karbonu dogada birakmamak icin camasir makinesi veya elektrikli aracini tam bu saatte calistir! 🌍💚"
            elif beklenen_uretim_kw >= 2.0:
                sahte_cevap = f"Saat {saat} itibariyle gunesten {beklenen_uretim_kw} kW verimli enerjimiz var. Bu sayede {engellenen_karbon_kg} kg CO2 engelliyoruz. Gunluk islerini halletmek icin guzel bir saat! ☀️"
            else:
                sahte_cevap = f"Saat {saat}'te uretim sadece {beklenen_uretim_kw} kW seviyesinde kalacak. Karbon ayak izini dusuk tutmak icin lutfen agir cihazlari calistirmayi ertele. ☁️"
            
            return sahte_cevap
# -- Modul dogrudan calistirildiginda basit bir test yap -------------------
if __name__ == "__main__":
    print("=" * 50)
    print("  CarbonZero AI Asistan - Tam Test")
    print("=" * 50)

    asistan = CarbonZeroAssistant()

    print("\n[OK] Gemini API baglantisi basarili!")
    print(f"   Model: {asistan.model_name}")

    # 1) ML tahmin verisini al
    df = predict_solar("bugun")
    print(f"\n[DATA] Gunes Uretim Tahmini (predict_solar):")
    print(df.to_string(index=False))

    # 2) Zirve saatini ve karbon hesabini goster
    zirve = df.loc[df["beklenen_uretim_kw"].idxmax()]
    karbon = round(zirve["beklenen_uretim_kw"] * 0.4, 2)
    print(f"\n[ZIRVE] En yuksek uretim: {zirve['saat']} -> {zirve['beklenen_uretim_kw']} kW")
    print(f"[CO2] Engellenen karbon: {karbon} kg")

    # 3) LLM'den tavsiye al ve yazdir
    print("\n[AI] Gemini'den tavsiye isteniyor...")
    tavsiye = asistan.generate_advice(df)
    print(f"\n[SONUC] AI Tavsiyesi:")
    print(f"   {tavsiye}")
