import stardict


def init_sqlite_from_7z(zip_file="stardict.7z", target_db_file="stardict.db"):
    # check if py7zr module installed
    try:
        import py7zr
    except:
        print("py7zr module not found, please use pip to install")
        exit(1)

    print("start extracting 7z file: ", zip_file)
    with py7zr.SevenZipFile(zip_file, mode='r') as z:
        z.extractall(path="./")
    print("successfully extracted 7z file: ", zip_file)

    print("now start converting csv to sqlite")
    stardict.convert_dict(target_db_file, "stardict.csv")
    print("extracted and converted, target db file name: ", target_db_file)


def transform_sqlite_to_mysql(mysql_address, sqlite_file="stardict.db"):
    stardict.convert_dict(mysql_address, sqlite_file)


def get_stardict(db_file="stardict.db") -> stardict.StarDict:
    return stardict.StarDict(db_file)


if __name__ == "__main__":
    # init_sqlite_from_7z()

    # transform_sqlite_to_mysql()

    # db info
    db = {'host': '127.0.0.1', 'user': 'root', 'passwd': 'TODO', 'db': 'engai'}
    # init mysql
    stardict.DictMySQL(db, init=True)

    transform_sqlite_to_mysql(db)

    pass
