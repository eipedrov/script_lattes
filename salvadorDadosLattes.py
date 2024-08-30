import json
import csv
import pandas as pd

class SalvadorDadosLattes:
    def __init__(self, dados: dict) -> None:
        self.dados = dados

    def salvar_como_json(self, caminho_arquivo: str) -> None:
        try:
            with open(caminho_arquivo + '.json', 'w', encoding='utf-8') as f:
                json.dump(self.dados, f, ensure_ascii=False, indent=4)
            print(f"Dados salvos com sucesso em {caminho_arquivo}")
        except IOError as e:
            raise ValueError(f"Erro ao salvar os dados como JSON: {e}")

    def salvar_como_csv(self, caminho_arquivo: str) -> None:
        try:
            with open(caminho_arquivo + '.csv', 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                for key, value in self.dados.items():
                    writer.writerow([key, value])
            print(f"Dados salvos com sucesso em {caminho_arquivo}")
        except IOError as e:
            raise ValueError(f"Erro ao salvar os dados como CSV: {e}")

    def salvar_como_excel(self, caminho_arquivo: str) -> None:
        try:
            with pd.ExcelWriter(caminho_arquivo) as writer:
                for sheet_name, data in self.dados.items():
                    if isinstance(data, list) and data and isinstance(data[0], dict):
                        df = pd.DataFrame(data)
                    else:
                        df = pd.DataFrame([data])
                    df.to_excel(writer, sheet_name=sheet_name, index=False)
            print(f"Dados salvos com sucesso em {caminho_arquivo}")
        except IOError as e:
            raise ValueError(f"Erro ao salvar os dados como Excel: {e}")
