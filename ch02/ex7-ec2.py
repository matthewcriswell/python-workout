def check_for_name(article, names):
    names_set = set()
    [names_set.add(name.lower()) for name in names]

    filtered_article = []
    article_list = article.split()
    for word in article_list:
        if word.lower() in names_set:
            filtered_article.append(f"{len(word)*'_'}")
        else:
            filtered_article.append(word)
    filtered_article = ' '.join(filtered_article)
    return filtered_article


with open('test.txt', 'rt') as file:
    text = file.read()

