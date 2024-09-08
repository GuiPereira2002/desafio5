from abc import ABC, abstractmethod

# Interface para todos os exames
class Exame(ABC):
    @abstractmethod
    def verificar_condicoes(self):
        pass

# Classe para Exame de Sangue
class ExameSangue(Exame):
    def verificar_condicoes(self):
        # Implementa as condições específicas do exame de sangue
        print("Verificando condições para exame de sangue...")
        return True

# Classe para Exame de Raio-X
class ExameRaioX(Exame):
    def verificar_condicoes(self):
        # Implementa as condições específicas do exame de raio-x
        print("Verificando condições para Raio-X...")
        return True

# Classe de aprovação de exames
class AprovaExame:
    def aprovar_solicitacao_exame(self, exame: Exame):
        if exame.verificar_condicoes():
            print(f"{exame.__class__.__name__} aprovado!")

# Exemplo de uso:
exame_sangue = ExameSangue()
exame_raio_x = ExameRaioX()

aprovador = AprovaExame()
aprovador.aprovar_solicitacao_exame(exame_sangue)  # ExameSangue aprovado!
aprovador.aprovar_solicitacao_exame(exame_raio_x)  # ExameRaioX aprovado!
