import asyncio
import logging
from aiohttp import ClientSession
from util import async_timed, fetch_status


@async_timed()
async def main():
    async with ClientSession() as session:
        urls = ['https://example.com' for _ in range(10)]
        pending = [
            asyncio.create_task(fetch_status(session, url)) for url in urls
        ]
        while pending:
            done, pending = await asyncio.wait(
                pending,
                return_when=asyncio.FIRST_COMPLETED,
            )
            print(f'Число завершившихся задач: {len(done)}.')
            print(f'Число ожидающих задач: {len(pending)}.')
            for done_task in done:
                if not done_task.exception():
                    print(done_task.result())
                else:
                    logging.error(
                        'При выполнении запроса возникло исключение:',
                        exc_info=done_task.exception(),
                    )
                    for pending_task in pending:
                        pending_task.cancel()

asyncio.run(main())
