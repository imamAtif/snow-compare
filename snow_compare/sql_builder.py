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
