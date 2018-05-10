import requests
import os


def translate_it(news_language, result_language, news_file, news_result):
    """
    YANDEX translation plugin

    docs: https://tech.yandex.ru/translate/doc/dg/reference/translate-docpage/

    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]

    :param text: <str> text for translation.
    :return: <str> translated text.
    """
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'

    with open(news_file) as f:
        text = f.read()
        languages = (news_language, "-", result_language)
        params = {
            'key': key,
            'lang': languages,
            'text': text,
        }
        response = requests.get(url, params=params).json()
        translation = ' '.join(response.get('text', []))

    with open(news_result, "w") as f:
        f.write(translation)


def main():
    directory = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(os.path.join(directory, "result"))
    result_dir = os.path.join(directory, "result")
    current_dir = os.path.join(directory, "news")
    dir_files = os.listdir(current_dir)
    for file in dir_files:
        news_language = os.path.splitext(os.path.basename(file))[0].lower()
        result_language = "ru"
        news_file = os.path.join(current_dir, file)
        news_result = os.path.join(result_dir, file)
        translate_it(news_language, result_language, news_file, news_result)
main()
