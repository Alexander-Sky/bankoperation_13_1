"""
Модуль для чтения финансовых транзакций из CSV и Excel файлов.
"""

import csv
from typing import List, Dict, Any

import pandas as pd


def read_csv_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает CSV-файл и возвращает список словарей с транзакциями.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            transactions = list(reader)

            for transaction in transactions:
                for key, value in transaction.items():
                    if value == '':
                        transaction[key] = None

            return transactions
    except FileNotFoundError:
        print(f"Файл {file_path} не найден")
        return []
    except Exception as e:
        print(f"Ошибка при чтении CSV файла: {e}")
        return []


def read_excel_file(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает Excel-файл и возвращает список словарей с транзакциями.
    """
    try:
        df = pd.read_excel(file_path)
        df = df.where(pd.notnull(df), None)

        transactions = df.to_dict('records')
        if isinstance(transactions, list):
            return transactions
        return []
    except FileNotFoundError:
        print(f"Файл {file_path} не найден")
        return []
    except Exception as e:
        print(f"Ошибка при чтении Excel файла: {e}")
        return []


def read_csv_with_pandas(file_path: str) -> List[Dict[str, Any]]:
    """
    Читает CSV-файл с помощью pandas (альтернативный метод).
    """
    try:
        df = pd.read_csv(file_path, sep=';')
        df = df.where(pd.notnull(df), None)

        transactions = df.to_dict('records')
        if isinstance(transactions, list):
            return transactions
        return []
    except FileNotFoundError:
        print(f"Файл {file_path} не найден")
        return []
    except Exception as e:
        print(f"Ошибка при чтении CSV файла с pandas: {e}")
        return []