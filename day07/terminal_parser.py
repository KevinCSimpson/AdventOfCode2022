from day07.dir import Dir
from day07.file import File


class TerminalParser(object):

    @staticmethod
    def parse(rows: list[str]) -> Dir:
        root = Dir(None)
        cursor = root
        for row in rows:
            if row[0] == '$':
                if row[2:4] == 'cd':
                    match row[5:]:
                        case '/':
                            cursor = root
                        case '..':
                            cursor = cursor.get_parent()
                        case _:
                            cursor.add_child(row[5:], Dir(cursor))
                            cursor = cursor.get_child(row[5:])
            else:
                parts = row.split(' ')
                if parts[0] == 'dir':
                    cursor.add_child(parts[1], Dir())
                else:
                    cursor.add_child(parts[1], File(int(parts[0])))
        
        return root