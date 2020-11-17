import sqlite3
import mysql.connector
from util.db.fmt_table import FormatTable
from datetime import datetime

class LiteTable(FormatTable):

    def config(self, table_name, schema, params):
        super().config(table_name, schema, params)
        if 'user' in params:
            self.connection = mysql.connector.connect(**params)
        else:
            self.connection = sqlite3.connect(
                params['database'], 
                check_same_thread=False
            )
        self.cache = {}

    def execute(self, command, need_commit):
        print('-'*100)
        print(command)
        print('-'*100)
        cursor = self.connection.cursor()
        cursor.execute(command)
        if need_commit:
            self.connection.commit()
            self.cache = {}
        return cursor

    def get_max(self):
        command = 'SELECT max({}) FROM {}'.format(
            self.pk_fields[0],
            self.table_name
        )
        result = self.execute(command, False).fetchall()
        return result[0][0]

    def find_all(self, limit=0, filter_expr=''):
        field_list = list(self.map)
        command = 'SELECT {} FROM {}{}{}'.format(
            ','.join(field_list),
            self.table_name,
	        f' WHERE {filter_expr}' if filter_expr else '',
	        f' LIMIT {limit}' if limit else ''
        )
        if self.cache and filter_expr:
            result = self.cache.get(filter_expr)
            if result:
                return result
        dataset = self.execute(command, False).fetchall()
        result = []
        for values in dataset:
            record = {}
            for field, value in zip(field_list, values):
                if field in self.joins:
                    join = self.joins[field]
                    value = join.find_one(value, True)
                if 'date' in str(type(value)):
                    value = value.strftime('%Y-%m-%d')
                record[field] = value
            result.append(record)
        if filter_expr:
            self.cache[filter_expr] = result
        return result

    def find_one(self, values, only_pk=False):
        found = self.find_all(
            1, self.get_conditions(values, only_pk=only_pk)
        )
        if found:
            return found[0]
        return None

    def delete(self, values):
        command = 'DELETE FROM {} WHERE {}'.format(
            self.table_name,
            self.get_conditions(values)
        )
        self.execute(command, True)

    def insert(self, json_data):
        for field, value in json_data.items():
            if field in self.joins:
                join = self.joins[field]
                found = join.find_one(value, False)
                if not found:
                    errors = join.insert(value)
                    if errors:
                        return errors
                    found = join.find_one(value, False)
                json_data[field] = found
        errors = super().insert(json_data)
        if errors:
            return errors
        command = self.get_command(
            json_data,
            is_insert=True,
            use_quotes=False
        )
        self.execute(command, True)
        return None

    def update(self, json_data):
        if not json_data:
            return 'No data to update'
        command = self.get_command(
            json_data,
            is_insert=False,
            use_quotes=False
        )
        self.execute(command, True)
        return None
