import asyncio
from cgitb import html

from prompt_toolkit import output
from aiohttp import ClientSession
import pathlib


sort_by = {
    "Ranking": "rk",
    "IMDb Rating": "ir",
    "Release Date": "us",
    "Number of Ratings": "nv"
}


async def fetch_url(url, session, sort_by=None):
    async with session.get(url) as response:
        html_body = await response.read()
        return {
            "body": html_body,
            "sortBy": sort_by
        }


async def fetch_url_semaphore(url, session, sort_by, semaphore):
    async with semaphore:
        return await fetch_url(url, session, sort_by)


async def main():
    global sort_by
    tasks = []
    semaphore = asyncio.Semaphore(10)  # number of tasks per given time
    async with ClientSession() as session:
        for k, v in sort_by.items():
            url = f"https://www.imdb.com/chart/moviemeter/?sort={v},asc&mode=simple&page=1"
            tasks.append(
                asyncio.create_task(
                    fetch_url_semaphore(url, session, k, semaphore)
                )
            )
        pages_content = await asyncio.gather(*tasks)
        return pages_content

results = asyncio.get_event_loop().run_until_complete(main())
output_directory = pathlib.Path().resolve() / "Movie Ratings"
output_directory.mkdir(parents=True, exist_ok=True)

for result in results:
    sort_way = result.get("sortBy")
    html_data = result.get("body")
    output_file = output_directory / f"{sort_way}.html"
    output_file.write_text(html_data.decode())
