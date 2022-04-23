from PyQt5 import QtCore
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5.QtWidgets import (
    QMessageBox, QVBoxLayout, QTableView, QDialog, QAbstractItemView
)


class List(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("List")
        self.resize(415, 200)

        create_connection()
        self.createTableQuery = QSqlQuery()
        self.createTableQuery.exec(
            """
            CREATE TABLE list (
                id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
                al_time STRING NOT NULL
            )
            """
        )

        main_layout = QVBoxLayout()

        self.model = QSqlTableModel(self)
        self.model.setTable('list')
        self.refresh()

        self.view_list = QTableView()
        self.view_list.setModel(self.model)
        self.view_list.setEditTriggers(QAbstractItemView.NoEditTriggers)

        main_layout.addWidget(self.view_list)

        self.setLayout(main_layout)

    def refresh(self):
        self.model.setSort(1, QtCore.Qt.AscendingOrder)
        self.model.select()

    def create_new_record(self, time):
        insert_sql = 'INSERT INTO list (al_time) VALUES (?)'
        query = QSqlQuery()
        query.prepare(insert_sql)
        query.addBindValue(time)
        if not query.exec_():
            print(query.lastError())
        else:
            print('inserted')
            self.refresh()

    def delete_record(self, time):
        query = QSqlQuery()
        query.exec("""SELECT * FROM list""")
        while query.next():
            if query.value('al_time') == time:
                id_al = query.value('id')
        query.exec(f"""DELETE FROM list WHERE id = {id_al}""")
        if not query.exec_():
            print(query.lastError())
        else:
            print('deleted')
            self.refresh()


def create_connection():
    connect = QSqlDatabase.addDatabase("QSQLITE")
    connect.setDatabaseName("alarm_clock_db.sqlite")
    connect.open()

    if not connect.open():
        QMessageBox.critical(
            None,
            "QTableView Example - Error!",
            "Database Error: %s" % connect.lastError().databaseText()
        )
        return False
    return True
