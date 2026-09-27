# Machinery Django Project

Ye aapki `machinery-updated-html-12-1-19` HTML template ko Django project mein convert kiya gaya hai.
Sare 27 pages Django templates ban chuke hain, header/footer includes mein hain, aur css/js/images
static files ke through load ho rahe hain.

## Project Structure

```
manage.py
config/                     -> Django settings/urls (project config)
    settings.py
    urls.py
templates/                   -> sare pages/templates yahan main directory mein hain (apps ke andar nahi)
    base.html                 -> common <head>, header/footer include, scripts
    includes/
        header.html               -> default header (25 pages)
        header_home.html           -> index.html ka style-two header
        header_v3.html             -> index2.html ka style-three header
        footer.html                -> default footer
        footer_v3.html              -> index2.html ka footer variant
    pages/
        about.html, contact.html, shop.html, ... (27 templates)
apps/
    website/                 -> aapka Django "app" (sirf logic yahan hai)
        views.py             -> har page ke liye ek TemplateView
        urls.py              -> har page ka URL route
        static/website/
            css/, js/, images/, fonts/, plugins/   -> original static assets (as-is)
```

`config/settings.py` mein `TEMPLATES[0]['DIRS'] = [BASE_DIR / 'templates']` set kiya gaya hai,
isliye Django root-level `templates/` folder ko directly dhoondh leta hai — koi app-level
namespacing (`website/pages/...`) ki zaroorat nahi.

## Kaise Chalayen

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver
```

Phir browser mein `http://127.0.0.1:8000/` khol dein.

## URL -> Page Mapping

| URL                              | Template                        |
|-----------------------------------|----------------------------------|
| `/`                                | index.html (home)               |
| `/index2/`                         | index2.html (alt home)          |
| `/about/`                          | about.html                      |
| `/contact/`, `/contact-2/`         | contact.html, contact-2.html    |
| `/shop/`, `/shop-single/`          | shop.html, shop-single.html     |
| `/shoping-cart/`, `/checkout/`     | cart & checkout                 |
| ... baki sab pages same tarah se, file name se milta URL slug |

Sab internal links (`href="about.html"` waghera) ko Django `{% url %}` tag mein convert kar diya
gaya hai, isliye navigation menu properly kaam karega.

## Notes

- Ye pure static/presentational pages hain — koi database model ya form-processing backend
  nahi banaya gaya (jaise contact form abhi bhi `sendemail.php` ki taraf point kar raha hai,
  usay chahen to aap Django view/form se replace kar sakte hain).
- `python manage.py check` aur sare 27 pages ka live HTTP test (200 OK) locally verify kiya
  ja chuka hai.
- `apps.py` mein app ka label `website` rakha gaya hai taake app_name namespace clean rahe.
