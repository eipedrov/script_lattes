import json
import pandas as pd

class SalvadorDadosLattes:
    def __init__(self, dados: dict) -> None:
        self.dados = dados

    def salvar_como_json(self, caminho_arquivo: str) -> None:
        """Salva os dados no formato JSON."""
        try:
            caminho_completo = caminho_arquivo + '.json'
            with open(caminho_completo, 'w', encoding='utf-8') as f:
                json.dump(self.dados, f, ensure_ascii=False, indent=4)
            print(f"Dados salvos com sucesso em {caminho_completo}")
        except IOError as e:
            raise ValueError(f"Erro ao salvar os dados como JSON: {e}")

    def salvar_como_excel(self, caminho_arquivo: str) -> None:
        """Salva os dados no formato Excel com melhor estruturação."""
        try:
            caminho_completo = caminho_arquivo + '.xlsx'
            with pd.ExcelWriter(caminho_completo) as writer:
                for sheet_name, data in self.dados.items():
                    if isinstance(data, list) and data and isinstance(data[0], dict):
                        # Quando os dados são uma lista de dicionários, convertê-los diretamente para DataFrame
                        df = pd.DataFrame(data)
                    else:
                        # Quando os dados são dicionários simples, colocá-los em DataFrame com uma linha
                        df = pd.DataFrame([data])
                    # Salva cada tipo de dado em uma aba separada
                    df.to_excel(writer, sheet_name=sheet_name, index=False)
            print(f"Dados salvos com sucesso em {caminho_completo}")
        except IOError as e:
            raise ValueError(f"Erro ao salvar os dados como Excel: {e}")
