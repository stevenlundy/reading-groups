from sql import get_connection
from sql.migration import MYSQL_UPGRADE, MYSQL_DOWNGRADE

def run_migration():
    conn = get_connection()
    results = [r for r in conn.cursor().execute(MYSQL_UPGRADE, multi=True)]
    conn.commit()

def run_downgrade():
    conn = get_connection()
    result = [r for r in conn.cursor().execute(MYSQL_DOWNGRADE, multi=True)]
    conn.commit()
