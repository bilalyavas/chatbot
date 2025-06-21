from langchain_ollama import OllamaLLM ##imprort icin
from langchain_core.prompts import ChatPromptTemplate
model = OllamaLLM(model="gemma3") ##bu siniftan bir ornek aliyoruz. modelimiz hazir.
template = """Question : {question} 
Answer : Lets think step by step.""" ## bir template yani kalip olusturduk, burda template bir degiskendir. 
## {} bir degisken yazmak istedigimi belirtiyor. boylece girdi kalibimizi olusturduk. 
## simdi bu kalibi modele vermek icin bir prompt olusturalim. 
## Bunun icin langchain icindeki ChatPromttemplate sinifini kullanacagiz
prompt = ChatPromptTemplate.from_template(template) 
##template variable ini kullarak model icin bir prompt olursturduk.
##bunun icin from_template metodunu kullandik.
##simdi yapmamiz gereken modele promptu vermek.
##model promptu alacak ve bir cikti uretecek. Bunu langchain ile yapmak icin bir boru hatti kullanacagiz
##bunun icin chain adinda bir degisken kullaniyoruz. daha sonra prompt degiskenini kullaniyoruz
## ve bir pipe | operatoru ile modeli bagliyoruz.(promptu modele vermek istedigimizi soyluyorum.)
chain = prompt | model ##burda pipe operatoru kullanarak promptu modele bagladik.
##tamaam, pipeline miz oluşturuldu.
##simde modeli calistirabilmemiz icin klik yapmamiz gereken envoke methodunu cagiriyoruz.
response = chain.invoke({"question": "Turkce bir fikra yaz"}) ##burda invoke metodunu cagiriyoruz.
##Cevabi response degiskenine atiyoruz. chainin calismasi icin invoke metodunu cagiriyoruz.
## curly barackets icindeki question degiskeni, promptta tanimladigimiz degiskenle ayni. Bu question
##degiskenine gelecek degeri yazdik. cevabi gormek icib bu degiskeni print komutu ile yazdiralim.
print(response) ##cevabi yazdiriyoruz. bunun icin command line da python my-chatbot.py komutunu calistiriyoruz.
## bu komut calistiginda, modelimiz soruyu alacak ve cevabi uretecek.(python my-chatbot.py)
##Langchain ile modelimizi calistirdik.
##Hadi simdi Streamlit ile chatbot umuzun fronthandini yapalim.
##Streamlit ile chatbotumuzu yapalim. streamlit yapay zeka uygulamalari gelistirmek icin harika bir kutuphane. 
##Simdi bu kutuphaneyi (streamlit) import edelim ve chatbotumuzu yapalim.
import streamlit as st ##streamlit kutuphanesini import ediyoruz.
##modelimiz ile promtumuz ayni olacak. yani model ve promptu ayni isimdeki degiskenlere atayalim.
##Oncelikle uygulamamiza bir isim verelim.
st.title("Chatbot with Ollama") ##streamlit ile uygulamamiza bir baslik veriyoruz. 
##bunun icin title metodunu kullaniyoruz. Simdi uygulamamizi calistiralim ve basligi gorelim.
##Streamlit uygulamamizi calistirmak icin terminalde streamlit run my-chatbot.py komutunu calistiriyoruz.
##bu komutla beraber uygulamamiz calisacak ve tarayicimizda acilacak.Browserda yani.   
# Simdi bir input alanı ekleyelim.user_input degiskeni ile input alanını tanımlayalım.
user_input = st.text_input("Type a question:") ##streamlit ile bir input alanı ekliyoruz. 
##kullanicidan input almak icin text_input metodunu kullaniyoruz.
##bu metodun icine bir metin yaziyoruz. bu metin input alaninin ustunde gorunecek.
## Simdi kullanici   bir input girdiginde olacaklari yazalim. if ile.
if user_input:  ##eğer kullanici input girdiyse yani true ise
    ##burda kullanicinin girdigi inputu aliyoruz ve chaini invoke ediyoruz.
    response = chain.invoke({"question": user_input})  ##girdi olarak kullanicinin girdisini modele veriyoruz.
    ##chaini invoke ediyoruz. yani modeli calistiriyoruz. modelin cevabini response degiskenine atiyoruz.
    st.write("Response:",  response)  ##cevabi streamlit ile yazdiriyoruz. yani kullaniciya gosteriyoruz.
    ##tamaam chatbotumuz hazir. Simdi browserda sonucu gorelim. Browserda sayfamizi yenileyelim.
    ##ve input alanina bir soru yazalim. ornegin "Turkce bir fikra yaz" yazalim.




