import asyncio
import asyncpg

import util.postgres_commands as pscmd


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
        pscmd.CREATE_BRAND_TABLE,
        pscmd.CREATE_PRODUCT_TABLE,
        pscmd.CREATE_PRODUCT_COLOR_TABLE,
        pscmd.CREATE_PRODUCT_SIZE_TABLE,
        pscmd.SIZE_INSERT,
        pscmd.COLOR_INSERT,
    ]
    print('Создаётся база данных product...')
    for statement in statements:
        status = await connection.execute(statement)
        print(status)
    print('База данных product создана.')
    await connection.close()


asyncio.run(main())
