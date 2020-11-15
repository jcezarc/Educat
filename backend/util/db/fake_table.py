import json
from util.db.db_table import DbTable

class FakeTable(DbTable):
    def config(self, table_name, schema, params):
        super().config(table_name, schema, params)
        self.internal_data = []

    def insert(self, json_data):
        errors = self.validator.validate(json_data)
        if errors:
            return errors
        self.internal_data.append(json_data)
        return None

    def find_one(self, values, only_pk=False):
        self.get_conditions(values, only_pk=only_pk)
        for record in self.internal_data:
            match = True
            for item in self.conditions:
                field, value = item
                if record[field] != value:
                    match = False
                    break
            if match:
                return record
        return None

    def update(self, json_data):
        found = self.find_one(json_data, True)
        if not found:
            raise Exception('Record not found to update')
        pos = self.internal_data.index(found)
        self.internal_data[pos] = json_data

    def add_condition(self, field, value):
        self.conditions.append(
            (field, value)
        )
    