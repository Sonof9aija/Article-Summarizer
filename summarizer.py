import tkinter as tk
from newspaper import Article
from deep_translator import GoogleTranslator

root = tk.Tk()
root.title("Article Summarizer")

languages = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'assamese': 'as', 'aymara': 'ay', 'azerbaijani': 'az', 'bambara': 'bm', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bhojpuri': 'bho', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-CN', 'chinese (traditional)': 'zh-TW', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dhivehi': 'dv', 'dogri': 'doi', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'ewe': 'ee', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'guarani': 'gn', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'iw', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'ilocano': 'ilo', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'kinyarwanda': 'rw', 'konkani': 'gom', 'korean': 'ko', 'krio': 'kri', 'kurdish (kurmanji)': 'ku', 'kurdish (sorani)': 'ckb', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lingala': 'ln', 'lithuanian': 'lt', 'luganda': 'lg', 'luxembourgish': 'lb', 'macedonian': 'mk', 'maithili': 'mai', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'meiteilon (manipuri)': 'mni-Mtei', 'mizo': 'lus', 'mongolian': 'mn', 'myanmar': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia (oriya)': 'or', 'oromo': 'om', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'quechua': 'qu', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'sanskrit': 'sa', 'scots gaelic': 'gd', 'sepedi': 'nso', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'tatar': 'tt', 'telugu': 'te', 'thai': 'th', 'tigrinya': 'ti', 'tsonga': 'ts', 'turkish': 'tr', 'turkmen': 'tk', 'twi': 'ak', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}

def show_languages():
    new_window = tk.Toplevel(root)
    new_window.title("Languages")
    text = tk.Text(new_window, height=30, width=100)
    text.pack()
    text.insert('1.0',"Use one of the following in the language entry text box\n")
    for language, code in languages.items():
        text.insert(tk.END, f"{language} or {code}\n")

def summarize():
    url = url_entry.get()
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()

    article_name_text.delete('1.0', tk.END)
    summary_text.delete('1.0', tk.END)

    if language_entry.get():
        translated_title = GoogleTranslator(source='auto', target=language_entry.get().lower()).translate(text=article.title)
        translated_text = GoogleTranslator(source='auto', target=language_entry.get().lower()).translate(text=article.summary)
        article_name_text.insert('1.0', translated_title)
        summary_text.insert('1.0', translated_text)
    else:
        article_name_text.insert('1.0', article.title)
        summary_text.insert('1.0', article.summary)

article_name = tk.Label(root, text="Article Title:")
article_name.pack()
article_name_text = tk.Text(root, height=1, width=100)
article_name_text.pack()
summary = tk.Label(root, text="Article Summary:")
summary.pack()
summary_text = tk.Text(root, height=20, width=100)
summary_text.pack()


url_name = tk.Label(root, text="Article URL:")
url_name.pack()
url_entry = tk.Entry(root)
url_entry.pack()

language = tk.Label(root, text="Language for summary(leave empty for no translation):")
language.pack()
language_entry = tk.Entry(root)
language_entry.pack()




summarize_button = tk.Button(root, text="Summarize", command=summarize)
summarize_button.pack()
language_link = tk.Label(root, text="Click if translate not working", fg="blue", cursor="hand2")
language_link.pack()
language_link.bind("<Button-1>", lambda e: show_languages())
root.mainloop()
