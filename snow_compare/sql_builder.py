def build_row_count_sql(left_table: str, right_table: str) -> str:
    """
    Build SQL query to count rows in two tables."""
    sql_query = (
        f"SELECT COUNT(*) as row_count FROM {left_table} "
        f"UNION ALL SELECT COUNT(*) as row_count FROM {right_table};"
    )

    return sql_query
