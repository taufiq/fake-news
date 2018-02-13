from newspaper import Article
import csv
import os
import pred


def parseArticle(url):
    article = Article(url=url)
    article.download()
    article.parse()

    with open('single_body.csv', 'w') as f:  # formatted = str(article.text).replace("\n", "")
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        writer.writerow(['Body ID', 'articleBody'])
        writer.writerow(['1', article.text])

    with open('single_stance_unlabeled.csv', 'w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL)
        writer.writerow(['Headline', 'Body ID'])
        writer.writerow([article.title, '1'])
    # Load result
    return [article.title, article.text, pred.runPredictor('load')]
