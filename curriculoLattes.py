class CurriculoLattes():
    autor = None
    resumo = None

    def exibeInfoCurriculo(self):
        print("Curriculo Lattes de " + self.autor + "\n\n")
        print(self.resumo)
