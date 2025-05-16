import matplotlib

matplotlib.use('Agg')  # Важно: до импорта pyplot!
import matplotlib.pyplot as plt
from io import BytesIO
import base64
import sqlite3
import pandas as pd


def generate_filter_plot() -> str:

    db = sqlite3.connect("C:/Users/User/PycharmProjects/pythonProject5/rosatom_project/backend/filters1.db")

    try:
        query = "SELECT status_text, timestamp FROM filter_data ORDER BY timestamp"
        df = pd.read_sql_query(query, db)

        plt.figure(figsize=(10, 5))
        plt.plot(df['timestamp'], df['status_text'],
                 marker='o',
                 linestyle='-',
                 color='green',
                 label='Состояние фильтра')

        plt.title('Состояние фильтра')
        plt.xlabel('Дата')
        plt.ylabel('Состояние')
        plt.xticks(rotation=45)
        plt.grid(True, linestyle=':')
        plt.legend()
        plt.tight_layout()

        # Сохраняем в буфер вместо файла
        buf = BytesIO()
        plt.savefig(buf, format='png', dpi=600, bbox_inches='tight')
        buf.seek(0)

        return base64.b64encode(buf.read()).decode()

    finally:
        plt.close()
        db.close()
