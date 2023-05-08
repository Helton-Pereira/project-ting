def exists_word(word, instance):
    result = list()
    occurrences = list()

    for item in instance.data():
        count = 0
        for content in item['linhas_do_arquivo']:
            count += 1
            if word.lower() in content.lower():
                occurrences.append({'linha': count})
        if len(occurrences) < 1:
            return []

        result.append(
            {
                'palavra': word.lower(),
                'arquivo': item['nome_do_arquivo'],
                'ocorrencias': occurrences
            }
        )
    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
