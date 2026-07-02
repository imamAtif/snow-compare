from snow_compare.sql_builder import build_row_count_sql


def test_build_row_count_sql_contains_left_and_right_tables():
    sql = build_row_count_sql(
        left_table="DB.SCHEMA.LEFT_TABLE",
        right_table="DB.SCHEMA.RIGHT_TABLE",
    )

    assert "DB.SCHEMA.LEFT_TABLE" in sql
    assert "DB.SCHEMA.RIGHT_TABLE" in sql
    assert "COUNT(*) as row_count" in sql
    assert "UNION ALL" in sql
