import aula147_CONTA
import aula148_PESSOA


class Banco:
    def __init__(  # é uma lista ou (| significa OU) None
            self,
            agencias: list[int] | None = None,
            clientes: list[aula148_PESSOA.Pessoa] | None = None,
            contas: list[aula147_CONTA.Conta] | None = None,
    ):
        # se a algum desses abaixo for None, vai retornar uma lista vazia
        self.agencias = agencias or []
        self.clientes = clientes or [
        self.contas = contas or [

    def _checa_agencias(self, conta  # se a agencia desse conta tiver em
        # self.agencias retorne true
        if conta.agencia in self.agencias
            print('_checa_agencia', True
            return True

        print('_checa_agencia', False
        return False

    def _checa_cliente(self, cliente  # se o cliente q eu recebi aqui estiver
        # em self.clientes retorne true
        if cliente in self.clientes:
            print('_checa_cliente', True
            return True
        print('_checa_cliente', False
        return False

    def _checa_conta(self, conta
        print('_checa_conta', True
        if conta in self.contas:
            return True
        print('_checa_aconta', False
        return False

    def _checa_se_conta_e_do_cliente(self, cliente, conta
        if conta is cliente.conta:
            print('_checa_se_conta_e_do_cliente', True
            return True
        print('_checa_se_conta_e_do_cliente', False
        return False

    def autenticar(self, cliente: aula148_PESSOA.Pessoa, conta: aula147_CONTA.
                   Conta):
        return self._checa_agencias(conta) and 
            self._checa_cliente(cliente) and 
            self._checa_conta(conta) and 
            self._checa_se_conta_e_do_cliente(cliente, conta

    def __repr__(self
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r
        return f'{class_name} {attrs


if __name__ == '__main__':
    c1 = aula148_PESSOA.Cliente('luiz', 30
    cc1 = aula147_CONTA.ContaCorrente(111, 222, 0, 0
    c1.conta = cc1

    c2 = aula148_PESSOA.Cliente('brendon', 23
    cp1 = aula147_CONTA.ContaPoupanca(112, 223, 100
    c2.conta = cp1
    banco = Banco(
    banco.clientes.extend([c1, c2
    banco.contas.extend([cc1, cp1
    banco.agencias.extend([111, 222

    if banco.autenticar(c1, cc1
        cc1.depositar(10
        c1.conta.depositar(100
        print(c1.conta
