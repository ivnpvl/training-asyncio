import asyncio
import asyncpg

import util.postgres_commands as pgcmd


async def main():
    connection = await asyncpg.connect(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        database='products',
        password='password',
    )
    version = connection.get_server_version()
    print(f'Подключено! Версия postgres равна {version}.')
    statements = [
        pgcmd.CREATE_BRAND_TABLE,
        pgcmd.CREATE_PRODUCT_TABLE,
        pgcmd.CREATE_PRODUCT_COLOR_TABLE,
        pgcmd.CREATE_PRODUCT_SIZE_TABLE,
        pgcmd.SIZE_INSERT,
        pgcmd.COLOR_INSERT,
    ]
    print('Создаётся база данных product...')
    for statement in statements:
        print(statement)
        status = await connection.execute(statement)
        print(status)
    print('База данных product создана.')
    await connection.close()


asyncio.run(main())
