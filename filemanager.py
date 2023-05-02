from database import Database


def list(parent_id: int or None):
    sql = """
        SELECT * FROM [Entry] WHERE [ParentId] = ?
    """
    with Database() as db:
        return db.query(sql, parent_id)


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


def new_file(filename: str, file_id: str, dir_id: int or None):
    sql = """
        INSERT INTO [Entry]
            ([Name], [EntryType], [FileId], [ParentId], [Desc])
        VALUES
            (?, ?, ?, ?, ?)
    """
    with Database() as db:
        db.exec(sql, [filename, 'file', file_id, dir_id, None])


def update_file(file_id: str, desc: str):
    sql = """
        UPDATE [Entry] SET [Desc] = ? WHERE [Id] = ?
    """
    with Database() as db:
        db.exec(sql, [desc, file_id])
