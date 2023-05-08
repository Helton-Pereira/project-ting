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
    if instance.__len__() == 0:
        print('Não há elementos', file=sys.stdout)
    else:
        file_path = instance.dequeue()
        print(
            f"Arquivo {file_path['nome_do_arquivo']} removido com sucesso",
            file=sys.stdout)


def file_metadata(instance, position):
    try:
        print(f'{instance.search(position)}')
    except IndexError:
        print('Posição inválida', file=sys.stderr)
