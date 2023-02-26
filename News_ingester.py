from flask import Flask, jsonify, request

app = Flask(__name__)

# List that stores news article_items
article_items = []

@app.route('/')
def index():
    return 'News Ingester welcomes you'

# For retrieving news article_items by author
@app.route('/article_items/<string:author>', methods=['GET'])
def get_articles_by_author(author):
    author_articles = []
    for article in article_items:
        if article['author'] == author:
            author_articles.append(article)
    return jsonify({'article_items': author_articles}), 200

# For retrieving all article_items
@app.route('/article_items', methods=['GET'])
def get_articles():
    return jsonify({'article_items': article_items}), 200

# For adding a new article_item
@app.route('/article_items', methods=['POST'])
def add_article():
    # From the request body, extracting the article data
    author = request.json.get('author')
    title = request.json.get('title')
    content = request.json.get('content')
    article = {'author': author, 'title': title, 'content': content}

    # Appending the article to article_items list
    article_items.append(article)
    
    # Returning the response of inserted article data
    return jsonify({'message': 'Article added to news feed.', 'article': article}), 201


# For deleting an article by it's title
@app.route('/article_items/<string:title>', methods=['DELETE'])
def delete_article(title):
    global article_items
    new_article_items = [article for article in article_items if article['title'] != title]
    if len(new_article_items) == len(article_items):
        return jsonify({'message': 'Article not found.'}), 404
    else:
        article_items = new_article_items
        return jsonify({'message': 'Article deleted from news feed.'}), 200

# For starting the server
if __name__ == '__main__':
    app.run(debug=True)