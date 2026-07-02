def build_row_count_sql(left_table: str, right_table: str) -> str:
    """
    Build SQL query to count rows in two tables."""
    sql_query = (
        f"SELECT '{left_table}' AS table_name, COUNT(*) as row_count FROM {left_table} "
        f"UNION ALL SELECT '{right_table}' AS table_name, COUNT(*) as row_count FROM {right_table};"
    )

    return sql_query


def build_distinct_count_sql(left_table: str, right_table: str, key: str) -> str:
    """
    Build SQL query to compare distinct key counts in two tables.
    """
    sql_query = (
        f"SELECT '{left_table}' AS table_name, COUNT(DISTINCT {key}) AS distinct_key_count FROM {left_table}\n"
        "UNION ALL\n"
        f"SELECT '{right_table}' AS table_name, COUNT(DISTINCT {key}) AS distinct_key_count FROM {right_table};"
    )

    return sql_query


def build_missing_keys_right_table_sql(
    left_table: str, right_table: str, key: str
) -> str:
    """
    Build SQL query to find missing keys in the right table compared to the left table.
    """
    sql_query = (
        f"SELECT\n"
        f"    l.{key}\n"
        f"FROM {left_table} AS l\n"
        f"LEFT JOIN {right_table} AS r\n"
        f"    ON l.{key} = r.{key}\n"
        f"WHERE r.{key} IS NULL;"
    )

    return sql_query


def build_missing_keys_left_table_sql(
    left_table: str, right_table: str, key: str
) -> str:
    """
    Build SQL query to find missing keys in the left table compared to the right table.
    """
    sql_query = (
        f"SELECT\n"
        f"    r.{key}\n"
        f"FROM {right_table} AS r\n"
        f"LEFT JOIN {left_table} AS l\n"
        f"    ON r.{key} = l.{key}\n"
        f"WHERE l.{key} IS NULL;"
    )

    return sql_query


def build_missing_keys_both_tables_sql(
    left_table: str, right_table: str, key: str
) -> str:
    """
    Build SQL query to find missing keys in both tables.
    """
    sql_query = (
        f"SELECT\n"
        f"    l.{key} AS missing_in_right\n"
        f"FROM {left_table} AS l\n"
        f"LEFT JOIN {right_table} AS r\n"
        f"    ON l.{key} = r.{key}\n"
        f"WHERE r.{key} IS NULL\n"
        f"UNION ALL\n"
        f"SELECT\n"
        f"    r.{key} AS missing_in_left\n"
        f"FROM {right_table} AS r\n"
        f"LEFT JOIN {left_table} AS l\n"
        f"    ON r.{key} = l.{key}\n"
        f"WHERE l.{key} IS NULL;"
    )

    return sql_query

