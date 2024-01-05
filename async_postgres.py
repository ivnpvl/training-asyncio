import asyncio
import asyncpg
from random import sample
from typing import List, Tuple


def load_common_words() -> List[str]:
    with open('common_words.txt') as common_words:
        return common_words.readlines()


def generate_brand_names(words: List[str]) -> List[Tuple[str]]:
    return [(words[i].rstrip('\n'),) for i in sample(range(1000), 100)]


async def insert_brands(common_words, connection) -> int:
    brands = generate_brand_names(common_words)
    insert_command = "INSERT INTO brand VALUES(DEFAULT, $1)"
    return await connection.executemany(insert_command, brands)


async def main():
    common_words = load_common_words()
    connection = await asyncpg.connect(
        host='127.0.0.1',
        port=5432,
        user='postgres',
        database='products',
        password='password',
    )
    version = connection.get_server_version()
    print(f'Подключено! Версия postgres равна {version}.')
    await insert_brands(common_words, connection)
    await connection.close()


asyncio.run(main())
