class Phonebook:

    def __init__(self):
        self.entries = {'POLICIA': '190'}

    def add(self, name, number):
        """

        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """
        # Validação do nome
        # foi alterado a forma de validação para considerar todas as validações juntas
        if any(char in name for char in ['#', '@', '!', '$', '%']):
            return 'Nome invalido'  # aqui tinha uma mensagem com erro de digitação

        # Validação do número
        if not number.isdigit() or len(number) == 0:
            return 'Numero invalido'  # aqui tinha uma mensagem com erro de digitação

        # Adiciona o nome e número à agenda
        # Adicionei a validação para caso o nome já estiver sido adicionado
        if name not in self.entries:
            self.entries[name] = number
            return 'Numero adicionado'
        else:
            return 'Nome ja existe'

    def change_number(self, name, number):
        if not isinstance(name, str) or not isinstance(number, str):
            return "O nome e o numero devem ser strings"
        if name is None or number is None:
            return "O campo nome ou numero não podem ser vazios"
        for user in self.store.bd:
            if user.name == name:
                user.job = new_job
                return "Usuário atualizado com sucesso!"
        return "Usuário não encontrado!"

    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        if name in self.entries:
            return self.entries[name]
        else:
            return 'Nome invalido'  # aqui tinha uma mensagem com erro de digitação

    def get_names(self):
        """

        :return: return all names in phonebook
        """
        return list(self.entries.keys())  # no return estava faltando trazer uma lista ao inves de uma entrada somente

    def get_numbers(self):
        """

        :return: return all numbers in phonebook
        """
        return list(self.entries.values())  # no return estava faltando trazer uma lista ao inves de uma entrada somente

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """
        self.entries.clear()  # faltou chamar a função clear ao inves de passar uma lista vazia
        return 'phonebook limpo'  # poderia ser limpo

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        result = []
        for name, number in self.entries.items():
            if search_name.lower() in name.lower():  # a busca vai ser feita com caracteres lowercase
                result.append({name: number})
        return result

    def get_phonebook_sorted(self):
        """

        :return: return phonebook in sorted order
        """
        sorted_entries = sorted(self.entries.items())
        return dict(sorted_entries)  # adicionei a função para fazer a ordenação da lista

    def get_phonebook_reverse(self):
        """

        :return: return phonebook in reverse sorted order
        """
        sorted_entries = sorted(self.entries.items(), reverse=True)  # adicionei a função para fazer a ordenação da lista
        return dict(sorted_entries)

    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        if name in self.entries:  # foi reescrito essa função afim de adicionar mais validações a função de delete
            self.entries.pop(name)
            return 'Numero deletado'
        else:
            return 'Nome não encontrado'
