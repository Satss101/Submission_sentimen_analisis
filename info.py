# Pandas untuk manipulasi dan analisis data
import pandas as pd  
# Menonaktifkan peringatan chaining
pd.options.mode.chained_assignment = None  
# NumPy untuk komputasi numerik
import numpy as np  
# Menyimpan ulasan dalam file CSV
import csv
import pandas as pd

# Mengimpor pustaka google_play_scraper untuk mengakses ulasan dan informasi aplikasi dari Google Play Store.
from google_play_scraper import reviews_all, Sort # type: ignore
# Pandas untuk manipulasi dan analisis data
import pandas as pd  
# Menonaktifkan peringatan chaining
pd.options.mode.chained_assignment = None  
# NumPy untuk komputasi numerik
import numpy as np  

seed = 0
# Mengatur seed untuk reproduktibilitas
np.random.seed(seed)  
# Matplotlib untuk visualisasi data
# import matplotlib.pyplot as plt  
# Seaborn untuk visualisasi data statistik, mengatur gaya visualisasi
# import seaborn as sns  

import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer

# Manipulasi data waktu dan tanggal
# import datetime as dt  
# Modul untuk bekerja dengan ekspresi reguler
import re  
# Berisi konstanta string, seperti tanda baca
import string  
# Tokenisasi teks
from nltk.tokenize import word_tokenize  
# Daftar kata-kata berhenti dalam teks
from nltk.corpus import stopwords  

# Stemming (penghilangan imbuhan kata) dalam bahasa Indonesia
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory 
# Menghapus kata-kata berhenti dalam bahasa Indonesia
# from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory  

# Membuat visualisasi berbentuk awan kata (word cloud) dari teks
from wordcloud import WordCloud  

# from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split,GridSearchCV
# from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import accuracy_score, precision_score
import nltk  # Import pustaka NLTK (Natural Language Toolkit).
nltk.download('punkt')  # Mengunduh dataset yang diperlukan untuk tokenisasi teks.
nltk.download('stopwords')  # Mengunduh dataset yang berisi daftar kata-kata berhenti (stop words) dalam berbagai bahasa.
nltk.download('punkt_tab')       # Untuk tokenizer

import csv
import requests
from io import StringIO