import pytest

from src.service.phonebook import Phonebook


class TestPhonebook:

    def test_add_valid_entry(self):
        phonebook = Phonebook()

        assert phonebook.add("Prefeitura", "12345678901") == "Numero adicionado"
        assert "Prefeitura" in phonebook.entries
        assert phonebook.entries["Prefeitura"] == "12345678901"

    def test_add_invalid_name_with_special_characters(self):
        phonebook = Phonebook()

        assert phonebook.add("Escola#", "123") == "Nome invalido"
        assert phonebook.add("Escola@", "123") == "Nome invalido"
        assert phonebook.add("Escola!", "123") == "Nome invalido"
        assert phonebook.add("Escola$", "123") == "Nome invalido"
        assert phonebook.add("Escola%", "123") == "Nome invalido"

    def test_add_invalid_number(self):
        phonebook = Phonebook()

        assert phonebook.add("Prefeitura", "") == "Numero invalido"

    def test_add_duplicate_entry(self):
        phonebook = Phonebook()

        phonebook.add("Prefeitura", "1234567890")
        assert phonebook.add("Prefeitura", "9876543210") == "Nome ja existe"
        assert phonebook.entries["Prefeitura"] == "1234567890"

    def test_lookup_valid_name(self):
        phonebook = Phonebook()

        phonebook.add("Hospital", "1234567890")
        assert phonebook.lookup("Hospital") == "1234567890"

        phonebook.add("Clinica", "9876543210")
        assert phonebook.lookup("Clinica") == "9876543210"

    def test_lookup_invalid_name_with_special_characters(self):
        phonebook = Phonebook()

        phonebook.add("Delegacia", "123")

        assert phonebook.lookup("Delegacia#") == "Nome invalido"
        assert phonebook.lookup("Delegacia@") == "Nome invalido"
        assert phonebook.lookup("Delegacia!") == "Nome invalido"
        assert phonebook.lookup("Delegacia$") == "Nome invalido"
        assert phonebook.lookup("Delegacia%") == "Nome invalido"

    def test_lookup_name_not_found(self):
        phonebook = Phonebook()

        phonebook.add("Postinho", "1234567890")

        result = phonebook.lookup("Non Existent Name")
        assert result == "Nome invalido"

    def test_lookup_empty_phonebook(self):
        phonebook = Phonebook()

        result = phonebook.lookup("Non Existent Name")
        assert result == "Nome invalido"

    def test_get_names_with_entries(self):
        phonebook = Phonebook()

        assert set(phonebook.get_names()) == {"POLICIA"}

    def test_get_numbers_with_entries(self):

        phonebook = Phonebook()

        assert set(phonebook.get_numbers()) == {"190"}

    def test_clear_phonebook(self):

        phonebook = Phonebook()
        phonebook.add("Hospital", "456")

        assert len(phonebook.entries) == 2

        result = phonebook.clear()
        assert result == "phonebook limpo"

        assert len(phonebook.entries) == 0

    def test_search_match(self):

        phonebook = Phonebook()

        result = phonebook.search("POLICIA")
        assert result == [{'POLICIA': '190'}]

    def test_search_no_matches(self):

        phonebook = Phonebook()
        phonebook.add("Clinica", "654")

        result = phonebook.search("Posto")
        assert result == []

    def test_get_phonebook_sorted(self):

        phonebook = Phonebook()
        phonebook.add("Hospital", "1234567890")
        phonebook.add("Prefeitura", "0987654321")

        print(phonebook.entries)

        expected = {
            "POLICIA": "190",
            "Hospital": "1234567890",
            "Prefeitura": "0987654321"
        }

        result = phonebook.get_phonebook_sorted()
        print(result)
        assert result == expected

    def test_get_phonebook_reverse(self):

        phonebook = Phonebook()
        phonebook.add("Hospital", "1234567890")
        phonebook.add("Prefeitura", "0987654321")

        expected = {
            "POLICIA": "190",
            "Hospital": "1234567890",
            "Prefeitura": "0987654321"
        }

        result = phonebook.get_phonebook_reverse()
        assert result == expected

    def test_delete_existing_name(self):

        phonebook = Phonebook()

        assert "POLICIA" in phonebook.entries
        result = phonebook.delete("POLICIA")

        assert result == "Numero deletado"
        assert "POLICIA" not in phonebook.entries

    def test_delete_non_existent_name(self):
        phonebook = Phonebook()

        result = phonebook.delete("Posto")

        assert result == "Nome não encontrado"


