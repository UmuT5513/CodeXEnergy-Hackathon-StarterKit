# Energy Hackathon Starter Kit

Bu proje, CodeXEnergy için hazırlanmış kapsamlı bir başlangıç paketidir (starter kit). Proje içerisinde veri setleri, keşifçi veri analizi (EDA) notebook'ları, bir API şablonu ve bir dashboard şablonu bulunmaktadır.

## Proje Yapısı

- **`datasets/`**: Projede kullanılabilecek 4 farklı ana veri seti kategorisini içerir:
  - `1_energy_consumption/`: Dünya enerji tüketim verileri.
  - `2_renewable_energy/`: Yenilenebilir enerji metrikleri.
  - `3_carbon_emission_and_sustainable_energy/`: Karbon (CO2) emisyonları ve küresel sürdürülebilir enerji verileri.
  - `4_smart_grid/`: Akıllı şebeke (smart grid) verileri.
- **`notebooks/`**: Veri setlerini incelemek ve analiz etmek için hazırlanmış Jupyter Notebook dosyalarını içerir (EDA).
- **`api_template/`**: Modelinizi veya veri servislerinizi sunmak için kullanabileceğiniz temel bir API şablonu (örneğin FastAPI veya Flask temel alınabilir).
- **`dashboard_template/`**: Verilerinizi görselleştirmek ve kullanıcıya sunmak için hazırlanmış bir Streamlit dashboard şablonu.
- **`requirements.txt`**: Projenin çalışması için gerekli olan Python kütüphanelerinin listesi.

## Kurulum ve Çalıştırma

### 1. Sanal Ortam Oluşturma
Proje dizininde bir terminal açın ve aşağıdaki komutu çalıştırarak bir sanal ortam oluşturun:
```bash
python -m venv .venv
.venv/Scripts/activate #.venv/bin/activate for linux
```


### 2. Gerekli Kütüphanelerin Kurulumu
Sanal ortamı seçtiğinizden emin olduktan sonra aşağıdaki komutu çalıştırarak gerekli bağımlılıkları yükleyin:
```bash
pip install -r requirements.txt
```

### 3. EDA (Keşifçi Veri Analizi) Notebook'larını İnceleme
`notebooks/` klasöründeki Jupyter Notebook'ları açarak veri setleri üzerinde yapılmış analizleri inceleyebilir ve kendi modellerinizi geliştirmeye başlayabilirsiniz.

### 4. API'yi Çalıştırma
API şablonunu başlatmak için `api_template/` klasörüne gidip ilgili Python dosyasını çalıştırın:
```bash
cd api_template
python app.py
```

### 5. Dashboard'u Çalıştırma
Görselleştirme arayüzünü (Streamlit) başlatmak için ana dizinde şu komutu çalıştırabilirsiniz:
```bash
.venv/Script/python.exe -m streamlit run dashboard_template/dashboard.py
```

![Dashboard](dashboard.png)

## Katkıda Bulunma
Bu şablonu kendi hackathon hedeflerinize göre özelleştirebilirsiniz. Veri analizi sonuçlarınıza göre dashboard'u güncelleyebilir ve oluşturduğunuz makine öğrenmesi modellerini API üzerinden dışa sunabilirsiniz.

Başarılar! 🌍⚡
