# Proje Adı

Kitap Yönetim Sistemi..

## Kurulum

1. Projeyi klonlayın veya indirin.
2. Gerekli bağımlılıkları yükleyin: `pip install -r requirements.txt`
3. Uygulamayı çalıştırın: `python app.py`

## Kullanım

Aşağıdaki örneklerle API'yi kullanabilirsiniz:

-   Tüm kitapların listesini almak için: `GET http://localhost:5000/books`
-   Yeni bir kitap eklemek için: `POST http://localhost:5000/books`
-   Belirli bir kitabı almak için: `GET http://localhost:5000/books/{id}`
-   Belirli bir kitabı güncellemek için: `PUT http://localhost:5000/books/{id}`
-   Belirli bir kitabı silmek için: `DELETE http://localhost:5000/books/{id}`
