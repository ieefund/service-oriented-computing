import pprint

import requests
from flask import Blueprint, render_template

from keys import KAKAO_REST_KEY
from rest_client.read_kakao import KAKAO_BASE_URL
from views.auth import kakao_oauth

menus_blueprint = Blueprint('menus', __name__)
@menus_blueprint.route('/main')
def menus_main():
    return 'welcome news {0}'.format("hakjae")

@menus_blueprint.route('/sports')
def menus_sports():
    return 'welcome sports news {0}'.format("hakjae")

@menus_blueprint.route('/images')
def images():

    headers = {'Authorization': 'KakaoAK ' + KAKAO_REST_KEY}

    res1 = requests.get(
        url=KAKAO_BASE_URL + "/v2/search/image?query=김고은",
        headers=headers
    )
    if res1.status_code == 200:
        docs = res1.json()
        pprint.pprint(docs)
        images = []
        for image in docs['documents']:
            images.append(image['image_url'])

        print(images)
    else:
        print("Error {0} {1}".format(res1.status_code, res1.text))

    return render_template(
        'Images.html', images=images, nav_menu="images", kakao_oauth=kakao_oauth
    )

@menus_blueprint.route('/books')
def books():

    headers = {'Authorization': 'KakaoAK ' + KAKAO_REST_KEY}

    res2 = requests.get(
        url=KAKAO_BASE_URL + "/v3/search/book?query=Maxim",
        headers=headers
    )
    if res2.status_code == 200:
        docs = res2.json()
        books = docs['documents'];
        # for book in docs['documents']:
        #     bookImg.append(book['thumbnail'])
        #     print("{0:50s} - {1:20s}".format(str(book['title']), str(book['authors'])))
        #
        # print(books)
    else:
        print("Error {0} {1}".format(res2.status_code, res2.text))

    return render_template(
        'books.html', books=books, nav_menu="books", kakao_oauth=kakao_oauth
    )

@menus_blueprint.route('/searchs')
def searchs():

    headers = {'Authorization': 'KakaoAK ' + KAKAO_REST_KEY}

    res2 = requests.get(
        url=KAKAO_BASE_URL + "/v3/search/book?query=Maxim",
        headers=headers
    )
    if res2.status_code == 200:
        docs = res2.json()
        books = docs['documents'];
        # for book in docs['documents']:
        #     bookImg.append(book['thumbnail'])
        #     print("{0:50s} - {1:20s}".format(str(book['title']), str(book['authors'])))
        #
        # print(books)
    else:
        print("Error {0} {1}".format(res2.status_code, res2.text))

    return render_template(
        'searchs.html', searchs=searchs, nav_menu="searchs", kakao_oauth=kakao_oauth
    )

@menus_blueprint.route('/uploads')
def uploads():

    return render_template(
        'uploads.html', uploads=uploads, nav_menu="uploads", kakao_oauth=kakao_oauth
    )

