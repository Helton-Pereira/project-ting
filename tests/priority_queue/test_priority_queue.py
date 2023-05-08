from ting_file_management.priority_queue import PriorityQueue
import pytest


mock = [
    {
        'nome_do_arquivo': 'text1.txt',
        'qtd_linhas': 2,
        'linhas_do_arquivo': ['Exemplo', 'teste'],
    },
    {
        'nome_do_arquivo': 'text2.txt',
        'qtd_linhas': 5,
        'linhas_do_arquivo': ['Exemplo', 'teste', 'vejamos', 'se', 'funciona'],
    }
]


def test_basic_priority_queueing():
    instance = PriorityQueue()

    instance.enqueue(mock[0])
    assert len(instance.high_priority) == 1

    instance.enqueue(mock[1])
    assert len(instance.regular_priority) == 1

    assert instance.search(1) == mock[1]

    instance.dequeue()
    assert len(instance.high_priority) == 0

    with pytest.raises(IndexError, match='Índice Inválido ou Inexistente'):
        instance.search(3)
