from typing import LiteralString, Optional


def execute_query(sql: LiteralString, parameters: Optional[tuple[str]] = None) -> str:
    return sql


if __name__ == "__main__":
    # def query_user(user_id: str) -> str:
    #     query = f"SELECT * FROM data WHERE user_id = {user_id}"
    #     return execute_query(query) expect-type-error

    def query_data(user_id: str, limit: bool) -> None:
        query = """
            SELECT
                user.name,
                user.age
            FROM data
            WHERE user_id = ?
        """

        if limit:
            query += " LIMIT 1"

        execute_query(query, (user_id,))
