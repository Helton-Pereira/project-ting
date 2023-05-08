from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    file_path = ''

    for index in range(instance.__len__()):
        if instance.search(index)['nome_do_arquivo'] == path_file:
            file_path = instance.search(index)

    if file_path == '':
        text = txt_importer(path_file)
        lines = len(text)
        result = {
            'nome_do_arquivo': path_file,
            'qtd_linhas': lines,
            'linhas_do_arquivo': text,
        }
        instance.enqueue(result)
        print(f'{result}', file=sys.stdout)


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
