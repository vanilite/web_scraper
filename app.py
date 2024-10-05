import requests
from bs4 import BeautifulSoup

def get_content(link):
    try: 
        response = requests.get(link)
        response.raise_for_status()
    
        soup = BeautifulSoup(response.text, 'html.parser')
    
        title = soup.find('h1').get_text(strip=True) if soup.find('h1') else 'No title found'
    
        updated_date = soup.find('time').get_text(strip=True) if soup.find('time') else 'No date found'
    
        byline = soup.find('div', class_='!text-brand.text-sm.font-normal').get_text(strip=True) if soup.find('div', class_='!text-brand.text-sm.font-normal') else 'No byline found'
    
        article_content = soup.find('div', class_='ciam-article-pf1').get_text(strip=True) if soup.find('div', class_='ciam-article-pf1') else 'No content found'
        return {
            'title': title,
            'updated_date': updated_date,
            'byline': byline,
            'content': article_content
        }
    
    except requests.RequestException as e:
        return {'error': f'Network error: {e}'}
    except Exception as e:
        return {'error': f'Error: {e}'}
    
if __name__ == '__main__':
    link = 'https://www.planetf1.com/news/michael-schumacher-accident-what-happened-condition'
    content = get_content(link)
    print(content)
