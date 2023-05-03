from django.core.files.base import ContentFile
from bs4 import BeautifulSoup
import requests
from .validators import is_favorite


def get_slug(array: list[str]) -> str:
    string = ''
    for a in array:
        string += a + '-'
    return string[:-1]


def get_products_overview(keywords: str) -> list[object]:
    search_url = 'https://www.cgtrader.com/3d-models?keywords=' + \
        keywords.replace(' ', '+') + "+jewelry"
    page_content = requests.get(search_url)
    soup = BeautifulSoup(page_content.text, 'html.parser')
    main_images = soup.select('img.item-main-image')
    urls = soup.select('a.content-box__link')
    results = []
    for i in range(len(main_images)):
        url = urls[i]['href']
        image = main_images[i]['data-src']
        favorite = is_favorite(url)
        product = {'image': image, 'url': url, 'is_favorite': favorite}
        if favorite:
            results.insert(0, product)
        else:
            results.append(product)
    return results
    # return list(map(lambda img, url: {'image': img['data-src'], 'url': url.attrs['href']}, main_images, urls))


# Search for items


def cgt_search(keywords: str) -> list[str]:
    """
    Return the url of all the items founded
    """
    search_url = 'https://www.cgtrader.com/3d-models?keywords=' + \
        keywords.replace(' ', '+')
    page_content = requests.get(search_url)
    soup = BeautifulSoup(page_content.text, 'html.parser')
    items = soup.select('a.content-box__link')

    return list(map(lambda i: i.attrs['href'], items))


#  Get info for each item
def get_product_info(url: str, collection: str) -> object:
    page_content = requests.get(url)
    index = page_content.text.find('The collection consists of')
    # If the text is founded (index > 0) this is a collection. We are looking for just for individual items
    if (page_content.ok and index < 0):
        soup = BeautifulSoup(page_content.text, 'html.parser')

        tags = list(map(lambda t: t.text, soup.select('li.label')))
        image_url = soup.select_one(
            'div.product-carousel__image').select_one('img').attrs['src']
        image_binary = requests.get(image_url).content

        data = {
            'title': get_slug(tags),
            'url': url,
            'collection': collection,
            'image': ContentFile(image_binary, 'file.jpg')
        }

        return data

    return None


#  Add item to DB


def add_image_to_db(product_info: object) -> requests.Response.ok:
    headers = {'charset': 'utf-8',
               'Content-type': 'multipart/form-data, application/json'}
    try:
        response = requests.post('http://localhost:8000/photos/images/',
                                 data=product_info['data'], files=product_info['files'])
        print('Product added')
    except:
        print('Product not added')
    return response.ok


if __name__ == '__main__':
    print('Getting products')
    products_urls = cgt_search('jewelry engagement ring')

    for url in products_urls:
        print('Get info from: ', url)
        product_info = get_product_info(url, 'engagement')

        if product_info == None:
            continue

        print('Adding product to DB')
        response = add_image_to_db(product_info)
