import pytest

from skiplist import SkipList


@pytest.fixture
def alphabet_list():
    skl = SkipList()
    [skl.insert(chr(65+i), i) for i in range(26)]
    skl.print()
    return skl


def test_insertion():
    skl = SkipList()
    skl.insert('A', 100)
    skl.insert('B', 200)
    assert skl.header.forward[0].key == 'A'
    assert skl.header.forward[0].val == 100
    assert skl.header.forward[0].forward[0].key == 'B'
    assert skl.header.forward[0].forward[0].val == 200


def test_search(alphabet_list):
    node = alphabet_list.search('A')
    assert node is not None
    assert node.key == 'A'


def test_deletion(alphabet_list):
    assert 'A' in alphabet_list
    alphabet_list.delete('A')
    assert 'A' not in alphabet_list

    assert 'B' in alphabet_list
    alphabet_list.delete('B')
    assert 'B' not in alphabet_list

    # Can attempt to delete non-existent entry
    alphabet_list.delete('XX')

