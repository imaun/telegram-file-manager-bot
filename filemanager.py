from database import Database


def create_directory(message: str, parent_id: int or None):
    dir_name = ' '.join(message.split(' ')[1:])
    if is_directory_exists(dir_name, parent_id):
        return False
    else:
        sql = """
            INSERT INTO [Entry]
                ([EntryType], [ParentId], [Name])
            VALUES
                (?, ?, ?)
        """
        with Database() as db:
            db.exec(sql, ['dir', parent_id, dir_name])
        return True


def is_directory_exists(dir_name: str, parent_id: int or None):
    sql = "SELECT COUNT(Id) FROM [Entry] WHERE [Name] = ? AND ParentId = ?"
    with Database() as db:
        result = db.query_single(sql, [dir_name, parent_id])
        return int(result[0]) > 0
